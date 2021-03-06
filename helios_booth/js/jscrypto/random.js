
/*
 * Random Number generation, now uses the glue to Java
 */

Random = {};

Random.GENERATOR = null;

Random.setupGenerator = function() {
  // no longer needed
/*    if (Random.GENERATOR == null && !USE_SJCL) {
	    if (BigInt.use_applet) {
	      var foo = BigInt.APPLET.newSecureRandom();
	      Random.GENERATOR = BigInt.APPLET.newSecureRandom();
	    } else {
	      // we do it twice because of some weird bug;
	      var foo = new java.security.SecureRandom();
	      Random.GENERATOR = new java.security.SecureRandom();
	    }
    }
    */
};

Random.getRandomInteger = function(max) {
  var bit_length = max.bitLength();
  Random.setupGenerator();
  var random;
  random = sjcl.random.randomWords(bit_length / 32, 0);
  // we get a bit array instead of a BigInteger in this case
  var rand_bi = new BigInt(sjcl.codec.hex.fromBits(random), 16);
  return rand_bi.mod(max);
  return BigInt._from_java_object(random).mod(max);
};
Random.random_k_relative_prime_p_1= function(p) {
        while (true){
            var k = Random.getRandomInteger(p-1);
            if (gcd(k,p-1)==1){
                return k;
                }
           }
         };
            

