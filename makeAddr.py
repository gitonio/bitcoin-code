import random, keyUtils

#private_key = ''.join(['%x' % random.randrange(16) for x in range(0, 64)])
private_key = '0C28FCA386C7A227600B2FE50B7CAE11EC86D3BF1FBE471BE89827E19D72AA1D'
print (keyUtils.privateKeyToWif(private_key))
print (keyUtils.keyToAddr(private_key))

