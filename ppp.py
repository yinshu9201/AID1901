from pymongo import MongoClient

#创建数据链接
conn = MongoClient('localhost',27017)

#创建数据库对象
db = conn.stu

#创建集合对象
myset = db.class0              

# print(dir(myset))
# myset.insert_one({'name':'大冬///////瓜', 'work':'吃挂男' },{'name':'午夜屠猪男', 'work':'杀猪' })


myset.remove({'sex':None})

#cursor = myset.find({},{'_id':0})
#for循环比那里游标查找内容
# for i in cursor:
#     print(i)
# print(cursor.next())      

# for i in cursor([('name',1),('singer')]):
#     print(i)



#关闭数据链接
conn.close()
