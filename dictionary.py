"""Dictionery -> is a collection of (key:value) pairs
they are ordered and changable. no duplicates allowed

enclose with curly brackets like sets

"""

provinces = {
    "Western Cape": "Cape Town",
    "Kwazulu Natal": "Durban",
    "Eastern Cape": "Mtata",
    "Joburg": "Sandton"
    }

# print(dir(provinces)) # to see different attributes and methods of a dictionery
# print(provinces.get("Western Cape"))# to get the value from the dictonery


#use if statement to check if the province or city exist
"""if provinces.get("mtata"):
    print("city doesnt exist")
else:
    print("city exist")
     
    
"""

#use update nethod to add/insert a new key:value pair

# provinces.update ({"Limpompo": "mamjiji"})
# print(provinces)

# provinces.pop("Eastern Cape") # pop dont need a key tharefore no need for {}
# print(provinces)

# provinces.popitem() # removes the last item on the dictionary
# print(provinces)

"""to get all the keys but not the value"""
#  option 1
# key = provinces.keys()
# print(key)

# option 2
key = provinces.keys()
for key in provinces.keys():
    print(key)
