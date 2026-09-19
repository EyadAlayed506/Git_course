from fastapi import FastAPI, HTTPException, status
from enum import Enum
from pydantic import BaseModel
 
app = FastAPI()
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
@app.get("/")
def home():
    return {"massage":"hello world"}


@app.get("/{item_id}")
def get_item(item_id:int):
    return {"item_id":item_id}  


from fastapi import FastAPI

app = FastAPI()
# below it reads in order so for ex."http://127.0.0.1:8000/users/me"
#the ouput is userid:me
# @app.get("/users/{user_id}")
# async def read_user(user_id: str):
#     return {"user_id": user_id}

# @app.get("/users/me")
# async def read_user_me():
#     return {"user_id": "the current user"}
#therefore we use this order


@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}



class ModelName(str,Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet: ##model_anme is enum object so we compare with object
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":#string==stirng
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}



@app.get("/items/{item_id}")
def get_item_id(item_id:str,q:str|None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}


@app.post("/items/")
def create_item(item:Item):
    return item


@app.put("/items/{item_id}")
async def update_item(item_id:int,item:Item,q:str|None=None):
    result={"item_id":item_id,**item.model_dump()}
    if q:
        result.update({"q":q})
    return result