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