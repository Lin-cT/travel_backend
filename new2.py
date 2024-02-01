import jwt

u1 = {"_uid":"lct"}
print(jwt.encode(u1, "SECRET_KEY", algorithm="HS256"))

#eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJfdWlkIjoibGN0In0.hA_QlRliwanl29bpcgKq0jdzKS-HLxozLB0bdb5Zq6E