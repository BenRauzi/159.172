def binary_search(the_list, lower, upper, item):
   
    if lower > upper:
       return -1

    middle_pos = (lower + upper) // 2
    print(middle_pos)

    if the_list[middle_pos] < item:
       lower = middle_pos+1
       return binary_search(the_list, lower, upper, item)
    elif the_list[middle_pos] > item:
       upper = middle_pos-1
       return binary_search(the_list, lower, upper, item)
    else:
       return middle_pos

def search2(the_list, lower, upper, item):
    if  lower>upper:
        print("The name was not in the list.")
        return
    middle_pos = (lower + upper) // 2
    if the_list[middle_pos] < item:
        lower = middle_pos+1
        search2(the_list, lower, upper, item)
    elif the_list[middle_pos] > item:
        upper = middle_pos - 1
        search2(the_list, lower, upper, item)
    else:
        print( "Thenameisaposition",middle_pos)
        return

print(binary_search(sorted([1,12,3,4,5,6,7,8,5,6]), 0, 9, 12))