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
    
def euclid(x,y):
    #returns a,b, and d such that gcd(x,y)=d=ax+by.
    return 0,0,gcd(x,y) #one out of three... 

def inverse(g,n):
    #returns h so that g*h=1 mod n
    #first check that g is an element of the multiplicative group
    if gcd(g,n)!=1: print "ERROR!"
    a,b,d=euclid(g,n)
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

genkey()
