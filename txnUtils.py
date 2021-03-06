# https://pypi.python.org/pypi/ecdsa/0.10

import ecdsa
import hashlib
import struct
import unittest
import codecs
import utils
import keyUtils

# Makes a transaction from the inputs
# outputs is a list of [redemptionSatoshis, outputScript]
def makeRawTransaction(outputTransactionHash, sourceIndex, scriptSig, outputs):
    def makeOutput(data):
        redemptionSatoshis, outputScript = data
        return (codecs.encode(struct.pack("<Q", redemptionSatoshis),'hex') +
        ('%02x' % len(codecs.decode(outputScript.encode('utf-8'),'hex'))).encode('utf-8') + outputScript.encode('utf-8')).decode()
    formattedOutputs = ''.join(map(makeOutput, outputs))
    return (
        b"01000000" + # 4 bytes version
        b"01" + # varint for number of inputs
#        outputTransactionHash.decode('hex')[::-1].encode('hex') + # reverse outputTransactionHash
        codecs.encode(codecs.decode(outputTransactionHash.encode('utf-8'),'hex')[::-1],'hex') + # reverse outputTransactionHash
#        struct.pack('<L', sourceIndex).encode('hex') +
        codecs.encode(struct.pack('<L', sourceIndex),'hex') +
#        '%02x' % len(scriptSig.decode('hex')) + scriptSig +
        ('%02x' % len(codecs.decode(scriptSig.encode('utf-8'),'hex'))).encode('utf-8') + scriptSig.encode('utf-8') +
        b"ffffffff" + # sequence
        ("%02x" % len(outputs)).encode('utf-8') + # number of outputs
        formattedOutputs.encode('utf-8') +
        b"00000000" # lockTime
        )

# Returns [first, sig, pub, rest]
def parseTxn(txn):
    first = txn[0:41*2]
    scriptLen = int(txn[41*2:42*2], 16)
    script = txn[42*2:42*2+2*scriptLen]
    sigLen = int(script[0:2], 16)
    sig = script[2:2+sigLen*2]
    pubLen = int(script[2+sigLen*2:2+sigLen*2+2], 16)
    pub = script[2+sigLen*2+2:]
            
    assert(len(pub) == pubLen*2)
    rest = txn[42*2+2*scriptLen:]
    return [first, sig, pub, rest]         

# Substitutes the scriptPubKey into the transaction, appends SIGN_ALL to make the version
# of the transaction that can be signed
def getSignableTxn(parsed, compressed='no'):
    first, sig, pub, rest = parsed
    #inputAddr = utils.base58CheckDecode(keyUtils.pubKeyToAddr(pub.decode()))
    print('first: ', first, 'sig: ', sig, 'pub: ', pub, 'rest: ', rest)
    #if (compressed=='yes'):
    #    inputAddr = codecs.encode(utils.base58CheckDecode(keyUtils.pubKeyToAddr('03' +  pub[2:66],net= 'test', compressed='yes')),'hex').decode()
    #    print('pubk  ','03' +  pub[2:66] )
    #else:
    #    inputAddr = codecs.encode(utils.base58CheckDecode(keyUtils.pubKeyToAddr(pub)),'hex').decode()
    inputAddr = codecs.encode(utils.base58CheckDecode(keyUtils.pubKeyToAddr(pub)),'hex').decode()
    
    #inputAddr = codecs.encode(utils.base58CheckDecode('moyDyvi7VeAhZnGEWtvE62PoDdmoRXRRkf'),'hex').decode()
    print('pub uncompressed: ', keyUtils.pubKeyToAddr(pub,net='test'))
    print('pub   compressed: ', keyUtils.pubKeyToAddr('03' + pub[2:66],net='test'))
    print("inputAddr:", keyUtils.pubKeyToAddr('02' +pub[2:66],net= 'test'))
    print('a:', codecs.encode(utils.base58CheckDecode('1MMMMSUb1piy2ufrSguNUdFmAcvqrQF8M5'),'hex').decode())
    print('b:', codecs.encode(utils.base58CheckDecode('muwc2rRij1XuJZ5JqsevtjCvqMw9CenJfK'),'hex').decode())
    print("inputAddr:", inputAddr)
    #inputAddr = 'msZwQEA3dYTXDEUjHgfXkGSkLXpfEpLZEA'
    #print(codecs.encode(inputAddr,'hex').decode())
    #return first + "1976a914" + inputAddr.encode('hex') + "88ac" + rest + "01000000"
    return first.encode('utf-8') + b"1976a914" + inputAddr.encode('utf-8') + b"88ac" + rest.encode('utf-8') + b"01000000"
