from pydantic import BaseModel


class Register(BaseModel):
    name :str
    lastname :str
    email :str
    password :str

class Login(BaseModel):
    email:str
    password :str