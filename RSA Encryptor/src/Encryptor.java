import java.math.BigInteger;
import java.util.Random;


public class Encryptor {
	
	BigInteger p;
	BigInteger q;
	BigInteger n;
	BigInteger e;
	BigInteger d;
	BigInteger[] encrypted;
	String[] chunks;
	String[] outputArray;
	
	Encryptor(BigInteger p, BigInteger q, BigInteger e, BigInteger d){
		this.p = p;
		this.q = q;
		this.n = p.multiply(q);
		this.e = e;
		this.d = d;
	}
	
	public static BigInteger customModPow(BigInteger b, BigInteger p, BigInteger n){
		String binary = p.toString(2);
		BigInteger r = BigInteger.ONE;
		BigInteger s = b;
		for(int i = (binary.length() - 1); i >= 0; i--){
			if(binary.charAt(i) == '1'){
				r = r.multiply(s).mod(n);
			}
			s = s.pow(2).mod(n);
		}
		return r;
		
	}
	
	BigInteger[] encrypt(String message){
		chunks = message.split("(?<=\\G.{50})");
		int length = chunks.length;
		encrypted = new BigInteger[length];
		
		for (int i = 0; i < length; i++){
			String stringNumber = "";
			for(int j = 0; j < chunks[i].length(); j++){
				 int numLength = String.valueOf((int) chunks[i].charAt(j)).length();
				 switch(numLength) {
				 	case 1: stringNumber += "00" + (int) chunks[i].charAt(j);
				 			break;
				 	case 2: stringNumber += "0" + (int) chunks[i].charAt(j);
				 			break;
				 	case 3: stringNumber += (int) chunks[i].charAt(j);
				 			break; 
				 }	
			}
			System.out.println(stringNumber);
			encrypted[i] = new BigInteger(stringNumber);
			encrypted[i] = customModPow(encrypted[i], e, n);
		}
		return encrypted;
	}
	
	String decrypt(BigInteger[] encrypted_message){
		String output_value = "";
		String output = "";
		
		BigInteger [] decryption = new BigInteger[encrypted_message.length];
		for (int i = 0; i < encrypted_message.length; i++){
			decryption[i] = customModPow(encrypted_message[i], d, n);
		}
		for (int i = 0; i < decryption.length; i++){
			String piece = decryption[i].toString();
			switch(piece.length()%3){
				case 0: break;
			
				case 1: piece = "00" + piece;
						break;
						
				case 2: piece = "0" + piece;
						break;
			}
			output_value += piece;
		} 
		outputArray = output_value.split("(?<=\\G.{3})");
		for (int i = 0; i < outputArray.length; i++){
			output += (char) Integer.parseInt(outputArray[i]);
		}
		return output;
	}
	
	public static BigInteger gcd(BigInteger p, BigInteger q) {
		if (q == BigInteger.valueOf(0)) return p;
		else return gcd(q, p.mod(q));
	}
	
	public static BigInteger generateRandomBigInteger() {
		Random rnd = new Random();
		BigInteger r = new BigInteger(1024, rnd);
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
	
	public static BigInteger[] ext_euc(BigInteger a, BigInteger b){
		BigInteger[] result = new BigInteger[3];
		if (b.compareTo(BigInteger.valueOf(0)) == 0){
			result[0] = a;
			result[1] = BigInteger.ONE;
			result[2] = BigInteger.ZERO;
			return result;
		}
		result = ext_euc(b, a.mod(b));
		BigInteger a_prime = result[1];
		BigInteger b_prime = result[2];
		result[1] = b_prime;
		result[2] = a_prime.subtract(b_prime.multiply(a.divide(b)));
		return result;
	}	
}
