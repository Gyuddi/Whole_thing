def bubble_sort(a_list):
    movement = False
    while (True):
        movement = False
        for i in range(len(a_list)-1):
            if(a_list[i]>a_list[i+1]):
                a_list[i],a_list[i+1] =a_list[i+1],a_list[i]
                movement = True
        if (movement == False):
            break
    return a_list
a = [5,4,9,7,6,2,1,8,5,4]
print(bubble_sort(a))

