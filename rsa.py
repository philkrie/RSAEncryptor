import random
#there are more secure random number generating modules one should use in practice.

def modpow(b,p,n):
	digits = bin(p)[::-1]
	r=1
	for d in digits:
		if d=='b': return r
		if d=='1':
			r=r*b % n
		b=b**2 % n


def randomprime(n):
	#returns a random prime less than n
	if n<20: return "ERROR"
	while 1>0:
		guess=random.randint(3,n)
		if {modpow(k,guess-1,guess) for k in [2,3,5,7,11,13,17,19]}=={1L}:
			return guess
			break

    
def gcd(x,y):
    if y==0:
        return x
    else:
        return gcd(y,x % y)


def ext_euclid(a,b):
	#returns a,b, and d such that gcd(x,y)=d=ax+by.
	#From Dasgupta's Algorithms book
	if b==0:
		return 1,0,a
	x,y,d=ext_euclid(b,a-b*(a/b))
	return y, x-(a/b)*y,d


def inverse(g,n):
    #returns h so that g*h=1 mod n
    #first check that g is an element of the multiplicative group
    if gcd(g,n)!=1: print "ERROR!"
    a,b,d=ext_euclid(g,n)
    #so ag+bn = 1, which means ag = 1 (mod n).
    return a % n

def genkey(n):
    p=randomprime(2**n)
    q=randomprime(2**n)
    n=p*q
    phi=(p-1)*(q-1)
    e=2**16+1
    d=inverse(e,phi)
    print "Public:\t n =",n,"\n\t e =",e,"\n"
    print "Private: d =",d
    # print " because p =",p,"\n and \t q =",q,".\n"
    # print "testing..."
    # test=modpow(modpow(2,e,n),d,n)
    # print "(2^e)^d = ",test
    return n,e,d

def concat(a):
	#just slams a bunch of strings in an array together
	s=""
	for x in a:
		s=s+x
	return s

def chunk(s):
	# given a string, returns an array of 48-digit numbers
	# (means genkey's n should have at least 48 digits.)
	chars=[s[i] for i in range(len(s))]
	numb=[str(ord(c)) for c in chars]
	pad=['0'*(3-len(dig))+dig for dig in numb]
	chunks=[int(concat([pad[j] for j in range(16*i,16*(i+1))])) for i in range(len(pad)/16)]
	if len(pad)%16!=0:
		chunks=chunks+[int(concat([pad[j] for j in range(16*(len(pad)/16),len(pad))]))]
	return chunks

def unchunk(a):
	#converts an array of 3n-digit numbers into a string
	s=""
	for chunk in a:
		nibble=str(chunk)
		while (len(nibble)%3)!=0:nibble='0'+nibble  #adding lead zeroes as needed
		for i in range(len(nibble)/3):
			s=s+chr(int(nibble[3*i:3*(i+1)]))
	return s


def encrypt(string,e,n):
	vanilla=chunk(string)
	swirl=[modpow(v,e,n) for v in vanilla]
	return swirl
	
def decrypt(a,d,n):
	vanilla=[modpow(x,d,n) for x in a]
	return unchunk(vanilla)

# --------------------------------------

print "Probable-primes:"
for i in range(2,30):
	print randomprime(10**i)

s=" Mind at its perfect play is like some bat \n That beats about in caverns all alone,\n Contriving by a kind of senseless wit \n Not to conclude against a wall of stone. \n\n It has no need to falter or explore; \n Darkly it knows what obstacles are there, \n And so may weave and flitter, dip and soar \n In perfect courses through the blackest air.\n \n And has this simile a like perfection? \n The mind is like a bat. Precisely. Save\n That in the very happiest intellection \n A graceful error may correct the cave.\n"

print
print "key:"
n,e,d = genkey(100)
print
print "plaintext: \n",s,"\n"
a=encrypt(s,e,n)
print "encrypted: \n",a,"\n"
print "decrypted: \n",decrypt(a,d,n)
