from hashlib import md5

def is_valid_password(s):
    hash = md5(p)
    digest = hash.digest()
    if digest[0]==0 and digest[1]==0 and digest[2]>>4==0:
        return hash.hexdigest()


x = b'reyedfim'
idx = 0
pwd = ''
while len(pwd) < 8:
    p = b'%s%d' % (x, idx)
    hash = is_valid_password(p)
    if hash:
        pwd += hash[5]
        print(p, hash, pwd)
    idx += 1

print('The real answer is %s' % pwd)
print('The answer must be f97c354d')
