while True:
    print("\n=== PATTERN PRINTER ===")
    print("1. Pattern 1")
    print("2. Pattern 2") 
    print("3. Pattern 3")
    print("4. Pattern 4")
    print("5. Exit")
    
    choice = input("Enter choice (1-5): ")
    
    if choice == '5':
        break
        
    n = int(input("Enter number of rows: "))
    
    if choice == '1':
        # Pattern 1: Right triangle increasing
        for i in range(1, n+1):
            print(str(i) * i)
            
    elif choice == '2':
        # Pattern 2: Centered diamond
        for i in range(1, n+1):
            spaces = " " * (n-i)
            stars = str(i) * (2*i - 1)
            print(spaces + stars)
        for i in range(n-1, 0, -1):
            spaces = " " * (n-i)
            stars = str(i) * (2*i - 1)
            print(spaces + stars)
            
    elif choice == '3':
        # Pattern 3: Left triangle decreasing
        for i in range(n, 0, -1):
            print(str(i) * i)
            
    elif choice == '4':
        # Pattern 4: Pyramid with numbers
        for i in range(1, n+1):
            spaces = " " * (n-i)
            numbers = "".join(str((j+1)) for j in range(i))
            print(spaces + numbers.center(i*2-1))
            
    else:
        print("Invalid choice!")
