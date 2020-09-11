# Read in data from a file and put it into a Python List
def binary_search(the_list, lower, upper, item):
   
   if lower > upper:
      print( "The name was not in the list." )
      return -1

   middle_pos = (lower + upper) // 2
   if the_list[middle_pos][0] < item[0]:
      lower = middle_pos+1
      return binary_search(the_list, lower, upper, item)
   elif middle_pos == 0 and the_list[middle_pos - 1][0] == item:
      return middle_pos
   elif the_list[middle_pos][0] > item or (the_list[middle_pos][0] == item and the_list[middle_pos - 1][0] == item):
      upper = middle_pos-1
      return binary_search(the_list, lower, upper, item)
   else:
      return middle_pos

#print all names beginning with a given char. Assumed names are alphabetically sorted
def names_beginning(the_list, char):

   index = binary_search(the_list,  0, len(the_list)-1, char)

   if index == -1:
      return

   while True:
      if the_list[index][0] != char:
         break
   
      print(the_list[index])
      index += 1

#replaced this bad function by improving the binary search
#thought I would leave in it commented just because I can.
# def find_lowest(list, index, char): #binary search finds the pos of a name with the the given char. find_lowest() recursively finds the first occurance
#    if list[index - 1][0] == char:
#       return find_lowest(list, index - 1, char)

#    return index

def partition(array, start, end):
   pivot = array[start]
   low = start + 1
   high = end

   while True:
      # If the current value we're looking at is larger than the pivot
      # it's in the right place (right side of pivot) and we can move left,
      # to the next element.
      # We also need to make sure we haven't surpassed the low pointer, since that
      # indicates we have already moved all the elements to their correct side of the pivot
      while low <= high and len(array[high]) >= len(pivot):
         high = high - 1

      # Opposite process of the one above
      while low <= high and len(array[low]) <= len(pivot):
         low = low + 1

      # We either found a value for both high and low that is out of order
      # or low is higher than high, in which case we exit the loop
      if low <= high:
         array[low], array[high] = array[high], array[low]
         # The loop continues
      else:
         # We exit out of the loop
         break

   array[start], array[high] = array[high], array[start]

   return high

#unstable quick sort
def quick_sort(array, start, end):
   if start >= end:
      return

   p = partition(array, start, end)
   quick_sort(array, start, p-1)
   quick_sort(array, p+1, end)

#stable quick sort
def insertion_sort(list):
    # Start at the second element (pos 1).
    for i in range(1, len(list)):

        # Get the value of the element to insert
        keyValue = list[i]
        # Scan to the left
        j = i - 1

        # Loop each element, moving them up until
        # we reach the location where the insertion should be done 
        while (j >=0) and (len(list[j]) > len(keyValue)):
            list[j+1] = list[j]
            j = j - 1

        # Everything's been moved out of the way, insert
        # the key into the correct location
        list[j+1] = keyValue

#sort by length using quicksort
def sort_by_length_quicksort(the_list):
   quick_sort(the_list, 0, len(the_list) - 1)

   #print sorted items
   for i in the_list:
      print(i)

#sort by length using insertion sort
def sort_by_length(the_list):
   insertion_sort(the_list)
   
   #pritns sorted items
   for i in the_list:
      print(i)
file = open("example_sorted_names.txt")
 

#load names from file
name_list = []
for line in file:
    line=line.strip()
    name_list.append(line)
 
file.close()

# function calls

# names_beginning(name_list, "S")

# sort_by_length(name_list)

# sort_by_length_quicksort(name_list)

