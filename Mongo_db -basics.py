
from pymongo import MongoClient
# Connecting to MongoDB
mc = MongoClient('localhost:27017')
print(mc)
# Connecting to MyDatabase in Mongo
db = mc.sathya
print(db)

# Reading all Documents from employee
res = db.employee.find()
for x in res:
    print(x)

# Printing all elements in employee data base 

res = db.employee.find()
for x in res:
    print(x)

#inserting one employee results 

d1 = {"_id":104,"name":"Krishna","salary":185000.00}
res = db.employee.insert_one(d1)
print(res)
print("Data Inserted")

# Updating data 

filter = {"_id":104}
update_data = {
        "$set":{"name":"Krishna Mohan","salary":115000.00}
      }
up = db.employee.update_one(filter,update_data)
print(up)
print("Employee Details Updated")

# update one 

res = db.employee.delete_one({"_id":104})
print(res)

MongoClient().sathya.employee.insert_one({"_id":1005,"name":"ABCD"})
print("Data Inserted")
 
