strs = ["flower","flow","flight"]

def test(strs):
    common = ""
    smallest = min(strs, key=len)
    for i in range(len(smallest)):
        for char in strs:
            if i == len(char) or char[i] != smallest[i]:
                return common
        common += smallest[i]
    return common
print(test(strs))
