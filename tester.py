import utils,codecs, struct,hashlib, base58,keyUtils, binascii, ecdsa


private_key = '18E14A7B6A307F426A94F8114701E7C8E774E7F9A47E2C2035DB29A206321725'


print(utils.processAddr(b'xxxxxxxxxxxxxxxxxxxxb\x91\x98\x16 \x8d'))

#print(utils.varint(0x42))
#print(utils.processVarInt(utils.varint(0x42)))

#print(codecs.encode(keyUtils.privateKeyToPublicKey(private_key),'hex').decode())

#print(keyUtils.pubKeyToAddr(codecs.encode(keyUtils.privateKeyToPublicKey(private_key),'hex').decode()))


#print(utils.base256decode(b'abc'))
#print(utils.base256encode(utils.base256decode(b'abc')))

#print(utils.base58CheckEncode(42, b'abc'))
#print(utils.base58CheckDecode(utils.base58CheckEncode(42, b'abc')))


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



