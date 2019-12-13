num=[22,1,55,4,8,7]
def bubble_sort_ascending(num):
    for i in range(len(num)-1):
        for j in range(len(num)-1,i,-1):   
            if num[j]<num[j-1] :
                num[j],num[j-1]=num[j-1],num[j]
    return num              
print(bubble_sort_ascending(num))        