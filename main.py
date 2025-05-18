from flask import Flask

app = Flask(__name__)

import application.config

import application.models

import application.routes