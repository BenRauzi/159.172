def evens(a_list):
    return [a_list[i] for i in range(len(a_list)) if i % 2 == 0] #I'm aware this does not look as 'clean' as a for loop... but given this is a revision test and I've already used them I feel I may as well do this

#print(evens(["a", "b", "c", "d", "e"])) # Testing

test_list = [["me","my"],["you","yours"],["them"],["their"],["theirs"]] #I can't tell if this is a purposely confusing list or if some brackets [] are missing from when the question was written
print(evens(test_list)) 