
from math import sqrt
primes = [2,3,5,7,11,13,17,19,23,\
29,31,37,41,43,47,53,59,61,\
67,71,73,79,83,89,97,101,103,107,\
109,113,127,131,137,139,149,151,\
157,163,167,173,179,181,191,193,197,\
199,211,223,227,229,233,239,241,251,\
257,263,269,271,277,281,283,293,307,\
311,313,317,331,337,347,349,353,359,\
367,373,379,383,389,397,401,409,419,\
421,431,433,439,443,449,457,461,463,\
467,479,487,491,499,503,509,521,523,\
541,547,557,563,569,571,577,587,593,\
599,601,607,613,617,619,631,641,643,\
647,653,659,661,673,677,683,691,701,\
709,719,727,733,739,743,751,757,761,\
769,773,787,797,809,811,821,823,827,\
829,839,853,857,859,863,877,881,883,\
887,907,911,919,929,937,941,947,953,\
967,971,977,983,991,997]

#line1 = raw_input("")
#line1 = line1.split()
#array_len = int(line1[0])
#msg_count = int(line1[1])

array_len, msg_count = raw_input("").split()
array_len = int(array_len)
msg_count = int(msg_count)

line2 = raw_input()
array = line2.split()
array_dict = {}
for i in array:
    int_i = int(i)
    array_dict[int_i] = int_i

input_numbers = []
for i in range(msg_count):
    input_numbers.append(int(raw_input("")))

def prime_factorize(n, factors, index):
    if n == 1:
        return
    for i in range(index, len(primes)):
        if primes[i] > sqrt(n):
            factors.append(n)
            return factors
        quotient = n
        if quotient % primes[i] == 0:
            while quotient % primes[i] == 0:
                factors.append(primes[i])
                quotient = quotient/primes[i]
            #print "recursing for: ", quotient, i
            return prime_factorize(quotient, factors, i)

def get_prime_pairs(factors):
    prime_pairs = []
    for i in range(len(factors)):
        for j in range(i+1, len(factors)):
            pair = (factors[i], factors[j])
            prime_pairs.append(pair)
    prime_pairs = list(set(prime_pairs))
    return prime_pairs

def get_remaining_factors(factors, pair):
    pair_array = list(pair)
    #print "pair_array: ", pair_array
    return [i for i in factors if not i in pair_array or pair_array.remove(i)]
#    result = []
#    for i in factors:
#        result.append(i)
    #print "result: ", result
#    for i in pair:
#        result.remove(i)
#    return result

def are_all_nos_same(numbers):
    temp = set(numbers)
    if len(temp) == 1:
        return True
    else:
        return False

def calc_product(numbers):
    product = 1
    for i in numbers:
        product *= i
    return product

def decryption(n):
    if n == 0 or n == 1:
        print "NO"
        return
    factors = []
    prime_factorize(n, factors, 0)
    #print "factors: ", factors
    primePairs = get_prime_pairs(factors)
    #print "prime pairs: ", primePairs
    if len(factors) == 1:
        print "NO"
        return
    for prime_pair in primePairs:
        #print "prime_pair: ", prime_pair
        product = n/(prime_pair[0]*prime_pair[1])
        #print "product: ", product
        #calc_product(remaining_factors)
        if product in array_dict:
            print "YES"
            return

        remaining_factors = get_remaining_factors(factors, prime_pair)
        #print "remaining_factors: ", remaining_factors
        if len(remaining_factors) > 1 and remaining_factors[0] in array_dict:
            if are_all_nos_same(remaining_factors):
                print "YES"
                return
    print "NO"


def main():
    for i in input_numbers:
        decryption(i)

if __name__ == '__main__':
    main()
