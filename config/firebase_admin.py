import firebase_admin
from firebase_admin import credentials
from config.settings import FIREBASE_SERVICE_ACCOUNT_PATH

cred = credentials.Certificate(FIREBASE_SERVICE_ACCOUNT_PATH)
default_app = firebase_admin.initialize_app(cred)
