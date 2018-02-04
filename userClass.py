from itemClass import Item

class User():

    def __init__(self,userName):
        self.userName = userName
        self.basket = []

    #Creates new object via food class 
    def newFoodItem(name,daysLeft):
        newItem = Item(name,daysLeft)
        return newItem
    
    #From loaded dictionary to object    
    def fileToObject(self,foodDict):
        for item in foodDict:
            self.basket.append(User.newFoodItem(item,foodDict[item]['days']))

    def addItem(self,name,days):
        self.basket.append(User.newFoodItem(name,days))
        
                          
    #Delet by loop return none
    def deleteItem(self,name):
       for item in basket:
            if item.getName() == name:
                self.basket.remove(item)

    def getTime(self,name):
        for item in self.basket:
            if item.getName() == name:
                return item.getExpire()
        return None

    def getName(self):
        return self.userName

    def getBasket(self):
        readBasket = []
        for item in self.basket:
            readBasket.append(item.getName())
        return readBasket

    

    
                      

    #Returns 2D list in form [[name,days],etc.] for ease of write to file
    def basketToList(self):
        saveBasket = []

        for item in self.basket:
            saveItem = []
            saveItem[0] = item.getName()
            saveItem[1] = item.getExpire()
            saveBasket.append(saveItem)
            

        return saveBasket
        
