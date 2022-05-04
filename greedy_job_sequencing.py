def printJobScheduling(arr, t):
    n = len(arr)

    for i in range(n):  # sort all jobs acc to decreasing order of profit              
        for j in range(n-i-1):
            if arr[j][2] < arr[j+1][2]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    result = [False]*t  # to keep track of free time slots
    job = ['-1']*t  # to store result, i.e. sequence of jobs

    for i in range(len(arr)):   # iterate through all jobs
        for j in range(min(t-1, arr[i][1]-1), -1, -1):  # we start from last possible slot
            if result[j] is False:
                result[j] = True
                job[j] = arr[i][0]
                break
        
    print(job)

arr = [['a', 2, 100],
        ['b', 1, 19],
        ['c', 2, 27],
        ['d', 1, 25],
        ['e', 3, 15]]

print("Maximum Profit Sequence of Jobs: ")
printJobScheduling(arr, 3)