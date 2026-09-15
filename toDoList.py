# To do list program
while True:

    inputToDoItem = input("Do you want to add a new To-Do item?\n(y/n): ")
    if inputToDoItem.lower() == "exit":
        break

    if inputToDoItem.lower() == 'y':

        newToDoItem = input("Enter your new To-Do item: ")
        file = open("to_do.txt", "a+", encoding="UTF-8")
        file.write(newToDoItem + "\n")
        file.close()

    elif inputToDoItem.lower() == 'n':

        inputToDoList = input("Do you want to list your To-Do items? (y/n): ")
        if inputToDoList.lower() == 'y':
            file = open("to_do.txt", "r+", encoding="UTF-8")
            itemList = file.read()
            print(itemList)
            file.close()

print("Thank you for using the To-Do program, come back again soon")