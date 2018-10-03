#Kanishka Udapitiya - KUDKC152

import random

#Implementing a function to Insertion-Sort
def InsertionSort (LottoNum):
    for i in range(1, len(LottoNum)):
        currentValue = LottoNum[i]
        position = i

        while (position > 0) and (LottoNum[position-1] > currentValue):
            LottoNum[position] = LottoNum[position-1]
            position = position-1
            
        LottoNum[position] = currentValue

#Implementing a function to Merge-Sort
def MergeSort(LottoNum):
    if len(LottoNum)>1:
        mid = len(LottoNum)//2
        lefthalf = LottoNum[:mid]
        righthalf = LottoNum[mid:]

        MergeSort(lefthalf)
        MergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                LottoNum[k]=lefthalf[i]
                i=i+1
            else:
                LottoNum[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            LottoNum[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            LottoNum[k]=righthalf[j]
            j=j+1
            k=k+1

#Function 1
#Implementing a function to compare two lists
def CommonValue (list1, list2):                 #O(N)
    count = 0                                   #O(1)
    for i in range (0,6):                       #O(1)
        for j in range (0,6):                   #O(1)
            if list1[i] == list2[j]:            #O(N)
                count += 1                      #O(1)
    return count                                #O(1)
#Time complexity of the Function 1
#O(N) + O(1) + O(1) + O(1) + O(N) + O(1) + O(1) = O(1)

#Function 2
#Implementing a function to check a player's winning status
def BinarySearch (target,array ,left, right):
    n = 0
    l, r = left, right

    while 1 <= r:
        #Get the midpoint
        m = (l+r)//2
        n = array[m][0]
        s = n[0]
        #If target is found, return m
        if target == s:
            return m
        #If target is not found, search left
        elif target < s:
            r = m-1
        #If target is not found, search right
        else:
            l = m+1

#Displaying a Welcome message
print('\t> > > Welcome to Lotto Drawing < < < ')
print('-------------------------------------------------')

#Initialise an empty list that will be used to store the player's 6 lucky numbers!
GameNum = []
#Initialise an empty list that will be used to store the player ID!
IDNum = []
#Initialise an empty list that will be used to store the player ID and player's 6 lucky numbers!
Lotto = []

for j in range (1,1001):
    #Resetting the IDNum array
    IDNum = []
    #Append the ID number to the list
    IDNum.append(j)
    #Resetting the GameNum array
    GameNum = []
    #Generating 6 distinct integer numbers from a barrel of 45 integer numbers
    for i in range (0,6):
        number = random.randint(1,45)
        #Check if this number has already been picked and ...
        while number in GameNum:
            # ... if it has, pick a new number instead
            number = random.randint(1,45)          
        #Append the unique number to the list
        GameNum.append(number)
        #Sort the list in ascending order by using the InsertionSort function
        MergeSort(GameNum) 

    #Merge two lists to one main array
    Lotto.append((list(IDNum),list(GameNum)))

#Print the Player ID and their corresponding Lotto Numbers 
for l in range (0,1000):
    print('Player ID : ',Lotto[l])

#Initialise an empty list that will be used to store the 6 lucky numbers!
WinNum = []

#Generating 6 distinct integer numbers from a barrel of 45 integer numbers
for i in range (0,6):
  number = random.randint(1,45)
  
  #Check if this number has already been picked and ...
  while number in WinNum:
    # ... if it has, pick a new number instead 
    number = random.randint(1,45)
  
  #Append the unique number to the list
  WinNum.append(number)

#Sort the list in ascending order by using the InsertionSort function
InsertionSort(WinNum) 

#Display the list on screen:
print("\nToday's Lottery Numbers are: ", WinNum)

class_1 = 0
class_2 = 0
class_3 = 0
class_4 = 0
count = 0

for i in range (0,1000):
    #Calling the function 1
    count = CommonValue (WinNum, Lotto[i][1])

    if count == 3:
        class_4 += 1
        count = 0

    elif count == 4:
        class_3 += 1
        count = 0
                    
    elif count == 5:
        class_2 += 1
        count = 0
                    
    elif count == 6:    
        class_1 += 1
        count = 0
    
#Displaying the statistic data
print('Class 1 : ', class_1)
print('Class 2 : ', class_2)
print('Class 3 : ', class_3)
print('Class 4 : ', class_4)

playerInput = int(input('Enter Player ID: '))
#Check if this Player ID is valid ...
while ((playerInput > len(Lotto)) or (playerInput < 0)):
    # ... if not, get the user input again
    print('Invalid Player ID! Please check again')
    playerInput = int(input('Enter Player ID: '))

#Calling the function 2    
search = BinarySearch (playerInput, Lotto, 0, len(Lotto))

compSearch = Lotto[search][1]
print(compSearch)

#Displaying the message of the player's winning status
status = CommonValue (WinNum, compSearch)
if status == 3:
    print('You are a 4th class winner, congratulations!')
elif status == 4:
    print('You are a 3rd class winner, congratulations!')
elif status == 5:
    print('You are a 2nd class winner, congratulations!')
elif status == 6:
    print('You win the game, congratulations!')
else:
    print('Thanks for playing lotto. Good luck next time')
























