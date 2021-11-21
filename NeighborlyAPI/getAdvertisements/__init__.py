import azure.functions as func
import pymongo
import json
from bson.json_util import dumps

def main(req: func.HttpRequest) -> func.HttpResponse:

    try:
        url = "mongodb://project2udacity:YpZnmz1FaNkguh1W4AkRRI7B642ExmXfAe1keeBHi2grZzsdIXxCvTodYuH2mLIDpy3AlcqXfJhqqF2wPOUyGA==@project2udacity.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@project2udacity@"
        client = pymongo.MongoClient(url)
        database = client['neigbourlymongodb']
        collection = database['advertisements']


        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8')
    except:
        print("could not connect to mongodb")
        return func.HttpResponse("could not connect to mongodb",
                                 status_code=400)

