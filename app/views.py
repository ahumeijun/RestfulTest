# -*- coding: utf-8 -*-
#!/usr/bin/env python

from app import app
from flask import Flask

@app.route('/')
@app.route('/index')
def index():
    return "Hello, world!"

