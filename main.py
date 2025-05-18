from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# App Configuration
import application.config

# Initialize DB and Models
from application.models import *

if __name__ == "__main__":
    app.run()