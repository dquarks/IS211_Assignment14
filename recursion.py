def fibonnaci(n):
    if(n <= 1):
        return n
    return (fibonnaci(n-1) + fibonnaci(n-2))

def gcd(a,b):
    if(a == 0):
        return b
    return gcd(b % a, a)

def compareTo(s1, s2):
    if len(s1) < len(s2):
        return -2
    elif s1 == s2:
        return 0
    elif len(s1) > len(s2):
        return 1
    return compareTo(s1[:-1], s2[:-1])