# Verifies that a transaction is properly signed, assuming the generated scriptPubKey matches
# the one in the previous transaction's output
def verifyTxnSignature(txn, compressed='no', pubk = '0'):        
    print('txn:', txn)            
    parsed = parseTxn(txn)     
    print('parsed: ', parsed) 
    compressed=compressed
    print('compressed vts:', compressed)
    signableTxn = getSignableTxn(parsed, compressed=compressed)
    print('SignableTxn:', signableTxn)
    hashToSign = hashlib.sha256(hashlib.sha256(codecs.decode(signableTxn,'hex')).digest()).digest()
    assert(parsed[1][-2:] == '01') # hashtype
    sig = keyUtils.derSigToHexSig(parsed[1][:-2])
    if (compressed=='no'):
        public_key = parsed[2]
    else:
        public_key = pubk
    print('public_key: ', public_key)
    print('sig :', sig.encode('utf-8'))
    vk = ecdsa.VerifyingKey.from_string(codecs.decode(public_key[2:].encode('utf-8'),'hex'), curve=ecdsa.SECP256k1)
    #print(vk.verify_digest(codecs.decode(sig.encode('utf-8'),'hex'), hashToSign ))
    assert(vk.verify_digest(codecs.decode(sig.encode('utf-8'),'hex'), hashToSign ))

def makeSignedTransaction( privateKey, outputTransactionHash, sourceIndex, scriptPubKey, outputs, net='main', compressed='no'):
        #Testnet
    
    myTxn_forSig = (makeRawTransaction(outputTransactionHash, sourceIndex, scriptPubKey, outputs)
         + b"01000000") # hash code
    #myTxn_forSig = codecs.decode(myTxn_forSig.encode('utf-8'),'hex')
    s256 =        hashlib.sha256(hashlib.sha256( codecs.decode(myTxn_forSig,'hex') ).digest()).digest()
    sk = ecdsa.SigningKey.from_string(codecs.decode(privateKey.encode('utf-8'),'hex'), curve=ecdsa.SECP256k1)
    sig = sk.sign_digest(s256, sigencode=ecdsa.util.sigencode_der) + b'\x01' # 01 is hashtype
    pubKey =  keyUtils.privateKeyToPublicKey(privateKey, net=net, compressed =compressed)
    pubKey2 = codecs.encode(keyUtils.privateKeyToPublicKey(privateKey, net= net,compressed ='no'),'hex').decode()
    print('pubKey : ', codecs.encode(pubKey,'hex').decode())
    print('pubKey2: ', pubKey2)
    #scriptSig = utils.varstr(sig).encode('hex') + utils.varstr(pubKey.decode('hex')).encode('hex')
    scriptSig = codecs.encode(utils.varstr(sig),'hex').decode() + codecs.encode(utils.varstr(pubKey),'hex').decode()
    signed_txn = makeRawTransaction(outputTransactionHash, sourceIndex, scriptSig, outputs)
    print('compressed mst:',compressed)
    verifyTxnSignature(signed_txn.decode(),compressed=compressed, pubk=pubKey2)
    return signed_txn.decode()
    
