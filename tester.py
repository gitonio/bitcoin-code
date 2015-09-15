import utils,codecs, struct,hashlib, base58,keyUtils, binascii, ecdsa, txnUtils

payload = ('\x71\x11\x01\x00\x01\x00\x00\x00' +
'\x00\x00\x00\x00\xa2\x31\xa0\x52\x00\x00\x00\x00\x01\x00\x00\x00' +
'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xff' +
'\x6c\x51\xe0\xee\xd8\x73\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00' +
'\x00\x00\x00\x00\x00\x00\x00\x00\xff\xff\x62\x91\x98\x16\x20\x8d' +
'\xf4\x7d\x37\xbf\xe4\xe7\x1f\xd2\x11\x2f\x53\x61\x74\x6f\x73\x68' +
'\x69\x3a\x30\x2e\x38\x2e\x32\x2e\x32\x2f\x02\x2b\x04\x00')
print(payload)
print( codecs.encode(keyUtils.wifToPrivateKey("5Kb6aGpijtrb8X28GzmWtbcGZCG8jHQWFJcWugqo3MwKRvC8zyu"),'hex').decode())
print( keyUtils.addrHashToScriptPubKey("15nhZbXnLMknZACbb3Jrf1wPCD9DWAcqd7").decode() )
print( codecs.encode(keyUtils.addrHashToScriptPubKey("15nhZbXnLMknZACbb3Jrf1wPCD9DWAcqd7"),'hex').decode() )


txn = txnUtils.makeRawTransaction(
"f2b3eb2deb76566e7324307cd47c35eeb88413f971d88519859b1834307ecfec", # output transaction hash
1, # sourceIndex
"76a914010966776006953d5567439e5e39f86a0d273bee88ac", # scriptSig
[[99900000, #satoshis
"76a914097072524438d003d23a2f23edb65aae1bb3e46988ac"]], # outputScript
) + b"01000000" # hash code type

print(txn.decode())
print(txn.decode()==            "0100000001eccf7e3034189b851985d871f91384b8ee357cd47c3024736e5676eb2debb3f2" +
            "010000001976a914010966776006953d5567439e5e39f86a0d273bee88acffffffff" +
            "01605af405000000001976a914097072524438d003d23a2f23edb65aae1bb3e46988ac" +
            "0000000001000000"
)



derSig = "304502204c01fee2d724fb2e34930c658f585d49be2f6ac87c126506c0179e6977716093022100faad0afd3ae536cfe11f83afaba9a8914fc0e70d4c6d1495333b2fb3df6e8cae"
"4c01fee2d724fb2e34930c658f585d49be2f6ac87c126506c0179e6977716093faad0afd3ae536cfe11f83afaba9a8914fc0e70d4c6d1495333b2fb3df6e8cae"== keyUtils.derSigToHexSig(derSig)
   
txn =  ("0100000001a97830933769fe33c6155286ffae34db44c6b8783a2d8ca52ebee6414d399ec300000000" +
"8a47" +
"304402202c2e1a746c556546f2c959e92f2d0bd2678274823cc55e11628284e4a13016f80220797e716835f9dbcddb752cd0115a970a022ea6f2d8edafff6e087f928e41baac01" +
"41" +
"04392b964e911955ed50e4e368a9476bc3f9dcc134280e15636430eb91145dab739f0d68b82cf33003379d885a0b212ac95e9cddfd2d391807934d25995468bc55" +
"ffffffff02015f0000000000001976a914c8e90996c7c6080ee06284600c684ed904d14c5c88ac204e000000000000" +
"1976a914348514b329fda7bd33c7b2336cf7cd1fc9544c0588ac00000000")
myTxn_forSig = ("0100000001a97830933769fe33c6155286ffae34db44c6b8783a2d8ca52ebee6414d399ec300000000" +
"1976a914" + "167c74f7491fe552ce9e1912810a984355b8ee07" + "88ac" +
"ffffffff02015f0000000000001976a914c8e90996c7c6080ee06284600c684ed904d14c5c88ac204e000000000000" +
"1976a914348514b329fda7bd33c7b2336cf7cd1fc9544c0588ac00000000" +
"01000000")
public_key =    "04392b964e911955ed50e4e368a9476bc3f9dcc134280e15636430eb91145dab739f0d68b82cf33003379d885a0b212ac95e9cddfd2d391807934d25995468bc55"

hashToSign = hashlib.sha256(hashlib.sha256(codecs.decode(myTxn_forSig.encode('utf-8'),'hex')).digest()).digest()
print(hashlib.sha256(hashlib.sha256(codecs.decode(myTxn_forSig.encode('utf-8'),'hex')).digest()).hexdigest())
sig_der =       "304402202c2e1a746c556546f2c959e92f2d0bd2678274823cc55e11628284e4a13016f80220797e716835f9dbcddb752cd0115a970a022ea6f2d8edafff6e087f928e41baac01"[:-2]
sig = keyUtils.derSigToHexSig(sig_der)
print(sig)
vk = ecdsa.VerifyingKey.from_string(codecs.decode(public_key[2:].encode('utf-8'),'hex'), curve=ecdsa.SECP256k1)
print(vk)

print(vk.verify_digest(codecs.decode(sig.encode('utf-8'),'hex'), hashToSign))



