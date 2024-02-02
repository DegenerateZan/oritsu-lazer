from dotenv import load_dotenv
import os
from enum import Enum

class ENV(Enum):
    DB_HOST = 'DB_HOST'
    DB_USER = 'DB_USER'
    DB_PASSWORD = 'DB_PASSWORD'
    DB_DATABASE = 'DB_DATABASE'

    @classmethod
    def get(cls:Enum, var:Enum) -> str:
        """
        Retrieves the value of the specified environment variable.
        """
        return os.getenv(var.value)

load_dotenv()