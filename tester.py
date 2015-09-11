import utils,codecs, struct,hashlib, base58,keyUtils, binascii, ecdsa

x=ecdsa.der.encode_sequence(
            ecdsa.der.encode_integer(0x123456),
            ecdsa.der.encode_integer(0x89abcd))

x=codecs.encode(x,'hex')
print(x)

wallet_addr = "1EyBEhrriJeghX4iqATQEWDq38Ae8ubBJe"
wallet_private = "8tnArBrrp4KHVjv8WA6HiX4ev56WDhqGA16XJCHJzhNH"
print(utils.base58decode(wallet_private))
wallet_key = utils.base256encode(utils.base58decode(wallet_private))
print(codecs.encode(wallet_key,'hex').decode())
keyUtils.keyToAddr(codecs.encode(wallet_key,'hex').decode())
bitcoin_qt = "5Jhw8B9J9QLaMmcBRfz7x8KkD9gwbNoyBMfWyANqiDwm3FFwgGC"
wallet_key = utils.base58CheckDecode(bitcoin_qt)
wallet_key = codecs.encode(wallet_key,'hex').decode()
print(wallet_key)
keyUtils.keyToAddr(wallet_key)
#private_key = '18E14A7B6A307F426A94F8114701E7C8E774E7F9A47E2C2035DB29A206321725'
 
#print(keyUtils.privateKeyToPublicKey(private_key))
#x=keyUtils.privateKeyToPublicKey(private_key)
#print(codecs.encode(x,'hex').decode())
#keyUtils.pubKeyToAddr(codecs.encode(x,'hex').decode())

#a = keyUtils.keyToAddr("18E14A7B6A307F426A94F8114701E7C8E774E7F9A47E2C2035DB29A206321725")



#print(utils.processAddr(b'xxxxxxxxxxxxxxxxxxxxb\x91\x98\x16 \x8d'))

#print(utils.varint(0x42))
#print(utils.processVarInt(utils.varint(0x42)))

#print(codecs.encode(keyUtils.privateKeyToPublicKey(private_key),'hex').decode())

#print(keyUtils.pubKeyToAddr(codecs.encode(keyUtils.privateKeyToPublicKey(private_key),'hex').decode()))


#print(utils.base256decode(b'abc'))
#print(utils.base256encode(utils.base256decode(b'abc')))

print(utils.base58CheckEncode(42, b'abc'))
print(utils.base58CheckDecode(utils.base58CheckEncode(42, b'abc')))


#print(utils.base58CheckEncode(0, b'\0\0abcd'))
#print(utils.base58CheckDecode(utils.base58CheckEncode(0, b'\0\0abcd')))

#s = utils.base256encode(0x0C28FCA386C7A227600B2FE50B7CAE11EC86D3BF1FBE471BE89827E19D72AA1D)
#print('ce', codecs.encode(s,'hex').decode())
#b = utils.base58CheckEncode(0x80, s)
#print(b)




#s = utils.base256encode(0x0C28FCA386C7A227600B2FE50B7CAE11EC86D3BF1FBE471BE89827E19D72AA1D)
#print(s)
#b = utils.base58CheckEncode(0x80, s)



#x=utils.base58CheckEncode(42,'abc')
#print('bce ',x )
#print (utils.base58decode(x))
#print (utils.base256encode(utils.base58decode(x)))
#print('bcd ', utils.base58CheckDecode(x))



