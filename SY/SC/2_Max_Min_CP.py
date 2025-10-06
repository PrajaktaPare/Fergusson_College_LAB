def menu():
    print("1 - Max Min")
    print("2 - Max Product")
    print("3 - Exit")
    
    

while True:
    a=[]
    b=[]
    
    n=int(input("Enter number of elements in fuzzy set A: "))
    for i in range(n):
        ele=float(input(f"Enter element {i+1} of A: "))
        a.append(ele)
    
    m=int(input("Enter number of elements in fuzzy set B: "))
    for i in range(m):
        ele=float(input(f"Enter element {i+1} of B: "))
        b.append(ele)
        
    menu()
    opt=int(input("Select option: "))
    if opt in [1,2] and n!=m:
        print("Error: Fuzzy sets A and B must be of the same length for this operation.\n")
        continue
    
    if opt==1:
        max_min=[max(min(a[i],b[i]) for i in range(n))]
        print("Max Min is:",max_min)
    elif opt==2:
        max_product=[max(a[i]*b[i] for i in range(n))]
        print("Max Product is:",max_product)
    elif opt==3:
        break