import random
#there are more secure random number generating modules one should use in practice.

def exp(b,p,n):
	#bin=p in binary
	#for d in digits(bin) (right to left)
		#if d==1 then
			# r=r*s % n
		#s=s^2 %n
	# return r
    return (b**p)%n


def randomprime(n):
	#returns a random prime less than n
	if n<10: return "ERROR"
	while 1>0:
		guess=random.randint(3,n)
		if {exp(k,guess-1,guess) for k in [2,3,5,7]}=={1L}:
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

def concat(a):
	#just slams a bunch of strings in an array together
	s=""
	for x in a:
		s=s+x
	return s

def chunk(s):
	#given a string, returns an array of 48-digit numbers
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

s="This is some text that I'm chunking then unchunking."
print s,"\n"
a=chunk(s)
print a,"\n"
t=unchunk(a)	
print t,"\n"

# print randomprime(10)
print randomprime(100)
print randomprime(1000)
print randomprime(10000)
print randomprime(100000)
print randomprime(1000000)
# print randomprime(10000000)
# print randomprime(100000000)

print	
genkey(10)
