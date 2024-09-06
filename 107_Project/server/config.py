import pymongo
import certifi

con_str="mongodb+srv://test:test@zeri.udvhu.mongodb.net/?retryWrites=true&w=majority&appName=zeri"
client = pymongo.MongoClient(con_str, tlsCAfile=certifi.where())
db=client.get_database("organika")