def MaxActivities(arr, n):
    selected = []

    Activity.sort(key = lambda x : x[1])    # sort jobs according to their finish times

    i = 0
    selected.append(arr[i]) # 1st activity always gets selected

    for j in range(1, n):
        if arr[j][0] >= arr[i][1]:  # if this activity has start time >= finish time of previously selected activity
            selected.append(arr[j])
            i=j
    
    return selected

Activity = [[5,9], [1,2], [3,4], [0,6], [5,7], [8,9]]
n = len(Activity)
selected = MaxActivities(Activity, n)
print("Selected Activities: ")
print(selected)