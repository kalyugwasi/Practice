from passlib.context import CryptContext
pwd_context = CryptContext(schemes=['argon2'],deprecated='auto')
class Hash():
    def bcrypt(password:str):
        return pwd_context.hash(password)
    def verify(hash,plain):
        return pwd_context.verify(plain,hash)