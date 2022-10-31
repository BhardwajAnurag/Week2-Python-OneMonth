ans = input("Do you wish to hear a joke? \n")
#one way is to make lists instead of using many OR comparison
list1 = ["Yes","yes","y","Y"]
if ans in list1:
    print("I'm agianst picketing but I don't know how to show it")
#this way we can just match N and remove list altogether and also lowercase everything so no duplicates
elif "n" in ans.lower():
    print("Fine")
else:
    print("I do not understand")