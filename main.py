from uuid import uuid4
from fastapi import FastAPI, Body, status
from fastapi.responses import JSONResponse, FileResponse
from src.Order import Order


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.id = str(uuid4())


people = [
    Person("Tom", 38),
    Person("Bob", 42),
    Person("Sam", 28)
]

orders = [
    Order()
]
 

def find_person(id):
   for person in people: 
        if person.id == id:
           return person


app = FastAPI()


@app.get("/")
async def main():
    return FileResponse("public/index.html")


@app.get("/api/orders")
async def get_orders():
    return orders


@app.get("/api/users")
def get_people():
    return people


@app.get("/api/users/{id}")
def get_person(id):
    person = find_person(id)
    print(person)
    
    if person is None:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND, 
            content={ "message": "Пользователь не найден" }
        )
    
    return person


@app.post("/api/users")
def create_person(data = Body()):
    person = Person(data["name"], data["age"])
    people.append(person)
    return person


@app.put("/api/users")
def edit_person(data = Body()):
    person = find_person(data["id"])
    # если не найден, отправляем статусный код и сообщение об ошибке
    if person == None: 
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND, 
            content={ "message": "Пользователь не найден" }
        )
    
    person.age = data["age"]
    person.name = data["name"]
    return person


@app.delete("/api/users/{id}")
def delete_person(id):
    # получаем пользователя по id
    person = find_person(id)
  
    # если не найден, отправляем статусный код и сообщение об ошибке
    if person == None:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND, 
            content={ "message": "Пользователь не найден" }
        )
  
    people.remove(person)
    return person