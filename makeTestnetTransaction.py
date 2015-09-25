import utils
import keyUtils
import txnUtils
import codecs
import binascii

privateKey = codecs.encode(keyUtils.wifToPrivateKey("cMeNhXd7qUrAc9LpkCDfXpziQczdVrRdMVsauNTDhU1c4K5cptNk"),'hex').decode() #1MMMM
print('privateKey: ', privateKey)  #1MMMM
#F01E3C2210E1DD106399CD20D2D059412EEC856ABB3AD63E66749F24B6AA9DF
signed_txn = txnUtils.makeSignedTransaction(privateKey,
        "11e4de28d2254beed8f809cb2d97d218f1b0f78a7fec16dccc7c5c70359cdf14", # output (prev) transaction hash
        0, # sourceIndex
        keyUtils.addrHashToScriptPubKey("moyDyvi7VeAhZnGEWtvE62PoDdmoRXRRkf").decode(),
        [[100, #satoshis
        keyUtils.addrHashToScriptPubKey("mnS3yENBc3zpj35UAS8SHNACjdkD9YE2YP").decode()]]
        )
    
txnUtils.verifyTxnSignature(signed_txn)
print ('SIGNED TXN', signed_txn)
