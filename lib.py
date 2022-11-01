n = int(input("n="))
a = []
c =[]
for i in range (0,n):
    print("Введите список")

    count = int(input("count="))
    c.append(count)
    l = []
    for j in range (0,count):
        k=input()
        l.append(k)
    a.append(l)
b = []
for i in range (0,n):
    max = -1
    for j in range (0,c[i]):
        if (max<a[i].count(a[i][j])):
            max = a[i].count(a[i][j])

    b.append(max)
print(b)



