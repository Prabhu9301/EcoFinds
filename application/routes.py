from flask import render_template, request, redirect, url_for, flash, session
from main import app
from application.models import *
from functools import wraps
from datetime import datetime

def auth_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'user' not in session:
            return redirect(url_for('index'))
        return func(*args, **kwargs)
    return wrapper

# Landing Page
@app.route('/')
def index():
    return render_template('index.html')