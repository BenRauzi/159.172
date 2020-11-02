the_list = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

new_list = [the_list[i] for i in range(len(the_list)) if i % 2 == 0 and the_list[i] % 2 == 0]

print(new_list)