
def BubbleSort(list, answer):

  #this loops through ever element in our list / array
  for i in range(len(list)):
    #This compares each element using the loop above
    for e in range(0, len(list) - i - 1):
      #This part changes depending an how you want to sort your numbers.
      #> for ascending, < for descending.
      if answer == "desc":
        if list[e] < list[e + 1]:
          temp = list[e]
          list[e] = list[e + 1]
          list[e + 1] = temp
          list_ = list
          
      elif answer == "asce":
        if list[e] > list[e + 1]:
          temp = list[e]
          list[e] = list[e + 1]
          list[e + 1] = temp
      else:
        print("Unexpected error.")
    # list_ = list
    # print(list_)


array = [-6, 3, 5, 0, -23, 10, 17, 12, -2, 15, 25]
print(array)
des_asc = input("Would you like list the numbers Descending (d) or Ascending (a)?")
if des_asc == "d":
  ans = 'desc'
  BubbleSort(array, ans)
elif des_asc == "a":
  ans = 'asce'
  BubbleSort(array, ans)
else:
  print("Answer not valid, try again.")

print(array)