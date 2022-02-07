"""
    The function which generates fibonacci numbers iteratively is more efficient than the recursive function.
    The recursive function calculates the fibonacci of numbers multiple times and also occupies more
    more memory in the function call stack. 
"""



def fibonacci_iter(num):
    if num == 1:
        return 0
    elif num == 2:
        return 1
    
    first = 0
    second = 1
    count = 3
    
    while count <= num: 
        sum = first + second
        first = second
        second = sum
        count += 1
        
    return sum


def fibonacci_recur(num):
    if num == 1:
        return 0
    elif num == 2:
        return 1
    
    return fibonacci_recur(num - 1) + fibonacci_recur(num - 2)

def main():
    num = int(input("Enter a number: "))
    
    print("Fibonacci numbers obtained iteratively: ")
    for i in range(1, num+1):
        print(fibonacci_iter(i), end=' ')
    
    print()
    
    print("Fibonacci numbers obtained recursively: ")
    for i in range(1, num+1):
        print(fibonacci_recur(i), end=' ')
        
    print()
        
if __name__ == '__main__':
    main()