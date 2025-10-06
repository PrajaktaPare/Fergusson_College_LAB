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

# Check if sets are compatible
if n != m:
    print("Error: Fuzzy sets A and B must have the same number of elements.")
else:
    # Complement of A and B
    comp_a = [1 - x for x in a]
    comp_b = [1 - x for x in b]

    # Union and Intersection
    union = [max(a[i], b[i]) for i in range(n)]
    intersection = [min(a[i], b[i]) for i in range(n)]

    # De Morgan's Laws
    demorgan1_lhs = [1 - u for u in union]               # (A ∪ B)'
    demorgan1_rhs = [min(comp_a[i], comp_b[i]) for i in range(n)]  # A' ∩ B'

    demorgan2_lhs = [1 - i for i in intersection]        # (A ∩ B)'
    demorgan2_rhs = [max(comp_a[i], comp_b[i]) for i in range(n)]  # A' ∪ B'

    # Display Results
    print("\nDe Morgan's Law 1: (A ∪ B)' = A' ∩ B'")
    print("LHS:", demorgan1_lhs)
    print("RHS:", demorgan1_rhs)
    print("Equal?" , demorgan1_lhs == demorgan1_rhs)

    print("\nDe Morgan's Law 2: (A ∩ B)' = A' ∪ B'")
    print("LHS:", demorgan2_lhs)
    print("RHS:", demorgan2_rhs)
    print("Equal?", demorgan2_lhs == demorgan2_rhs)
