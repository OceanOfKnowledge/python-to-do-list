#Import time module for checking TO DO Time and sleeping
import time
#Import winsound to play alert sound
import winsound
#import Threading module to run ToDo cycle concurrently
import threading

#Function that accepts To Do Items and adds to dictionary
def enterToDo():
    toDoDict = {}
    print("Add new ToDo item")
    while(True):
        item = input("Enter ToDo Item: ")
        if(item == "q"):
            break
        toDoTime = input("Enter ToDo Time (hh:mm): ")
        if(toDoTime == "q"):
            break
        toDoDesc = input("Enter ToDo Description: ")
        if(toDoDesc == "q"):
            break
        try:
            hh, mm = toDoTime.split(":")
            hh = int(hh)
            mm = int(mm)
        except:
            print("Your time format should be hh:mm 24-hour format")
        toDoDict[item] = [hh, mm, toDoDesc]
        print("Item added to TODO List. Enter again or 'q' to quit")
    return toDoDict

def addToDo(toDoDict):
    print("Add new ToDo item")
    while(True):
        item = input("Enter ToDo Item: ")
        if(item == "q"):
            break
        toDoTime = input("Enter ToDo Time (hh:mm): ")
        if(toDoTime == "q"):
            break
        toDoDesc = input("Enter ToDo Description: ")
        if(toDoDesc == "q"):
            break
        try:
            hh, mm = toDoTime.split(":")
            hh = int(hh)
            mm = int(mm)
        except:
            print("Your time format should be hh:mm 24-hour format")
        toDoDict[item] = [hh, mm, toDoDesc]
        print("Item added to TODO List. Enter again or 'q' to quit")
    return toDoDict

#Function that checks if the time now equals time for an item in To Do List
def checkToDo(toDoList):
    now = time.gmtime()
    toDoNow = {}
    keysList = toDoList.keys()
    keyList = list(keysList)
    for keys in range(0,len(keyList)):
        if(toDoList[keyList[keys]][0] == now[3] and toDoList[keyList[keys]][1] == now[4]):
            toDoNow[keyList[keys]] = toDoList[keyList[keys]]
            del toDoList[keyList[keys]]
    return toDoNow

#Function to remove item from ToDo List
def removeToDo(toDoList):
    #collect all items(keys) in a list
    itemList = list(toDoList.keys())
    #List all items in ToDo List
    print("TODO LIST:")
    for i in range(0,len(itemList)):
        print("{} - {}:{}. {}".format(itemList[i],
                                      toDoList[itemList[i]][0],
                                      toDoList[itemList[i]][1],
                                      toDoList[itemList[i]][2]))
    while(True):
        itemToDel = input("Enter item to delete ('q' to quit deleting): ")
        if(itemToDel == "q"):
            break
        elif(itemToDel in itemList):
            del toDoList[itemToDel]
            print("{} deleted from ToDo List".format(itemToDel))
        else:
            print("Item does not exist in ToDo List")
def toDoCycle(toDoDict):
    while(len(toDoDict) > 0):
        #Call function to check if it is time for any toDo
        toDoNow = checkToDo(toDoDict)
        #If no To Do is returned, wait for 1 minute (60s) and continue the loop
        if(len(toDoNow) == 0):
            print("Waiting for next ToDo item...")
            time.sleep(25)
            continue
        else:
            print("TO DO ALERT")
            #Save To Do item Name
            keyVal = list(toDoNow.keys())[0]
            #Play alert sound
            winsound.PlaySound("alert.wav", winsound.SND_FILENAME)
            #Print To Do Item
            for key in toDoNow:
                print("The time is {}:{}.\n It is time for {} - {}".format(toDoNow[key][0],
                                                                       toDoNow[key][1],
                                                                       keyVal,
                                                                    toDoNow[key][2]))
    #If there is no item in To Do List
    print("Your TO DO LIST is empty!")

def toDoManager(toDoDict):
    while(True):
        print("\nTODO is running.\nYou can manage list while program is running!")
        print("Type 'add' to Add ToDo item to List. Type 'del' to Delete item from list. Type 'q' to quit")
        addDel = input("Add or Delete ToDo Entry?(add/del) ")
        if(addDel == "q"):
            break
        elif(addDel == "del"):
            removeToDo(toDoDict)
        elif(addDel == "add"):
            toDoDict = addToDo(toDoDict)
        else:
            print("Invalid input! Try again")

#Main function
def Main():
    #Call function to accept toDoList into dictionary
    toDoDict = enterToDo()
    #Declare cycle thread
    toDoThread = threading.Thread(target=toDoCycle, args=(toDoDict,))
    toDoManagerThread = threading.Thread(target=toDoManager, args=(toDoDict,))
    #Start ToDo Thread
    toDoThread.start()
    #Start ToDo manager
    toDoManagerThread.start()
    #Join ToDo Thread to main thread
    toDoThread.join()

if __name__ == '__main__':
    Main()
                                        
    
    
    
