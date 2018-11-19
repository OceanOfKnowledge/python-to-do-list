#Python To_Do List Console Application

#import time Module for checking time, and for delaying execution for 1 minute
import time
#import winsound Module for playing alert sound
import winsound
#Initialize list dictionary
to_do_list = {}
#create function to check what to do now!
def isTime(listDict,timeNow):
    for n in listDict:
        if((timeNow[3] == int(listDict[n][0])) and (timeNow[4] == int(listDict[n][1]))):
            return [True, n, listDict[n]]            
        else:
            return [False]
#create infinite loop
while(True):
    #Receive To Do item, time, and description
    newItem = input("Please enter new ToDo Item: ")
    if(newItem == "finished"):
        break
    newItemTime = input("Please enter time for new ToDo Item (hh:min): ")
    if(newItemTime == "finished"):
        break
    newItemDesc = input("Describe new ToDo Item: ")
    if(newItemDesc == "finished"):
        break
    #Try except block to separate time into hours and minutes
    try:
        hh, mm = newItemTime.split(":")
    except:
        print("The time format should be hh:min (24 hour format)")
        continue
    #push into To Do List
    to_do_list[newItem] = [hh, mm, newItemDesc]
#Print all To Do Items
for keys in to_do_list:
    print(keys + ": "+ to_do_list[keys][2])
    print("Time:", to_do_list[keys][0], to_do_list[keys][1])
#Infinite loop to check time for next To Do
while(True):
    #Check time now
    now = time.gmtime()
    #check which item time matches now
    checker = isTime(to_do_list, now)
    #Alert To Do item when time is up
    if(checker[0] == True):
        #Play sound
        #winsound.PlaySound("timeup", winsound.SND_FILENAME)
        #Print To Do Message
        print("The time is", checker[2][0], ":", checker[2][1])
        print("It is time for", checker[1], checker[2][2])
        break
    else:
        #Sleep for 1 minute and check again
        time.sleep(60)
        continue
