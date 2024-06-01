for _ in range(int(input())):
    try:
        N = input()
        N1 = float(N)
        print("." in N and N[-1] != ".")
    except:
        print(False)
input()