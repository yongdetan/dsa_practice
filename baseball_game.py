ops = ["5","-2","4","C","D","9","+","+"]

def calPoints(ops):
    record = []
    total = 0
    for v in ops:   
        if v == "C":
            total -= record[-1]
            del record[-1]            
        elif v == "D":
            total += (record[-1] * 2)
            record.append(record[-1] * 2)
           
        elif v == "+":
            total += (record[-1]+record[-2])
            record.append(record[-1]+record[-2])
            
        else:
            record.append(int(v))
            total += int(v)
    
    return total

print(calPoints(ops))