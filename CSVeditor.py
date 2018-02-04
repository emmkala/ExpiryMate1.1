import urllib.request
import json
import csv
from userClass import User
from itemClass import Item

class CSVeditor():
    def checkExisting(self,name):
        try:
            with open(name+'_account_data.csv') as csvFile:
                readCSV = csv.reader(csvFile, delimiter=',')
                return True
        except FileNotFoundError:
            return False
        
    def createCSVHeader(self,name):
        with open(name, 'w', newline="") as csvFile:
            csvFileWriter = csv.writer(csvFile)
            csvFileWriter.writerow(['Item','Room Temperature','Refrigerator','Freezer at 0°F'])
        csvFile.close()

    def appendToCSV(self,col_one,col_two,col_three,col_four):
        with open('FoodList.csv', "a",newline="",encoding='utf-8' ) as csvFile:
            csvFileWriter = csv.writer(csvFile)
            csvFileWriter.writerow([col_one,col_two,col_three,col_four])
        csvFile.close()

    def fillFoodList(self):
        self.createCSVHeader('FoodList.csv')
        data = []
        response = urllib.request.urlopen("https://food.unl.edu/food-storage-chart-cupboardpantry-refrigerator-and-freezer")
        line = response.readline()
        foodItem = []
        
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
                    self.appendToCSV(foodItem[0],foodItem[1],foodItem[2],foodItem[3])
                    foodItem = []     
            line = response.readline()

    def createNewUser(self,userName):
        with open(userName + '_account_data.csv', "w",newline="") as csvFile:
            csvFileWriter = csv.writer(csvFile)
            csvFileWriter.writerow(['FoodItem','DaysLeft'])

    def loadUserData(self,userName):
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
    
    
    
    def addItem(self,user,item,storageMethod):
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
                        pass

    def wipe_before_save(self,userName):
        with open(userName + '_account_data.csv', "w",newline="") as csvFile:
            csvFileWriter = csv.writer(csvFile)
            csvFileWriter.writerow(['FoodItem','DaysLeft'])                   

    def saveBasket(self,listOfItems,userName):
        with open(userName + '_account_data.csv', "a",newline="",encoding='utf-8' ) as csvFile:
            csvFileWriter = csv.writer(csvFile)
            for item in listOfItems:
                csvFileWriter.writerow([item[0],item[1]])
        csvFile.close()

