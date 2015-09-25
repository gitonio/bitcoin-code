import utils
import keyUtils
import txnUtils
import codecs
import binascii

privateKey = codecs.encode(keyUtils.wifToPrivateKey("cRYshQHwhbBfaQYRmcpJubbV3SMwVAif6cwger7BgwmtWLThW5xz"),'hex').decode() #1MMMM
print('privateKey: ', privateKey)  #1MMMM
#F01E3C2210E1DD106399CD20D2D059412EEC856ABB3AD63E66749F24B6AA9DF
signed_txn = txnUtils.makeSignedTransaction(privateKey,
        "7f83c6c264f5e18ab98b0a2a8f7ac941cc9646b40e7871cde1b3f4f89693dd0a", # output (prev) transaction hash
        0, # sourceIndex
        keyUtils.addrHashToScriptPubKey("msxdJgRxcSvxc2T71NqneypFcK5orhDrn9").decode(),
        [[100000, #satoshis
        keyUtils.addrHashToScriptPubKey("mnS3yENBc3zpj35UAS8SHNACjdkD9YE2YP").decode()]]
        )
    
txnUtils.verifyTxnSignature(signed_txn)
print ('SIGNED TXN', signed_txn)
