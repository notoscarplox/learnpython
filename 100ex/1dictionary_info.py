capitals = {
    "Japan": "Tokio",
    "USA": "Washington",
    "Mexico": "MexicoCty"
    }



capitals.get("Japan")                       #Will return the VALUE of the key

capitals.update({"Germany": "Berlin"})      #Adds a key and its value to dictionary
capitals.update({"Japan": "Uwo"})           #But you can also update a VALUE of a key

capitals["Germany"] = "Berlin"              #Also you can update/add a key

capitals["Germany"] = "Berlin"              #Another way to add a key and value, and you can modify the value of a key also

capitals.pop("Japan")                       #Removes the key and its value from dictionary
capitals.popitem()                          #Removes the last key in the dictionary




capitals.keys()                             #Returns all KEYS as a Dictionary View Object

for key in capitals.keys():                 #This will print the keys individually
    print(key)


capitals.values()                           #Returns VALUES as a Dictionary View Object

for value in capitals.values():             #This will print the values individually
    print(value)


capitals.items()                            #Returns a Dictionary with toples

for key, value in capitals.items():         #Prints the keys with respective values of a dictionary
    print(f"{key}: {value}")



