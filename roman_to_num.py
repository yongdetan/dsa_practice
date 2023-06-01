dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
total = 0
s = "LVIII"

for i in range(len(s)):
    current = dict[s[i]]
    next = 0
    #print("current", current)
    if i+1 < len(s):
        next = dict[s[i+1]] 
    if ((current < next) and (next % 5 == 0)) or ((current < next) and (next % 10 == 0)) :      
        total -= current 

    else:
        total += current
print(total)
