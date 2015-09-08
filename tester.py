import utils,codecs, struct,hashlib, base58,keyUtils, binascii, ecdsa


private_key = '18E14A7B6A307F426A94F8114701E7C8E774E7F9A47E2C2035DB29A206321725'

print(codecs.encode(keyUtils.privateKeyToPublicKey(private_key),'hex').decode())

version = 42
payload = 'abc'
s = chr(version) + payload
print ('s: ' , s)

s.encode('utf-8')

print(utils.base58CheckEncode(42,'abc'))
print(utils.base58CheckDecode(utils.base58CheckEncode(42,'abc')))

print(utils.varint(0x42)=='\x42')
x = utils.varint(0x123)
print(x)
print(codecs.encode(x,'hex'))
y = utils.varstr('abc')
z=y.decode()

print(z)



