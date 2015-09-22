import utils,codecs, struct,hashlib, base58,keyUtils, binascii, ecdsa, txnUtils

keyUtils.addrHashToScriptPubKey("mwAnSj8gvAkDHbW5wTN67DRQETdmTVDdHz").decode()
keyUtils.addrHashToScriptPubKey("moRsbz4GMe99KFSzq8XsSfkS2gmPfQ3GpC").decode()
k=keyUtils.wifToPrivateKey("5J3mBbAH58CpQ3Y5RNJpUKPE62SQ5tfcvU2JpbnkeyhfsYB1Jcn")
print('privk ', codecs.encode(k,'hex').decode().upper())
print('pk', keyUtils.privateKeyToPublicKey(codecs.encode(k,'hex').decode()) )
pk = keyUtils.privateKeyToPublicKey(codecs.encode(k,'hex').decode()) 
print('pubk ',  codecs.encode(pk, 'hex').decode() )

print('addr ', keyUtils.keyToAddr("754580de93eea21579441b58e0c9b09f54f6005fc71135f5cfac027394b22caa"))


k=keyUtils.wifToPrivateKey("KzTg2wn6Z8s7ai5NA9MVX4vstHRsqP26QKJCzLg4JvFrp6mMaGB9")
print('privk ', codecs.encode(k,'hex').decode().upper())
#print('pk', keyUtils.privateKeyToPublicKey(codecs.encode(k,'hex').decode()) )
pk = keyUtils.privateKeyToPublicKey(codecs.encode(k,'hex').decode()) 
print('pubk ',  codecs.encode(pk, 'hex').decode() )

print('addr ', keyUtils.pubKeyToAddr("0328592df0ad9de33919e38caa7ff567b708699f9c2f67d8e91ff7185f1e8158b3"))


k=keyUtils.wifToPrivateKey("cQmNq39nKXu1FbTE4uCX2PfpE4Q3K3Svxf9gAZEeRWTQSZYvLrTQ")
print('privk ', codecs.encode(k,'hex').decode().upper())
#print('pk', keyUtils.privateKeyToPublicKey(codecs.encode(k,'hex').decode()) )
pk = keyUtils.privateKeyToPublicKey(codecs.encode(k,'hex').decode(),net='test') 
print('pubk ',  codecs.encode(pk, 'hex').decode() )

print('addr ', keyUtils.pubKeyToAddr("037c8c83ca259ce05554ab7dfe7c46482b9595c5a092f592d961b686a1c4768c82", net='test'))

print("abcdef",type("abcdef"))
print(                            "abcdef".encode("utf-8"),   type("abcdef".encode("utf-8")))
print(              codecs.decode("abcdef".encode("utf-8"), "hex"), )
print(              codecs.encode("abcdef".encode("utf-8"), "hex"), )
print(codecs.encode(codecs.decode("abcdef".encode("utf-8"), "hex"), "hex"))
print(codecs.encode(codecs.decode("abcdef".encode("utf-8"), "hex"), "hex").decode())
print(              codecs.decode("abcdef".encode("utf-8"), "hex") )
print(              str(codecs.decode("abcdef".encode("utf-8"), "hex") )[1:] )
print(              str(codecs.decode("abcdef".encode("utf-8"), "hex") ) )
# 
