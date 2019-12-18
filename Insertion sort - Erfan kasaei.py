#tarif araye khali
a = []
#for baraye por kardan araye
for i in range(0,5):
    a.append(int(input(f'adad {i+1} ra vared konid : ')))
#tarif function insertion sort
def insertion_sort(arr):  
    for i in range(len(arr)):
        cursor = arr[i]
        pos = i
        while pos > 0 and arr[pos - 1] > cursor:
            arr[pos] = arr[pos - 1]
            pos = pos - 1
        arr[pos] = cursor
    return arr
#ejra kardan function
xx = insertion_sort(a)
#chap araye moratab shode
print("araye moratab shode shoma : ")
for i in range(len(a)):
    print(xx[i] , end = ' ')







