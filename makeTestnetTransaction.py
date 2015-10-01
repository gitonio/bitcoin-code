import utils
import keyUtils
import txnUtils
import codecs
import binascii

privateKey = codecs.encode(keyUtils.wifToPrivateKey("cQFK8Vqwanamn194EscN3zUMyvPTVc39Dubx5BYccvjXjrwS9mBG"),'hex').decode() #1MMMM
privateKey = codecs.encode(keyUtils.wifToPrivateKey("92BwrjLFBNf1dUfyvSWmC6miTVQfdPSQcYrc8kAt7nFcy3JDoL8"),'hex').decode() #1MMMM
print('privateKey: ', privateKey)  #1MMMM
#F01E3C2210E1DD106399CD20D2D059412EEC856ABB3AD63E66749F24B6AA9DF
signed_txn = txnUtils.makeSignedTransaction(privateKey,
        "acf7496e7262fb977e78bd3c0692722b428bf828c8c2033caa859f8ed582f8b1", # output (prev) transaction hash
        0, # sourceIndex
        keyUtils.addrHashToScriptPubKey("muwc2rRij1XuJZ5JqsevtjCvqMw9CenJfK", net='test', compressed='yes').decode(),
        #keyUtils.addrHashToScriptPubKey("mpCWzuKvmqHSoyPo3BQzsaSSp3hqqZEfic", net='test', compressed='no').decode(), #Source of funds
        [[100000, #satoshis
        keyUtils.addrHashToScriptPubKey("n22NLZeQMATUChs2BDPrKC8RJbgHTewjm7", net='test', compressed='yes').decode()]],net='test', #Destination of funds
        #keyUtils.addrHashToScriptPubKey("mtv5Zge8zK8r3UCb1ZVC5P3JkDccJEEB21", net='test', compressed='no').decode()]],net='test',
        compressed='yes'
        )
    
#txnUtils.verifyTxnSignature(signed_txn)
print ('SIGNED TXN', signed_txn)
