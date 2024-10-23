number_rows = int(input("Enter the number of rows: "))
print(f"Enter the number of rows: {number_rows}")

begin = 1

for i in range(1, number_rows + 1):
    for j in range(i):
        if begin <= number_rows * (number_rows + 1) // 2:
            print(begin, end = ' ')
            begin += 1
    print( )