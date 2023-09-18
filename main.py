from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


@app.get('/')  # Decorate
               # get : http Method
def index():   ##Decorator function line 7 & 8
    return {'data': 'Blog list'}

@app.get('/blog')
def index(limit=10, Published: bool = 'Published'):  ## Limit is querry Parameter
    ## Here defautlt value is mentioned GET link http://127.0.0.1:8000/blog
    if Published:
        return {'data': f'{limit} {Published}Blog list'}
    else:
        return{'data': f'{limit} Blog list'}


@app.get('/blog/tshirts')
def Tshirt():
    return {'data': 'All tshirts'}

@app.get('/blog/{id}') ##dynamic variable ID ## Path Parameter
def show(id:int):
    return {'data-1':id}

@app.get('/blog/{id}/comments')
def comments(id:int):
    return {'data':f'{id} the customer is happy'}


## Post Method - To update document in data base

class Blog(BaseModel):

    title = str
    Body = str
    Published = Optional[bool]

@app.post('/blog_post')
def create_blog(request:Blog):
    return {'data': f'Blog is created with {request.title}'}









