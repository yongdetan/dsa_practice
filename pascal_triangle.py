numRows = 5

def generate(numRows):
    res = []
    for x in range(numRows):
        temp = [1] #create a temp list with 1 inside since the list always stars with 1
        if len(res) >= 1:
            for i in range(len(res)-1):
                temp.append(res[x-1][i]+res[x-1][i+1]) #x-1 to not go out of range, 
            temp.append(1) #add 1 to the end of the temp list because the left and right side of the list is always 1
        res.append(temp)
    return res
            
generate(numRows)