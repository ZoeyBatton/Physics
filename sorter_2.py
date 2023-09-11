import os
os.system('cls')

def selectionSort(array, size, answer):
    
    for i in range(size):
        if answer == "asce":
            min_index = i
    
            for j in range(i + 1, size):
                if array[j] < array[min_index]:
                    min_index = j
            (array[i], array[min_index]) = (array[min_index], array[i])

        elif answer == "desc":
            min_index = i
 
            for j in range(i + 1, size):
                if array[j] > array[min_index]:
                    min_index = j
            (array[i], array[min_index]) = (array[min_index], array[i])
 
elements = [-2, 6, 1, -7, -12, 24, 10, 17]
size = len(elements)

des_asc = input("Would you like list the numbers Descending (d) or Ascending (a)?")
if des_asc == "d":
  ans = 'desc'
  selectionSort(elements, size, ans)
  print(elements)
elif des_asc == "a":
  ans = 'asce'
  selectionSort(elements, size, ans)
  print(elements)
else:
  print("Answer not valid, try again.")
