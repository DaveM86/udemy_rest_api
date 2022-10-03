'''
It's important the file name and the variable name are 'app' as when the command 'flask run' is passed the framework know what
you want to run.

This is being develop my following the udemy restful api course at https://www.udemy.com/course/rest-api-flask-and-python/learn/lecture/33781648?start=120#overview
'''

from flask import Flask, request

#running the app will make any end points that we define available to the client
app = Flask(__name__)

stores = [
    {
        "name": "My Store",
        "items":[
            {
                "name": "chair",
                "price": 15.99
            },
            {
                "name": "table",
                "price": 975.00
            }
        ]
    },
    {
        "name": "My 2nd store",
        "items":[
            {
                "name": "charcole",
                "price": 15.99
            },
            {
                "name": "BBQ",
                "price": 975.00
            }
        ]
    }
]


#create an endpoint the '/store' is the endpoint and func associated the EP is 'get_stores'
@app.get("/store")
def get_stores():
    return {"stores": stores}

#using the same endpoint but to post to.
@app.post("/store")
def create_store():
    #import the request module to interperate the json data in the payload
    request_data = request.get_json()
    #create a variable to sore the data from the payload
    new_store = {"name": request_data["name"], "items": []}
    #add the data to our list in memory
    stores.append(new_store)
    #return our confrimation and response code 201(added)
    return new_store, 201

#adding an item and details of the store name in the string
#use the crocidiles clips to define a variable in the url
#the /item part of the url will always remain /item
@app.post("/store/<string:name>/item")
def create_item(name):
    #use the request module to interperate the json data in the payload
    request_data = request.get_json()
    #loop throught the stores to match the name in the url
    for store in stores:
        if store["name"] == name:
            #create a variable to hold the json data
            new_item = {"name": request_data["name"], "price": request_data["price"]}
            #append it to "items" in the dict if the stores match
            store["items"].append(new_item)
            #return the conframation and the http code
            return new_item, 201
    #if no stores match return the error massage and http code
    return {"message": "Store not found"}, 404