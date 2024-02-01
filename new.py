import jwt

u1 = {"_uid": "toby", "password": "123toby"}
print(jwt.encode(u1, "SECRET_KEY", algorithm="HS256"))