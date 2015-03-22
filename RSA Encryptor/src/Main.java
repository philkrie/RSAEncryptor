import java.math.BigInteger;

public class Main {
	  public static void main(String[] args) {
		  
		  Encryptor encryptor = new Encryptor(BigInteger.valueOf(7), BigInteger.valueOf(11), BigInteger.valueOf(13), BigInteger.valueOf(37));
		  
		  boolean searching =true;
		  BigInteger test_e = BigInteger.valueOf(1);
		  while(searching){
			  int candidate = Encryptor.randInt(0, 77);
			  if (Encryptor.gcd(candidate, 60) == 1){
				  test_e = BigInteger.valueOf(candidate);
				  searching = false;
			  }
		  }
		  
		  @SuppressWarnings("unused")
		BigInteger test_d = BigInteger.valueOf(1);
		  
		  
		  System.out.println(test_e);
		  
		  BigInteger message = BigInteger.valueOf(27);
		  System.out.println(message);
		  BigInteger encrypted_message = encryptor.encrypt(message);
		  System.out.println(encrypted_message);
		  BigInteger decrypted_message = encryptor.decrypt(encrypted_message);
		  
		  System.out.println(decrypted_message);
	  }

}
