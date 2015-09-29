import utils
import keyUtils
import txnUtils
import codecs
import binascii

privateKey = codecs.encode(keyUtils.wifToPrivateKey("cQFK8Vqwanamn194EscN3zUMyvPTVc39Dubx5BYccvjXjrwS9mBG"),'hex').decode() #1MMMM
print('privateKey: ', privateKey)  #1MMMM
#F01E3C2210E1DD106399CD20D2D059412EEC856ABB3AD63E66749F24B6AA9DF
signed_txn = txnUtils.makeSignedTransaction(privateKey,
        "7f83c6c264f5e18ab98b0a2a8f7ac941cc9646b40e7871cde1b3f4f89693dd0a", # output (prev) transaction hash
        0, # sourceIndex
        keyUtils.addrHashToScriptPubKey("muwc2rRij1XuJZ5JqsevtjCvqMw9CenJfK").decode(),
        [[100000, #satoshis
        keyUtils.addrHashToScriptPubKey("n22NLZeQMATUChs2BDPrKC8RJbgHTewjm7").decode()]]
        )
    
txnUtils.verifyTxnSignature(signed_txn)
print ('SIGNED TXN', signed_txn)
