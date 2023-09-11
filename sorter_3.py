import os
os.system('cls')

def insertionSortAsce(arr):
    n = len(arr)
    
    if n <= 1:
        return

    for i in range(1, n):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]: 
            arr[j+1] = arr[j] 
            j -= 1
        arr[j+1] = key 

def insertionSortDesc(arr):
    n = len(arr)
    if n <= 1:
        return
 
    for i in range(1, n):
        key = arr[i]
        j = i-1
        while j >= 0 and key > arr[j]: 
            arr[j+1] = arr[j] 
            j -= 1
        arr[j+1] = key 
  
arr = [12, 11, 13, 5, 6]
arr_ = [12, 11, 13, 5, 6]

des_asc = input("Would you like list the numbers Descending (d) or Ascending (a)?")
if des_asc == "d":
#   ans = 'desc'
  insertionSortDesc(arr_)
  print(arr_)
elif des_asc == "a":
#   ans = 'asce'
  insertionSortAsce(arr)
  print(arr)
else:
  print("Answer not valid, try again.")

