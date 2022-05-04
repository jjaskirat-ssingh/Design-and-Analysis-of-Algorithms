class ItemValue:
    def __init__(self, wt, val, ind):
        self.wt = wt
        self.val = val
        self.ind = ind
        self.cost = val//wt

    def __lt__(self, other):
        return self.cost < other.cost


class FractionalKnapsack:   #T(n) = O(nlogn)
    def getMaxValue(wt, val, capacity):
        iVal = []
        for i in range(len(wt)):
            iVal.append(ItemValue(wt[i], val[i], i))

        iVal.sort(reverse = True)
    
        totalValue = 0
        for i in iVal:
            curWt = int(i.wt)
            curVal = int(i.val)
            if capacity - curWt >= 0:
                capacity = capacity - curWt
                totalValue = totalValue + curVal
            else:
                fraction = capacity/curWt
                totalValue = totalValue + (fraction * curVal)
                capacity = int(capacity - (fraction * curWt))
                break
        
        return totalValue


if __name__ == "__main__":
    wt = [10, 40, 20, 30]
    val = [60, 40, 100, 120]
    capacity = 50

    maxValue = FractionalKnapsack.getMaxValue(wt, val, capacity)
    print("Maximum value in Knapsack: ", maxValue)
        