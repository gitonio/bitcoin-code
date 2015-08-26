import random, keyUtils, codecs, hashlib, utils

#private_key = ''.join(['%x' % random.randrange(16) for x in range(0, 64)])
private_key = '0C28FCA386C7A227600B2FE50B7CAE11EC86D3BF1FBE471BE89827E19D72AA1D'
#https://en.bitcoin.it/wiki/Wallet_import_format
private_key = '0C28FCA386C7A227600B2FE50B7CAE11EC86D3BF1FBE471BE89827E19D72AA1D'
print('1 - Take a private key')
print (private_key)
print('2 - Add a 0x80 byte in front of it for mainnet addresses or 0xef for testnet addresses.')
payload = codecs.decode(private_key.encode("utf-8"),'hex')
versionb = b'\x80'
s = versionb + payload
print(codecs.encode(s, "hex").decode().upper())
print ('3 - Perform SHA-256 hash on the extended key')
first_hash = hashlib.sha256(s).hexdigest()
print (first_hash)
print(first_hash == '8147786C4D15106333BF278D71DADAF1079EF2D2440A4DDE37D747DED5403592'.lower())
print( '4 - Perform SHA-256 hash on result of SHA-256 hash')
second_hash = hashlib.sha256(codecs.decode(first_hash.encode("utf-8"), "hex")).hexdigest()
print (second_hash.upper())
print(second_hash == '507A5B8DFED0FC6FE8801743720CEDEC06AA5C6FCA72B07C49964492FB98A714'.lower())
print( '5 - Take the first 4 bytes of the second SHA-256 hash, this is the checksum')
checksum = hashlib.sha256(hashlib.sha256(s).digest()).digest()[0:4]
print (hashlib.sha256(hashlib.sha256(s).digest()).hexdigest()[0:8])
print('6 - Add the 4 checksum bytes from point 5 at the end of the extended key from point 2')
result = s + checksum
print (codecs.encode(result,'hex').decode().upper())
print (codecs.encode(result,'hex').decode()=='800C28FCA386C7A227600B2FE50B7CAE11EC86D3BF1FBE471BE89827E19D72AA1D507A5B8D'.lower())
leadingZeros = utils.countLeadingChars(result, '\0')

print('7 - Convert the result from a byte string into a base58 string using Base58Check encoding. This is the Wallet Import Format')
#print ( (utils.base256decode( str(codecs.encode(result,'hex').decode().upper())  ) ))
print(utils.base256decode( result ))

print ( utils.base58encode(utils.base256decode( result )))


print ('Wif:', keyUtils.privateKeyToWif( private_key))
#https://en.bitcoin.it/wiki/Technical_background_of_version_1_Bitcoin_addresses

print('0 - Private ECDSA Key')
private_key = '18E14A7B6A307F426A94F8114701E7C8E774E7F9A47E2C2035DB29A206321725'
print(private_key)
public_key  = keyUtils.privateKeyToPublicKey(private_key) 
print('1 - Public ECDSA Key')
print(codecs.encode(public_key,'hex').decode().upper())
print('2 - SHA-256 hash of 1')
first_hash = hashlib.sha256(public_key).hexdigest()
print (first_hash)
print('3 - RIPEMD-160 Hash of 2')
ripemd160 = hashlib.new('ripemd160')
ripemd160.update(hashlib.sha256(public_key).digest())
print(ripemd160.hexdigest())
print('4 - Adding network bytes to 3')
nb = b'\0'
s = nb + ripemd160.digest()
print(codecs.encode(s, "hex").decode().upper())
print('5 - SHA-256 hash of 4')
first_hash = hashlib.sha256(s).hexdigest()
print (first_hash)
print('6 - SHA-256 hash of 5')
second_hash = hashlib.sha256(codecs.decode(first_hash.encode("utf-8"), "hex")).hexdigest()
print (second_hash.upper())
print('7 - First four bytes of 6')
checksum = hashlib.sha256(hashlib.sha256(s).digest()).digest()[0:4]
print (hashlib.sha256(hashlib.sha256(s).digest()).hexdigest()[0:8])
print('8 - Adding 7 at the end of 4')
result = s + checksum
print (codecs.encode(result,'hex').decode().upper())
resultstr = codecs.encode(result,'hex').decode().upper()


print('9 - Base58 encoding of 8')
leadingZeros = utils.countLeadingChars(result, 0)
print (  '1' * leadingZeros + utils.base58encode(utils.base256decode( result )))
print ('Addr: ' , keyUtils.keyToAddr(private_key))

print (keyUtils.keyToAddr(private_key))


#Wif to private key
wif = '5HueCGU8rMjxEXxiPuD5BDku4MkFqeZyd4dZ1jvhTVqvbTLvyTJ'
print('1 - Take a Wallet Import Format string')
print(wif)
print('2 - Convert it to a byte string using Base58Check encoding')
leadingOnes = utils.countLeadingChars(s, '1')
s = utils.base256encode(utils.base58decode(wif))
#print(s)
print(s.encode(encoding='utf-8'))
result = '\0' * leadingOnes + s[:-4]
chk = s[-4:]
checksum = hashlib.sha256(hashlib.sha256(result.encode('utf-8')).digest()).hexdigest()[0:4]
print(checksum)
#assert(chk == checksum)
version = result[0]
print(result[1:].encode())
#print(keyUtils.wifToPrivateKey(wif))