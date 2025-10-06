def menu():
    print("1 - Union")
    print("2 - Intersection")
    print("3 - Complement")
    print("4 - Algebraic Sum")
    print("5 - Algebraic Product")
    print("6 - Cartesian Product")
    print("7 - Exit")


while True:
    a = []
    b = []
    
    n = int(input("Enter number of elements in fuzzy set A: "))
    for i in range(n):
        ele = float(input(f"Enter element {i+1} of A: "))
        a.append(ele)
        
    m = int(input("Enter number of elements in fuzzy set B: "))
    for i in range(m):
        ele = float(input(f"Enter element {i+1} of B: "))
        b.append(ele)

    menu()
    opt = int(input("Select option: "))

    if opt in [1, 2, 4, 5] and n != m:
        print("Error: Fuzzy sets A and B must be of the same length for this operation.\n")
        continue

    if opt == 1:
        union = [max(a[i], b[i]) for i in range(n)]
        print("Union is:", union)

    elif opt == 2:
        intersection = [min(a[i], b[i]) for i in range(n)]
        print("Intersection is:", intersection)

    elif opt == 3:
        comp_a = [1 - val for val in a]
        comp_b = [1 - val for val in b]
        print("Complement of A is:", comp_a)
        print("Complement of B is:", comp_b)

    elif opt == 4:
        algebraic_sum = [a[i] + b[i] - (a[i] * b[i]) for i in range(n)]
        print("Algebraic Sum is:", algebraic_sum)

    elif opt == 5:
        algebraic_product = [a[i] * b[i] for i in range(n)]
        print("Algebraic Product is:", algebraic_product)

    elif opt == 6:
        cartesian_product = []
        for i in range(n):
            for j in range(m):
                cartesian_product.append(((a[i], b[j]), min(a[i], b[j])))
        print("Cartesian Product (with min membership) is:", cartesian_product)

    elif opt == 7:
        print("Exiting program.")
        break

    else:
        print("Invalid option. Please try again.\n")
