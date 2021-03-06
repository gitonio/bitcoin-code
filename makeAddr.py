import random, keyUtils, codecs, hashlib, utils, binascii





print('****************************************')
print('***** WIF to Private key ***************')
print('****************************************')

#net = 'main'
#compressed='no'
#wif = '5HueCGU8rMjxEXxiPuD5BDku4MkFqeZyd4dZ1jvhTVqvbTLvyTJ'

net = 'test'
compressed='yes'
wif = "cQFK8Vqwanamn194EscN3zUMyvPTVc39Dubx5BYccvjXjrwS9mBG"

#net = 'test'
#compressed='yes'
#wif = "cR7UGQyRRJxnXUm3wLrUNWpi4mrRLB6vUQ797KYQrx5UUvPp473y"

#Antonopolous
#compressed='yes'
#wif = "KyBsPXxTuVD82av65KZkrGrWi5qLMah5SdNq6uftawDbgKa2wv6S"
#net = 'main'

#compressed='no'
#wif = "5JG9hT3beGTJuUAmCQEmNaxAuMacCTfXuw1R3FCXig23RQHMr4K"
print('1 - Take a Wallet Import Format string')
print('   ',wif)
print('2 - Convert it to a byte string using Base58Check encoding')
leadingOnes = utils.countLeadingChars(wif, '1')
s = utils.base256encode(utils.base58decode(wif))
#print(codecs.decode( s[:-4], 'hex' ).decode())

result = '\0' * leadingOnes + binascii.hexlify( s[:-4] ).decode()
print('   ',result.upper())
print('3 - Drop the last 4 checksum bytes from the byte string')
print('   ',result[:-4].upper())
chk = s[-4:]
checksum = hashlib.sha256(hashlib.sha256(result.encode('utf-8')).digest()).hexdigest()[0:8]
print('4 - Dropping first byte. This is the private key')
private_key = result[1:-4].upper()
print('   ',result[1:-4].upper())
private_key = codecs.encode(keyUtils.wifToPrivateKey(wif),'hex').decode()
print('   ',codecs.encode(keyUtils.wifToPrivateKey(wif),'hex').decode())
print('   ',codecs.encode(keyUtils.wifToPrivateKey(wif),'hex'))

print('****************************************')
print('***** WIF checksum       ***************')
print('****************************************')
#wif = '5HueCGU8rMjxEXxiPuD5BDku4MkFqeZyd4dZ1jvhTVqvbTLvyTJ'
#wif = "cMeNhXd7qUrAc9LpkCDfXpziQczdVrRdMVsauNTDhU1c4K5cptNk"
print('1 - Take a Wallet Import Format string')
print('   ',wif)
print('2 - Convert it to a byte string using Base58Check encoding')
leadingOnes = utils.countLeadingChars(s, '1')
s = utils.base256encode(utils.base58decode(wif))
result = '\0' * leadingOnes + binascii.hexlify( s ).decode()
print('   ',result.upper())
print('3 - Drop the last 4 checksum bytes from the byte string')
print('   ',result[:-8].upper())
chk = s[-4:]
checksum = hashlib.sha256(hashlib.sha256(result.encode('utf-8')).digest()).hexdigest()[0:8]
print('3 - Perform SHA-256 hash on the shortened string')
first_hash = hashlib.sha256(codecs.decode( result[:-8].encode('utf-8') ,'hex')).digest()
print('   ',hashlib.sha256(   codecs.decode( result[:-8].encode('utf-8') ,'hex')      ).hexdigest())
print('4 - Perform SHA-256 hash on result of SHA-256 hash')
second_hash = hashlib.sha256(first_hash).digest()
print('   ', hashlib.sha256(first_hash).hexdigest())
print('5 - Take the first 4 bytes of the second SHA-256 hash, this is the checksum')
chk = second_hash[:4]
print('   ',binascii.hexlify( chk ).decode())
#print(codecs.decode(chk,'hex').decode())
print('6 - Make sure it is the same, as the last 4 bytes from point 2')
print('   ', result[-8:])
print('7 - If they are, and the byte string from point 2 starts with 0x80 (0xef for testnet addresses), then there is no error.')

#http://gobittest.appspot.com/
#https://en.bitcoin.it/wiki/Wallet_import_format
#http://kunststube.net/encoding/
#private_key = ''.join(['%x' % random.randrange(16) for x in range(0, 64)]) 
#private_key = '0C28FCA386C7A227600B2FE50B7CAE11EC86D3BF1FBE471BE89827E19D72AA1D'
#private_key = '01E3C2210E1DD106399CD20D2D059412EEC856ABB3AD63E66749F24B6AA9DF'
print('****************************************')
print('***** Private key to WIF ***************')
print('****************************************')
print('1 - Take a private key')
print ('   ',private_key)
print('2 - Add a 0x80 byte in front of it for mainnet addresses or 0xef for testnet addresses.')
payload = codecs.decode(private_key.encode("utf-8"),'hex')
if (net == 'main'):
    versionb = b'\x80'
else:
    versionb = b'\xef'
