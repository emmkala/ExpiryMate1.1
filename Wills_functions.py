import urllib.request
import json
import csv
from userClass import User
from itemClass import Item

def createCSVHeader(fileName):
    with open(fileName, "w",newline="") as csvFile:
        csvFileWriter = csv.writer(csvFile)
        csvFileWriter.writerow(['Item','Room Temperature','Refrigerator','Freezer at 0°F'])

#Appends a row of data about a post to the end of the csv file containing status/post information
def appendToCSV(col_one,col_two,col_three,col_four):
    
    with open('FoodList.csv', "a",newline="",encoding='utf-8' ) as csvFile:
        csvFileWriter = csv.writer(csvFile)
        csvFileWriter.writerow([col_one,col_two,col_three,col_four])
    csvFile.close()

#Crawls page for list of common expiration times
def fillFoodList():
    createCSVHeader('FoodList.csv')
    data = []
    response = urllib.request.urlopen("https://food.unl.edu/food-storage-chart-cupboardpantry-refrigerator-and-freezer")
    line = response.readline()
    foodItem = []
    count = 1
    
    while len(line) != 0:
        textLine = line.decode('utf-8')
        #Check to see if the element is a food item
        if textLine[0:4] == "<td>" and textLine[4:11] != "<span c":
            cleanWord = []
            #Taking the tags away from the elements
            for letter in textLine[4::]:
                if letter != '<':
                    cleanWord.append(letter)
                else:
                    break
                data = ''.join(cleanWord)
                if data == '&nbsp;':
                    data = ""
            foodItem.append(data)
            if len(foodItem) == 4:
                appendToCSV(foodItem[0],foodItem[1],foodItem[2],foodItem[3])
                foodItem = []
            count = count + 1    
        line = response.readline()

#Creates a new empty CSV for a new user
def createNewUser(userName):
    with open(userName + '_account_data.csv', "w",newline="") as csvFile:
        csvFileWriter = csv.writer(csvFile)
        csvFileWriter.writerow(['FoodItem','DaysLeft'])

#Returns a dictionary of dictionaries where each sub dictionary is a food item
def loadUserData(userName):
    userFoodList = {}
    with open(userName + '_account_data.csv') as csvFile:
        readCSV = csv.reader(csvFile, delimiter=',')
        for row in readCSV:
            itemData = {}
            foodName = row[0]
            daysLeft = row[1]
            itemData['daysLeft'] = daysLeft
            userFoodList[foodName] = itemData
    return userFoodList

#Returns None if the item to add is not in our list    
def addItem(user,item,storageMethod):
    with open('FoodList.csv') as csvFile:
        readCSV = csv.reader(csvFile, delimiter=',')
        for row in readCSV:
            if row[0] == item:
                if storageMethod == 'room_temperature':
                    column = 1
                elif storageMethod == 'refrigerated':
                    column = 2
                elif storageMethod == 'frozen':
                    column = 3
                else:
                    print("Storage method did not match with conditionals")
                    return None
                if (row[column].split(" "))[1] == "week" or row[column][1] == "weeks":
                    user.addItem(item,int(row[column][0]) * 7)
                elif (row[column].split(" "))[1] == "day" or row[column][1] == "days":
                    user.addItem(item,int(row[column][0]))
                elif (row[column].split(" "))[1] == "month" or row[column][1] == "months":
                    user.addItem(item,int(row[column][0]) * 30)
                elif (row[column].split(" "))[1] == "year" or row[column][1] == "years":
                    user.addItem(item,int(row[column][0]) * 365)
                else:
                    #print "Something went wrong with converting week/day/month/year"
                    pass
                
def wipe_before_save(userName):
    with open(userName + '_account_data.csv', "w",newline="") as csvFile:
        csvFileWriter = csv.writer(csvFile)
        csvFileWriter.writerow(['FoodItem','DaysLeft'])                   

def saveBasket(listOfItems,userName):
    with open(userName + '_account_data.csv', "a",newline="",encoding='utf-8' ) as csvFile:
        csvFileWriter = csv.writer(csvFile)
        for item in listOfItems:
            csvFileWriter.writerow([item[0],item[1])
    csvFile.close()

