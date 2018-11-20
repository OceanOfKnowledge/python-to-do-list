#Import time module for checking TO DO Time and sleeping
import time
#Import winsound to play alert sound
import winsound

#Function that accepts To Do Items and adds to dictionary
def enterToDo():
    toDoDict = {}
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
#Main Program
if __name__ == '__main__':
    #Call function to accept toDoList into dictionary
    toDoDict = enterToDo()
    #Loop infinitely while there is an item in toDoDict
    while(len(toDoDict) > 0):
        #Call function to check if it is time for any toDo
        toDoNow = checkToDo(toDoDict)
        #If no To Do is returned, wait for 1 minute (60s) and continue the loop
        if(len(toDoNow) == 0):
            time.sleep(60)
            continue
        #If a To Do item is returned, play sound and display alert
        else:
            print("TO DO ALERT")
            #Save To Do item Name
            keyVal = list(toDoNow.keys())[0]
            #Play alert sound
            winsound.PlaySound("alert.wav", winsound.SND_FILENAME)
            #Print To Do Item
            for key in toDoNow:
                print("The time is {}:{}.\n It is time for {} - {}".format(toDoNow[key][0], toDoNow[key][1], keyVal, toDoNow[key][2]))
            continue
    #If there is no item in To Do List
    print("Your TO DO LIST is empty!")
    
    
