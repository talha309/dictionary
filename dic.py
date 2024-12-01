# Basic Operations
# Create a dictionary student with keys: name, age, and grade. Assign them appropriate values.
student={
    "name":"Anas Ishaq",
    "age":"18",
    "grade":"A"
}

# Access the value of the key grade in the student dictionary.
print (student["grade"])
# Add a new key city to the student dictionary and set its value to "New York".
student ["city"] = "New York"
# Update the value of the age key in the student dictionary to 20.
student["age"] ="20"
# Remove the key city from the student dictionary.
del student ["city"]
# Iterating through Dictionaries
# Iterate through the dictionary student and print all keys.
for each_keys in student.keys():
    print ( each_keys)
# Iterate through the dictionary student and print all values.
for each_values in student.values():
    print ( each_values)
# Iterate through the dictionary student and print all key-value pairs in the format key: value.
for keys,values in student.items():
    print (keys,":",values)
# Check if the key grade exists in the student dictionary and print True or False.
if  "grade" in student:
    print ("true")
else:
    print ("false")
# Count the total number of keys in the student dictionary.
print (len(student))
# Advanced Dictionary Usage
# Merge the following two dictionaries and print the result:
dict1 = {'a': 1, 'b': 2}  
dict2 = {'c': 3, 'd': 4}  
dict1.update(dict2)
print ( dict1)

# Create a dictionary from a list of tuples: [('name', 'Alice'), ('age', 25), ('city', 'Paris')].
dictionary_list = [{'name':'alice'},{'age':'25'},{'city':'Paris'}]
print (dictionary_list)

# Sort the keys of the dictionary {'z': 1, 'a': 2, 'c': 3} in ascending order and print the sorted dictionary.
dictionary = {'z': "1", 'a': "2", 'c': '3'}
sorted_dictionary={keys:dictionary[keys] for keys in sorted(dictionary)}
print (sorted_dictionary)

# Reverse the dictionary {'a': 1, 'b': 2, 'c': 3} so that keys become values and values become keys.
dictionary1 = {'a': '1', 'b': '2', 'c': "3"}
reversed_dict= {values : keys for keys , values in dictionary1.items()}
print (reversed_dict)
# Write a Python function to check if two dictionaries are identical (contain the same key-value pairs).
def dictionary_function(dic3,dic4):
    dict5 = dic3 is dic4 
    return dict5
dict1={'a':'34','b':'45'}
dict2={'a':'34','b':'54'}
print  (dictionary_function(dict1,dict2))