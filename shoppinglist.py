items = [] # new list to store the users items

def addItem(): #adding items to the "items" list
    while True: # continue to add items
        newItem =input("What would you like to add to your cart? press 'q' to quit or 'r' to remove. If you want to see all of the items in your list, enter 'show' : ")
        if newItem == 'q':
            break #exit
        elif newItem.lower() == 'r':
            removeItem() #run remove func. 
        elif newItem == "show":
            showMe()
        else:
            items.append(newItem)#add items to items list
        print (f'{newItem} added. Here are the items in your cart {items}')# add items to list and display list

def removeItem():
   while True:
       remove = input(f"What item would you like to remove?. press 'q' to quit or 'show' to see your cart. ") #getting item to be removed
       
       print(f"{remove} removed")#confirmation of removal of item
       if remove == "q":
           break
       elif remove =="add":
           addItem()
       elif remove == "show":
           showMe()
       else:
           items.remove(remove) #remove the first occurence of item

def showMe():
    for index, item in enumerate(items):
        print (f"Cart item number {index+1}:{item}")
    next_option = input("Would you like to add more items (add), or remove more items(remove)")
    if next_option == "add":
        addItem()
    elif next_option == "remove":
        removeItem()
    else:
        print("error please enter a valid response.")

addItem()
