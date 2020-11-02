count = 0
def sequential_search(the_list, item):
    global count
    count += 1
    if the_list == []:
       return False
    elif the_list[0] == item:
       return True
    else:
       return sequential_search(the_list[1:], item)

test = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

sequential_search(test, 16)

print(count)