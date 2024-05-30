S = input()
print(
    "{0}\n{1}\n{2}\n{3}\n{4}".format(
        any(I.isalnum() for I in S),
        any(J.isalpha() for J in S),
        any(K.isdigit() for K in S),
        any(L.islower() for L in S),
        any(M.isupper() for M in S),
    )
)
input()