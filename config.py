import os
from dotenv import load_dotenv
load_dotenv()
DB_URI=os.getenv("DB_URI")
API_URL=os.getenv("API_URL")