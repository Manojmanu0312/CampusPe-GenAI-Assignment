def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def fibonacci(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def sum_of_digits(n):
    return sum(int(d) for d in str(abs(n)))

def armstrong(n):
    s = str(abs(n))
    power = len(s)
    return sum(int(d)**power for d in s) == abs(n)

def gcd(a, b):
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a

def test_all(n):
    """Test all functions on number n"""
    results = {
        'prime': is_prime(n),
        'fibonacci': fibonacci(n),
        'sum_digits': sum_of_digits(n),
        'armstrong': armstrong(n),
        'gcd(12,n)': gcd(12, n)
    }
    return results

def display_results(n, results):
    print(f"\nResults for {n}:")
    print(f"Is prime: {results['prime']}")
    print(f"Fibonacci({n}): {results['fibonacci']}")
    print(f"Sum of digits: {results['sum_digits']}")
    print(f"Is Armstrong: {results['armstrong']}")
    print(f"GCD(12,{n}): {results['gcd(12,n)']}")


while True:
    print("\n=== NUMBER FUNCTIONS ===")
    print("1. Is Prime(n)")
    print("2. Fibonacci(n)") 
    print("3. Sum of Digits(n)")
    print("4. Armstrong(n)")
    print("5. GCD(a,b)")
    print("6. Test All(n)")
    print("7. Exit")
    
    choice = input("Enter choice (1-7): ")
    
    if choice == '7':
        break
        
    if choice == '6':
        n = int(input("Enter number: "))
        results = test_all(n)
        display_results(n, results)
    elif choice in ['1', '2', '3', '4']:
        n = int(input("Enter number: "))
        if choice == '1':
            print(f"{n} is {'prime' if is_prime(n) else 'not prime'}")
        elif choice == '2':
            print(f"Fibonacci({n}) = {fibonacci(n)}")
        elif choice == '3':
            print(f"Sum of digits({n}) = {sum_of_digits(n)}")
        elif choice == '4':
            print(f"{n} is {'Armstrong' if armstrong(n) else 'not Armstrong'}")
    elif choice == '5':
        a = int(input("Enter a: "))
        b = int(input("Enter b: "))
        print(f"GCD({a},{b}) = {gcd(a, b)}")
    else:
        print("Invalid choice!")
