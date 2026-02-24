def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print("1. Single number check")
print("2. Range check")
choice = input("Choose (1/2): ")

if choice == '1':
    num = int(input("Enter a number: "))
    print(f"{num} is a {'prime' if is_prime(num) else 'not prime'} number")
    
elif choice == '2':
    start = int(input("Enter start range: "))
    end = int(input("Enter end range: "))
    primes = [str(num) for num in range(start, end + 1) if is_prime(num)]
    print(f"Prime numbers {start},{end}: {', '.join(primes) if primes else 'None'}")
