from passlib.context import CryptContext
from passlib.exc import UnknownHashError

# Configuração simplificada do CryptContext
pwd_context = CryptContext(
    schemes=["bcrypt"],
    bcrypt__default_rounds=12
)

def get_password_hash(password: str) -> str:
    try:
        return pwd_context.hash(password)
    except Exception as e:
        print(f"Error hashing password: {e}")
        raise

def verify_password(password: str, hashed_password: str) -> bool:
    try:
        return pwd_context.verify(password, hashed_password)
    except UnknownHashError:
        print("Unknown hash format")
        return False
    except Exception as e:
        print(f"Error verifying password: {e}")
        return False