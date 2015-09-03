import utils,codecs, struct,hashlib, base58,keyUtils, binascii, ecdsa








print(utils.varint(0x42)=='\x42')
x = utils.varint(0x123)
print(x)
print(codecs.encode(x,'hex'))
y = utils.varstr('abc')
z=y.decode()

print(z)



