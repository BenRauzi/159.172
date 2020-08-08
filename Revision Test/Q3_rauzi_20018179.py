import random

#class Test:
#    def __init__(self):
#        pass
#    def __str__(self):
#        return "Hello There"

def random_print_list(a_list):
    while len(a_list) > 0:
        index = random.randrange(len(a_list))
        print(a_list.pop(index)) #print() automatically converts to string
    print("All done!")

#item = Test()
#random_print_list([item])

#Commented out parts to prove it works and that print() automatically prints string representation