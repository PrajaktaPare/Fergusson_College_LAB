rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = []
print("Enter the membership values row-wise (between 0 and 1):")
for i in range(rows):
    row = []
    for j in range(cols):
        val = float(input(f"Element [{i+1}][{j+1}]: "))
        if 0 <= val <= 1:
            row.append(val)
        else:
            print("Invalid value. Must be between 0 and 1.")
            exit()
    matrix.append(row)

lam = float(input("Enter lambda (λ) cut value (between 0 and 1): "))
if not (0 <= lam <= 1):
    print("Invalid lambda value. Must be between 0 and 1.")
    exit()

lambda_cut_matrix = []
for i in range(rows):
    row = []
    for j in range(cols):
        if matrix[i][j] >= lam:
            row.append(1)
        else:
            row.append(0)
    lambda_cut_matrix.append(row)


print("\nOriginal Fuzzy Matrix:")
for row in matrix:
    print(row)

print(f"\nλ-cut Matrix (λ = {lam}):")
for row in lambda_cut_matrix:
    print(row)
