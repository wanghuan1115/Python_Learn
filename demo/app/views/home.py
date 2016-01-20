#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import Blueprint, render_template
home = Blueprint('home', __name__, template_folder='templates')

class Home(object):
    def __init__(self):
        @home.route('/')
        def index():
            return render_template(getTemplate("index"))

        def getTemplate(str):
            return "home/" + str + ".html"
Home()