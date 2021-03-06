# -*- coding: utf-8 -*-
#!/usr/bin/env python

from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

from app import views, models
