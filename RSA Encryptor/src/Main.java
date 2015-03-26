import java.math.BigInteger;

public class Main {
	
	static BigInteger probablePrime(){
		while(true){
			BigInteger prime = Encryptor.generateRandomBigInteger();
			
			if(BigInteger.valueOf(2).modPow(prime.subtract(BigInteger.valueOf(1)), prime).compareTo(BigInteger.valueOf(1)) == 0 &&
				BigInteger.valueOf(3).modPow(prime.subtract(BigInteger.valueOf(1)), prime).compareTo(BigInteger.valueOf(1)) == 0 &&
				BigInteger.valueOf(4).modPow(prime.subtract(BigInteger.valueOf(1)), prime).compareTo(BigInteger.valueOf(1)) == 0) {
				return prime;
			}
		}	
	}
	
	public static void main(String[] args) {
		 
		BigInteger p = probablePrime();
		BigInteger q = probablePrime();
		
		System.out.println("(probable) Prime 1 is " + p);
		System.out.println("(probable) Prime 2 is " + q);

		BigInteger phi = p.subtract(BigInteger.valueOf(1)).multiply(q.subtract(BigInteger.valueOf(1)));
		
		boolean searching = true;
		BigInteger test_e = BigInteger.valueOf(1);
		while(searching){
			BigInteger candidate = Encryptor.generateRandomBigInteger(phi);
			if (Encryptor.gcd(candidate, phi).compareTo(BigInteger.valueOf(1)) == 0 ){
				test_e = candidate;
				searching = false;
			}
		}
		
		BigInteger test_d = test_e.modInverse(phi);
		Encryptor encryptor = new Encryptor(p, q, test_e, test_d);
		  
		System.out.println("Our e is " + test_e);
		System.out.println("Our d is " +test_d);

		BigInteger message = BigInteger.valueOf(27);
		System.out.println("The original message: " + message);
		BigInteger encrypted_message = encryptor.encrypt(message);
		System.out.println("The encrypted message: " + encrypted_message);
		BigInteger decrypted_message = encryptor.decrypt(encrypted_message);
		System.out.println("The decrypted message: " + decrypted_message);
	  }

}