class TestTxnUtils(unittest.TestCase):

    def test_verifyParseTxn(self):
        txn =          ("0100000001a97830933769fe33c6155286ffae34db44c6b8783a2d8ca52ebee6414d399ec300000000" +
                        "8a47" +
                        "304402202c2e1a746c556546f2c959e92f2d0bd2678274823cc55e11628284e4a13016f80220797e716835f9dbcddb752cd0115a970a022ea6f2d8edafff6e087f928e41baac01" +
                        "41" +
                        "04392b964e911955ed50e4e368a9476bc3f9dcc134280e15636430eb91145dab739f0d68b82cf33003379d885a0b212ac95e9cddfd2d391807934d25995468bc55" +
                        "ffffffff02015f0000000000001976a914c8e90996c7c6080ee06284600c684ed904d14c5c88ac204e000000000000" +
                        "1976a914348514b329fda7bd33c7b2336cf7cd1fc9544c0588ac00000000")


        parsed = parseTxn(txn)
        self.assertEqual(parsed[0], "0100000001a97830933769fe33c6155286ffae34db44c6b8783a2d8ca52ebee6414d399ec300000000")
        self.assertEqual(parsed[1], "304402202c2e1a746c556546f2c959e92f2d0bd2678274823cc55e11628284e4a13016f80220797e716835f9dbcddb752cd0115a970a022ea6f2d8edafff6e087f928e41baac01")
        self.assertEqual(parsed[2], "04392b964e911955ed50e4e368a9476bc3f9dcc134280e15636430eb91145dab739f0d68b82cf33003379d885a0b212ac95e9cddfd2d391807934d25995468bc55")
        self.assertEqual(parsed[3], "ffffffff02015f0000000000001976a914c8e90996c7c6080ee06284600c684ed904d14c5c88ac204e000000000000" +
                        "1976a914348514b329fda7bd33c7b2336cf7cd1fc9544c0588ac00000000")

    def test_verifySignableTxn(self):
        txn =          ("0100000001a97830933769fe33c6155286ffae34db44c6b8783a2d8ca52ebee6414d399ec300000000" +
                        "8a47" +
                        "304402202c2e1a746c556546f2c959e92f2d0bd2678274823cc55e11628284e4a13016f80220797e716835f9dbcddb752cd0115a970a022ea6f2d8edafff6e087f928e41baac01" +
                        "41" +
                        "04392b964e911955ed50e4e368a9476bc3f9dcc134280e15636430eb91145dab739f0d68b82cf33003379d885a0b212ac95e9cddfd2d391807934d25995468bc55" +
                        "ffffffff02015f0000000000001976a914c8e90996c7c6080ee06284600c684ed904d14c5c88ac204e000000000000" +
                        "1976a914348514b329fda7bd33c7b2336cf7cd1fc9544c0588ac00000000")

        parsed = parseTxn(txn)      
        myTxn_forSig = ("0100000001a97830933769fe33c6155286ffae34db44c6b8783a2d8ca52ebee6414d399ec300000000" +
                        "1976a914" + "167c74f7491fe552ce9e1912810a984355b8ee07" + "88ac" +
                        "ffffffff02015f0000000000001976a914c8e90996c7c6080ee06284600c684ed904d14c5c88ac204e000000000000" +
                        "1976a914348514b329fda7bd33c7b2336cf7cd1fc9544c0588ac00000000" +
                        "01000000")
        signableTxn = getSignableTxn(parsed)
        self.assertEqual(signableTxn.decode(), myTxn_forSig)

    def test_verifyTxn(self):
        txn =          ("0100000001a97830933769fe33c6155286ffae34db44c6b8783a2d8ca52ebee6414d399ec300000000" +
                        "8a47" +
                        "304402202c2e1a746c556546f2c959e92f2d0bd2678274823cc55e11628284e4a13016f80220797e716835f9dbcddb752cd0115a970a022ea6f2d8edafff6e087f928e41baac01" +
                        "41" +
                        "04392b964e911955ed50e4e368a9476bc3f9dcc134280e15636430eb91145dab739f0d68b82cf33003379d885a0b212ac95e9cddfd2d391807934d25995468bc55" +
                        "ffffffff02015f0000000000001976a914c8e90996c7c6080ee06284600c684ed904d14c5c88ac204e000000000000" +
                        "1976a914348514b329fda7bd33c7b2336cf7cd1fc9544c0588ac00000000")

        verifyTxnSignature(txn)

    def test_makeRawTransaction(self):
        #http://bitcoin.stackexchange.com/questions/3374/how-to-redeem-a-basic-tx
        txn = makeRawTransaction(
            "f2b3eb2deb76566e7324307cd47c35eeb88413f971d88519859b1834307ecfec", # output transaction hash
            1, # sourceIndex
            "76a914010966776006953d5567439e5e39f86a0d273bee88ac", # scriptSig
            [[99900000, #satoshis
            "76a914097072524438d003d23a2f23edb65aae1bb3e46988ac"]], # outputScript
            ) + b"01000000" # hash code type
        self.assertEqual(txn,
            b"0100000001eccf7e3034189b851985d871f91384b8ee357cd47c3024736e5676eb2debb3f2" +
            b"010000001976a914010966776006953d5567439e5e39f86a0d273bee88acffffffff" +
            b"01605af405000000001976a914097072524438d003d23a2f23edb65aae1bb3e46988ac" +
            b"0000000001000000")
   
    def test_makeSignedTransaction(self): 
        # Transaction from
        # https://blockchain.info/tx/901a53e7a3ca96ed0b733c0233aad15f11b0c9e436294aa30c367bf06c3b7be8
        # From 133t to 1KKKK
        privateKey = codecs.encode(keyUtils.wifToPrivateKey("5Kb6aGpijtrb8X28GzmWtbcGZCG8jHQWFJcWugqo3MwKRvC8zyu"),'hex').decode() #133t

        signed_txn = makeSignedTransaction(privateKey,
            "c39e394d41e6be2ea58c2d3a78b8c644db34aeff865215c633fe6937933078a9", # output (prev) transaction hash
            0, # sourceIndex
            keyUtils.addrHashToScriptPubKey("133txdxQmwECTmXqAr9RWNHnzQ175jGb7e").decode(),
            [[24321, #satoshis
            keyUtils.addrHashToScriptPubKey("1KKKK6N21XKo48zWKuQKXdvSsCf95ibHFa").decode() ],
             [20000,            keyUtils.addrHashToScriptPubKey("15nhZbXnLMknZACbb3Jrf1wPCD9DWAcqd7").decode() ]]
            )

        verifyTxnSignature(signed_txn)

if __name__ == '__main__':
    unittest.main()
