Items = {}
for _ in range(int(input())):
    Value = input().split()
    Name = " ".join(Value[:-1])
    Price = int(Value[-1])
    for i in Items.keys():
        if i == Name:
            Items[Name] = Items[Name] + Price
            break
    else:
        Items[Name] = Price
for I in Items.items():
    print(*I, sep=" ")
input()