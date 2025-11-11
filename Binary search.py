nlist = [12, 24, 34, 67, 70, 75, 81, 89, 99]
search_term = 75
found = False
x = 0

first = 0
last = len(nlist)-1

while (found == False and first<=last):

    mid = (first+last)//2

    if search_term == nlist[mid]:
        found = True

    else:
        if (search_term > nlist[mid]):
            first = mid + 1

        elif (search_term < nlist[mid]):
            last = mid - 1
    x = x + 1
if (found):
    print("Data found!")
    print("Operation count:" x)
else:
    print("No Object Found!")

