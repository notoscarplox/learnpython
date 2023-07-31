fruits = ["banana", "apple", "orange", "pineapple"]

print(fruits[0])      #This will print "banana"
print(fruits[0:2])    #This will print ["banana", "apple"] , Actually you dont need the 0
print(fruits[::2])    #This will print every two elements
print(fruits[::-1])   #This will print in reverse order
print(len(fruits))    #Lenght of the list which is 4



fruits[0]="peach"             #Will replace index 0 (apple) with peach
fruits.append("peach")        #Adds an element to the end of the list
fruits.remove("apple")        #Removes an element from the list
fruits.insert(1, "peach")     #Insert an element at given index, but dont replace the actual element
fruits.sort()                 #Sorts elements in alphabetical order
fruits.reverse()              #Reverse the order of the list
fruits.clear()                #Clears the list

fruits.index("apple")         #Returns the index of the element
fruits.count("banana")        #Returns how many elements are in the list
