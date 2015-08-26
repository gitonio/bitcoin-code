import utils,codecs, struct,hashlib
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
print('abc:', utils.base58CheckEncode(42, 'abc'))
print(utils.base58CheckDecode(utils.base58CheckEncode(42, 'abc')))
print(utils.base58CheckEncode( 0, '\0\0abc'))
print(utils.base58CheckDecode(utils.base58CheckEncode(0, '\0\0abc')))
s = utils.base256encode(0x0C28FCA386C7A227600B2FE50B7CAE11EC86D3BF1FBE471BE89827E19D72AA1D)
print(s.encode('utf-8'))
#print(s)
b = utils.base58CheckEncode(0x80, s)
print(b)
print(utils.base58CheckEncode(0x80, "\x0c(\xc3\xbc\xc2\xa3\xc2\x86\xc3\x87\xc2\xa2'`\x0b/\xc3\xa5\x0b|\xc2\xae\x11\xc3\xac\xc2\x86\xc3\x93\xc2\xbf\x1f\xc2\xbeG\x1b\xc3\xa8\xc2\x98'\xc3\xa1\xc2\x9dr\xc2\xaa\x1d"))

