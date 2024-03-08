from copy import deepcopy

weekdays_1 = ["Branch 1", ["Monday", "Wednesday", "Friday"]]

weekdays_2 = deepcopy(weekdays_1) # duplicate the first list
weekdays_2[0] = "Branch 2" # change the branch name in the second list
weekdays_2[1].insert(1, "Tuesday") # insert one more weekday name

print(*weekdays_1)
print(*weekdays_2)