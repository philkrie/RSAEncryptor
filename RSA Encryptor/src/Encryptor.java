import java.math.BigInteger;
import java.util.Random;


public class Encryptor {
	
	BigInteger p;
	BigInteger q;
	BigInteger n;
	BigInteger e;
	BigInteger d;
	
	Encryptor(BigInteger p, BigInteger q, BigInteger e, BigInteger d){
		this.p = p;
		this.q = q;
		this.n = p.multiply(q);
		this.e = e;
		this.d = d;
	}
	
	BigInteger encrypt(BigInteger message){
		return message.modPow(e, n);
	}
	
	BigInteger decrypt(BigInteger encrypted_message){
		return encrypted_message.modPow(d, n);
	}
	
	
	
	public static int gcd(int p, int q) {
		if (q == 0) return p;
		else return gcd(q, p % q);
	}
	
	public static int randInt(int min, int max) {

	    // NOTE: Usually this should be a field rather than a method
	    // variable so that it is not re-seeded every call.
	    Random rand = new Random();

	    // nextInt is normally exclusive of the top value,
	    // so add 1 to make it inclusive
	    int randomNum = rand.nextInt((max - min) + 1) + min;

	    return randomNum;
	}
}
