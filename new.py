import jwt

u1 = {"_uid": "toby"}
print(jwt.encode(u1, "SECRET_KEY", algorithm="HS256"))

#eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJfdWlkIjoidG9ieSJ9._wMcSfhkAWqGrPy_UpfMaDQDYiWB_B7hr__FaLKGCY4