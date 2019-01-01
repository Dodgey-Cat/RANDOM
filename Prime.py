import time
prime_numbers = 0

def is_prime_number(x):
    if x >= 2:
        for y in range(2,x):
            if not ( x % y ):
                return False
    else:
        return False
    return True
	        


for i in range(100000000):
    time.sleep(.0000003)
    if is_prime_number(i):
        prime_numbers += 1
        print (i)

print ("We found " + str(prime_numbers) + " prime numbers."
       446009
