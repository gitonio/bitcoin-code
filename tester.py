import utils,codecs, struct,hashlib, base58,keyUtils, binascii
# print("abcdef",type("abcdef"))
# print(                            "abcdef".encode("utf-8"),   type("abcdef".encode("utf-8")))
# print(              codecs.decode("abcdef".encode("utf-8"), "hex"), )
# print(codecs.encode(codecs.decode("abcdef".encode("utf-8"), "hex"), "hex"))
# print(codecs.encode(codecs.decode("abcdef".encode("utf-8"), "hex"), "hex").decode())
# print(              codecs.decode("abcdef".encode("utf-8"), "hex") )
# print(              str(codecs.decode("abcdef".encode("utf-8"), "hex") )[1:] )
# print(              str(codecs.decode("abcdef".encode("utf-8"), "hex") ) )
# 

print(utils.base256encode(0x4142))
print(type(utils.base256encode(0x4142)))
print(utils.base256decode(b'AB'))
print(utils.base256encode(16706))
print('abc:', utils.base58CheckEncode(42, 'AB'))
#print('abc:', utils.base58CheckEncode(42, utils.base256encode(0x4142)))
#print('AB:', utils.base58CheckEncode(0, 'AB'))
# print(utils.base58CheckDecode(utils.base58CheckEncode(42, 'abc')))
# print(utils.base58CheckEncode( 0, '\0\0abc'))
# print(utils.base58CheckDecode(utils.base58CheckEncode(0, '\0\0abc')))
hexstring = '800C28FCA386C7A227600B2FE50B7CAE11EC86D3BF1FBE471BE89827E19D72AA1D507A5B8D'
private_key = '0C28FCA386C7A227600B2FE50B7CAE11EC86D3BF1FBE471BE89827E19D72AA1D'
s = utils.base256encode(0x0C28FCA386C7A227600B2FE50B7CAE11EC86D3BF1FBE471BE89827E19D72AA1D)
s = utils.base256encode(0x0C28FCA386C7A227600B2FE50B7CAE11EC86D3BF1FBE471BE89827E19D72AA1D)
# print(s.encode('utf-8'))
# #print(s)
b = utils.base58CheckEncode(0x80, private_key)
print('b:',b)
#b = utils.base58CheckEncode(0x80, s)
print('b:',b)
print ('Wif:', keyUtils.privateKeyToWif( private_key))
# print(utils.base58CheckEncode(0x80, "\x0c(\xc3\xbc\xc2\xa3\xc2\x86\xc3\x87\xc2\xa2'`\x0b/\xc3\xa5\x0b|\xc2\xae\x11\xc3\xac\xc2\x86\xc3\x93\xc2\xbf\x1f\xc2\xbeG\x1b\xc3\xa8\xc2\x98'\xc3\xa1\xc2\x9dr\xc2\xaa\x1d"))

print('hex_string', hexstring)
unencoded_string = bytes.fromhex(hexstring)
print('unencoded_string',unencoded_string)
print(len(unencoded_string))
print(binascii.hexlify(unencoded_string).decode())
encoded_string= base58.b58encode(unencoded_string)
print('Encoded String:',encoded_string)
wif = '5HueCGU8rMjxEXxiPuD5BDku4MkFqeZyd4dZ1jvhTVqvbTLvyTJ'
encoded_string= base58.b58decode(wif,37)
print(len(encoded_string))
print((binascii.hexlify(encoded_string).decode()))
print(type(encoded_string))

x = '800C28FCA386C7A227600B2FE50B7CAE11EC86D3BF1FBE471BE89827E19D72AA1D507A5B8D'
print(codecs.decode(x.encode(), 'hex'))
y = codecs.decode(x.encode(), 'hex')
print ( utils.base58encode(utils.base256decode( y )))

x = '5HueCGU8rMjxEXxiPuD5BDku4MkFqeZyd4dZ1jvhTVqvbTLvyTJ'
i = utils.base58decode( x )
print(i)
#print(utils.base58encode(i))
#y = codecs.decode(x.encode(), 'hex')
z=utils.base256encode(i)
print(z)
print((binascii.hexlify(z).decode()))







