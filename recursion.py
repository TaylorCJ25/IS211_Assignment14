nth = int(input("Enter nth number of potential fibonacci sequence: "))
def fibonacci(n):  #https://realpython.com/fibonacci-sequence-python/
   if n <= 1: 
       return n
   else:
       return(fibonacci(n-1) + fibonacci(n-2))
print(fibonacci(nth))


num1 = int(input("Enter the first number to find the GCD of: "))
num2 = int(input("Enter the second number to find the GCD of: "))

def gcd(a , b): #https://www.geeksforgeeks.org/gcd-in-python/
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

print(gcd(num1,num2))

s1 = input("Enter First String: ")
s2 = input("Enter Second String: ")

def compareTo(s1, s2): #
    # https://www.geeksforgeeks.org/string-comparison-in-python/
    #https://careerkarma.com/blog/python-compare-strings/ : great for understanding which symbols would ensure that;
    # a negative number if s1 < s2,
    # if s1 == s2, and
    # a positive number if s1 > s2

    if len(s1) == 1 and len(s2) == 1:
        if (s1[0] == s2[0]):
            return True
    elif s1[0] == s2[0]:
        return compareTo(s1[1:],s2[1:])
    else:
        return False

print(compareTo(s1,s2))
