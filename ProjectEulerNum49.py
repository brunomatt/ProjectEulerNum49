# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways:
# (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.
#
# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.
#
# What 12-digit number do you form by concatenating the three terms in this sequence?

raw_primes = []
primes = []

def sieve_eratosthenes(n):
    sieve = [True] * n
    for p in range(2, n):
        if sieve[p]:
            raw_primes.append(p)
            for i in range(p*p, n, p):
                sieve[i] = False
    return raw_primes

sieve_eratosthenes(10000)

for k in raw_primes:
    if len(str(k)) == 4:
        primes.append(k)

def deconstruct(num): #turns number into a list of its digits
    digits = [int(k) for k in str(num)]
    return digits

def convert(list): #turns digit list into a number
    num = sum(digit * pow(10,i) for i, digit in enumerate(list[::-1]))
    return (num)

for k in primes:
    if k < 3340:
        num1 = k + 3330
        num2 = k + 6660
        if num1 in primes:
            if num2 in primes:
                if set(deconstruct(k)) == set(deconstruct(num1)) == set(deconstruct(num2)):
                    if k != 1487:
                        print(k,num1,num2, sep='')