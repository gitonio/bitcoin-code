import utils
import keyUtils
import txnUtils
import codecs
import binascii

privateKey = keyUtils.wifToPrivateKey("5HusYj2b2x4nroApgfvaSfKYZhRbKFH41bVyPooymbC6KfgSXdD") #1MMMM

#print(codecs.decode('0caecf01d74102a28aed6a64dcf1cf7b0e41c4dd6c62f70f46febdc32514f0bd'.encode('utf-8'),'hex'))

utils.base58CheckDecode('1MMMMSUb1piy2ufrSguNUdFmAcvqrQF8M5')
#print(type(utils.base58CheckDecode('1MMMMSUb1piy2ufrSguNUdFmAcvqrQF8M5'))) 
#print(binascii.unhexlify((utils.base58CheckDecode('1MMMMSUb1piy2ufrSguNUdFmAcvqrQF8M5')))) 
#print(codecs.decode(utils.base58CheckDecode('1MMMMSUb1piy2ufrSguNUdFmAcvqrQF8M5'),'hex'))
#print('k u    ', keyUtils.addrHashToScriptPubKey("1MMMMSUb1piy2ufrSguNUdFmAcvqrQF8M5"))



keyUtils.addrHashToScriptPubKey("1MMMMSUb1piy2ufrSguNUdFmAcvqrQF8M5")
keyUtils.addrHashToScriptPubKey("1KKKK6N21XKo48zWKuQKXdvSsCf95ibHFa")

codecs.decode('0caecf01d74102a28aed6a64dcf1cf7b0e41c4dd6c62f70f46febdc32514f0bd'.encode('utf-8'),'hex')



signed_txn = txnUtils.makeSignedTransaction(privateKey,
        "81b4c832d70cb56ff957589752eb4125a4cab78a25a8fc52d6a09e5bd4404d48", # output (prev) transaction hash
        0, # sourceIndex
        keyUtils.addrHashToScriptPubKey("1MMMMSUb1piy2ufrSguNUdFmAcvqrQF8M5"),
        [[91234, #satoshis
        keyUtils.addrHashToScriptPubKey("1KKKK6N21XKo48zWKuQKXdvSsCf95ibHFa")]]
        )
    
txnUtils.verifyTxnSignature(signed_txn)
print ('SIGNED TXN', signed_txn)




