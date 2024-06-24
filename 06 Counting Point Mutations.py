s = input("Insert string No. 1: ")
t = input("Insert string No. 2: ")

def HammDist(s, t):
    if len(s) != len(t):
        raise ValueError("Strings should be of equal length.")

    distance = 0

    for x in range(len(s)):
        if s[x] != t[x]:
            distance += 1

    return distance

HmDsResult = HammDist(s, t)
print(HmDsResult)