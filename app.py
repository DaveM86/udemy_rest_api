'''
It's important the file name and the variable name are 'app' as when the command 'flask run' is passed the framework know what
you want to run.

This is being develop my following the udemy restful api course at https://www.udemy.com/course/rest-api-flask-and-python/learn/lecture/33781648?start=120#overview
'''

from flask import Flask

#running the app will make any end points that we define available to the client
app = Flask(__name__)

stores = [
    {
        "name": "My Store",
        "item":[
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
        "item":[
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

