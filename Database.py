import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017")

mydb = myclient["python"]
mycollection = mydb["ATM"]

def insertData():
    pass

def selectData():
    result = mycollection.find()
    return result

def updateData(allreadyData , newData):
    freshData = {
        '$set':newData
    }
    mycollection.update_one(allreadyData , freshData)
    return True