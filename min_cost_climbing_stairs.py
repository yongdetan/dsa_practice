cost = [0,0,0,1]


def minCostClimbingStairs(cost):
    counter = 0
    minCost = 0
    while counter < len(cost):
        print(counter, minCost, len(cost))
        if counter+2 >= len(cost):
            return minCost
        if counter == 0:
            if cost[counter+1] < cost[counter] or counter == 0 and cost[counter] == cost[counter+1] or  cost[counter+2] > cost[counter+1]:
                minCost += cost[counter+1]
            else:
                minCost += cost[counter]
        else:
            if cost[counter] < cost[counter+1]:
                minCost += cost[counter]
            if cost[counter+1] < cost[counter]:
                minCost += cost[counter+1]
                counter += 1
            if cost[counter] == cost[counter+1]:
                minCost += cost[counter+1]
                counter += 1
        
        counter += 1
    return(minCost)

print(minCostClimbingStairs(cost))