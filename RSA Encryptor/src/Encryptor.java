import java.math.BigInteger;
import java.util.Random;


public class Encryptor {
	
	BigInteger p;
	BigInteger q;
	BigInteger n;
	BigInteger e;
	BigInteger d;
	BigInteger[] encrypted;
	
	Encryptor(BigInteger p, BigInteger q, BigInteger e, BigInteger d){
		this.p = p;
		this.q = q;
		this.n = p.multiply(q);
		this.e = e;
		this.d = d;
	}
	
	BigInteger[] encrypt(String message){
		encrypted = new BigInteger[message.length()];
		for (int i = 0; i < message.length(); i++){
			encrypted[i] = BigInteger.valueOf((int) message.charAt(i)).modPow(e, n);
		}
		return encrypted;
	}
	
	String decrypt(BigInteger[] encrypted_message){
		char [] decryption = new char[encrypted_message.length];
		for (int i = 0; i < encrypted_message.length; i++){
			decryption[i] = (char) encrypted_message[i].modPow(d, n).intValue();
		}
		
		return new String(decryption);
	}
	
	public static BigInteger gcd(BigInteger p, BigInteger q) {
		if (q == BigInteger.valueOf(0)) return p;
		else return gcd(q, p.mod(q));
	}
	
	public static BigInteger generateRandomBigInteger() {
		Random rnd = new Random();
		BigInteger r = new BigInteger(512, rnd);
		return r;
	}
	
	public static BigInteger generateRandomBigInteger(BigInteger max){
		Random rnd = new Random();
		BigInteger r;
		do {
		    r = new BigInteger(max.bitLength(), rnd);
		} while (r.compareTo(max) >= 0);
		
		return r;
		
	}
}