s = versionb + payload
print('   ', codecs.encode(s, "hex").decode().upper())
print ('3 - Perform SHA-256 hash on the extended key')
first_hash = hashlib.sha256(s).hexdigest()
print ('   ',first_hash)
print('   ',first_hash == '8147786C4D15106333BF278D71DADAF1079EF2D2440A4DDE37D747DED5403592'.lower())
print( '4 - Perform SHA-256 hash on result of SHA-256 hash')
second_hash = hashlib.sha256(codecs.decode(first_hash.encode("utf-8"), "hex")).hexdigest()
print ('   ',second_hash.upper())
print('   ',second_hash == '507A5B8DFED0FC6FE8801743720CEDEC06AA5C6FCA72B07C49964492FB98A714'.lower())
print( '5 - Take the first 4 bytes of the second SHA-256 hash, this is the checksum')
checksum = hashlib.sha256(hashlib.sha256(s).digest()).digest()[0:4]
print ('   ',hashlib.sha256(hashlib.sha256(s).digest()).hexdigest()[0:8])
print('6 - Add the 4 checksum bytes from point 5 at the end of the extended key from point 2')
result = s + checksum
print ('   ',codecs.encode(result,'hex').decode().upper())
print ('   ',codecs.encode(result,'hex').decode()=='800C28FCA386C7A227600B2FE50B7CAE11EC86D3BF1FBE471BE89827E19D72AA1D507A5B8D'.lower())
leadingZeros = utils.countLeadingChars(result, '\0')

print('7 - Convert the result from a byte string into a base58 string using Base58Check encoding. This is the Wallet Import Format')
#print(utils.base256decode( result ))
print ('    WIF:', utils.base58encode(utils.base256decode( result )))
print ('    WIF:', keyUtils.privateKeyToWif( private_key , net=net, compressed='yes'))
print ('    WIF:', keyUtils.privateKeyToWif( private_key , net=net, compressed='no'))


#https://en.bitcoin.it/wiki/Technical_background_of_version_1_Bitcoin_addresses
print('****************************************')
print('***** Private key to Bitcoin Address ***')
print('****************************************')

print('0 - Private ECDSA Key')
#private_key = '18E14A7B6A307F426A94F8114701E7C8E774E7F9A47E2C2035DB29A206321725'
#private_key = '1E99423A4ED27608A15A2616A2B0E9E52CED330AC530EDCC32C8FFC6A526AEDD'
print('   ',private_key)
public_key  = keyUtils.privateKeyToPublicKey(private_key, net = net) 
print('1 - Public ECDSA Key')
print('   ',codecs.encode(public_key,'hex').decode().upper())
print('2 - SHA-256 hash of 1')
first_hash = hashlib.sha256(public_key).hexdigest()
print ('   ',first_hash)
print('3 - RIPEMD-160 Hash of 2')
ripemd160 = hashlib.new('ripemd160')
ripemd160.update(hashlib.sha256(public_key).digest())
print('   ',ripemd160.hexdigest())
print('4 - Adding network bytes to 3')
if (net == 'main'):
    nb = b'\0'
else:
    nb = b'o'
    nb = bytes(((111,)))
s = nb + ripemd160.digest()
print('   ',codecs.encode(s, "hex").decode().upper())
print('5 - SHA-256 hash of 4')
first_hash = hashlib.sha256(s).hexdigest()
print ('   ',first_hash)
print('6 - SHA-256 hash of 5')
second_hash = hashlib.sha256(codecs.decode(first_hash.encode("utf-8"), "hex")).hexdigest()
print ('   ',second_hash.upper())
print('7 - First four bytes of 6')
checksum = hashlib.sha256(hashlib.sha256(s).digest()).digest()[0:4]
print ('   ',hashlib.sha256(hashlib.sha256(s).digest()).hexdigest()[0:8])
print('8 - Adding 7 at the end of 4')
result =  s + checksum
print ('   ',codecs.encode(result,'hex').decode().upper())
resultstr = codecs.encode(result,'hex').decode().upper()


print('9 - Base58 encoding of 8')
leadingZeros = utils.countLeadingChars(result, 0)
print ( '   ', '1' * leadingZeros + utils.base58encode(utils.base256decode( result )))
print ('   Addr: ' , keyUtils.pubKeyToAddr(codecs.encode(keyUtils.privateKeyToPublicKey(private_key, net = net, compressed=compressed),'hex').decode(), net = net,compressed=compressed))
print ('   Addr: ' , keyUtils.pubKeyToAddr(codecs.encode(keyUtils.privateKeyToPublicKey(private_key, net = net, compressed='yes'),'hex').decode(), net = net, compressed='yes'))
print ('   Addr: ' , keyUtils.pubKeyToAddr(codecs.encode(keyUtils.privateKeyToPublicKey(private_key, net = net, compressed='no'),'hex').decode(), net = net, compressed='no'))
print ('   Addr: ' , keyUtils.pubKeyToAddr("025c0de3b9c8ab18dd04e3511243ec2952002dbfadc864b9628910169d9b9b00ec", net = net, compressed='yes'))
print('pubk ',codecs.encode(keyUtils.privateKeyToPublicKey(private_key, net = net, compressed='yes'),'hex').decode())