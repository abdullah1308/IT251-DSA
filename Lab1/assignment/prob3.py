def isPrime(num):
    if num < 2:
        return False
    
    isPrime = True
    i = 2
    
    while i * i <= num:
        if num % i == 0:
            isPrime = False
            break
        i+=1
    
    return isPrime

def main():
    num = int(input("Enter a number: "))
    
    if isPrime(num):
        print(True)
        print(num, "is a prime number.")
    else:
        print(False)
        print(num, "is not a prime number.")

if __name__ == '__main__':
    main()