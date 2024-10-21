

list_1 = ["a","b","c"]
print(list_1[-2])

print(len(list_1))
list_1.append("d")
print(list_1)
list_1.insert(1,"Alpha")
print(list_1)
list_1.pop(1)
print(list_1)

print()
list2 = [[1,2,3],[4 ,5,6],[7,8,9]]
print(list2)
print("\n")
for i in range(3):
    for j in range(3):
        print(list2[i][j], end=" ")
    print("\n")

list2A = [[1,2],[3,4]]
list2B = [[5,6],[7,8]]
result = [[0,0],[0,0]]

for i in range(2):
    for j in range(2):
        result[i][j] = list2A[i][j] + list2B[i][j]

        

print(result)