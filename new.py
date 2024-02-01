from flask import current_app
import jwt

u1 = {"name":'Thomas Edison', "uid":'toby', "email":'toed@gmail.com', "password":'123toby'}
print(jwt.encode(u1, current_app.config["SECRET_KEY"], algorithm="HS256"))