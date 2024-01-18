import argparse
import math

# Fibonacci sequence
def fibonacci(length):
    sequence = [0, 1]
    while len(sequence) < length:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence[:length]

# Sequence of prime numbers
def prime(length):
    sequence = []
    num = 2
    while len(sequence) < length:
        if all(num % i != 0 for i in range(2, int(math.sqrt(num)) + 1)):
            sequence.append(num)
        num += 1
    return sequence

# Sequence of squares
def square(length):
    return [i ** 2 for i in range(1, length + 1)]

# Sequence of triangular numbers
def triangular(length):
    sequence = []
    current_sum = 0
    for i in range(1, length + 1):
        current_sum += i
        sequence.append(current_sum)
    return sequence

# Iterative calculation of factorial
def factorial(n):
    result = 1
    factorial_sequence = []
    for i in range(1, n + 1):
        result *= i
        factorial_sequence.append(result)
    return factorial_sequence

# main function 
def main(args):
    if args.sequence == "fibonacci":
        result = fibonacci(args.length)
    elif args.sequence == "prime":
        result = prime(args.length)
    elif args.sequence == "square":
        result = square(args.length)
    elif args.sequence == "triangular":
        result = triangular(args.length)
    elif args.sequence == "factorial":
        result = factorial(args.length)
    else:
        result = []  
    
    return result

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate mathematical sequences.")
    parser.add_argument("--length", type=int, help="Length of the computed sequence.")
    parser.add_argument("--sequence", choices=["fibonacci", "prime", "square", "triangular", "factorial"], help="Name of the sequence.")
    
    args = parser.parse_args()
    result = main(args)
    
    print(result)
