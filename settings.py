import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("baseUrl")

ADMIN_EMAIL = os.getenv("adminEmail")
ADMIN_PASSWORD = os.getenv("adminPassword")

USER_EMAIL = os.getenv("userEmail")
USER_PASSWORD = os.getenv("userPassword")
