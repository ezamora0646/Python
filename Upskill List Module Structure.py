# Module 1
list = ["Intro", "Variables in Python", "Python operators", "Conditionals", "Functions", "Loops",
        "Python Modules", "Lists and Dictionaries"]
#print("I have finished watching these videos: " + sep=" " +",".join(list))
#print("I have finished watching these videos: "+",".join(list), sep=" ")
#print("I have finished watching these videos: "+ " ".join(list)) #removes commas, adds space between items
print("I have finished watching these videos: "+ ", \n".join(list)) #keeps commas, adds space
#join functions NEEDS TO BE called on a string

# Module 2
list2 = ["Lambda Functions", "Exceptions Handling", "Working w User Input", "Handling External Files pt 1",
         "Handling External Files Pt2", "Python + SQL Databases", "SQL: Inserting Data",
         "SQL: Retrieve & Manipulate Data"]
print("These are the meat and potatoes: \n" + ", \n".join(list2) + "\n ...watch on YouTube")