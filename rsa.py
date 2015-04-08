def randomprime():
    return 8675309
    #xkcd.com/221/
    
def gcd(x,y):
    if y==0:
        return x
    else:
        return gcd(y,x % y)

def exp(b,p,n):
    #returns b to the p mod n. Needs to be made much more efficient.
    return (b**p)%n
    
def ext_euclid(x,y):
    #returns a,b, and d such that gcd(x,y)=d=ax+by.
    return 0,0,gcd(x,y) #one out of three... 

def inverse(g,n):
    #returns h so that g*h=1 mod n
    #first check that g is an element of the multiplicative group
    if gcd(g,n)!=1: print "ERROR!"
    a,b,d=ext_euclid(g,n)
    #so ag+bn=1, which means ag=1 mod n.
    return a

def genkey():
    p=randomprime()
    q=randomprime()
    p=11 #delete once randomprime actually works
    q=7  #delete once randomprime actually works
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
a=chunk(s)
print a,"\n"
t=unchunk(a)	
print s
print t	

	
# genkey()
