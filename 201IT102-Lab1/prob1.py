def factorial_iter(num):
    if num < 0:
        print("Factorial undefined for numbers less than 0")
        return
    fact = 1
    for i in range(2, num+1):
        fact *= i
    return fact

def factorial_recur(num):
    if num == 0 or num == 1:
        return 1
    elif num < 0:
        print("Factorial undefined for numbers less than 0")
        return
        
    return num * factorial_recur(num - 1)

def main():
    num = int(input("Enter number to calculate factorial: "))
    fact_iter = factorial_iter(num)
    fact_recur = factorial_recur(num)
    
    print("Factorial calculated iteratively:", fact_iter)
    print("Factorial calculated recursively:", fact_recur)
    
if __name__ == '__main__':
    main()