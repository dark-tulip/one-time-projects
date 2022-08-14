import random

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


a, b, c, d = [random.randint(0, 100) for i in range(4)]

print('\nA =', a, '\nB =', b, '\nC =', c, '\nD =', d)

print("\nGCD from A and B is", gcd(a, b))
print("GCD from A and C is:", gcd(a, c))
print("GCD from A and D is:", gcd(a, d))
