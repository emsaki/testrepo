# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    names = ["Mariki Edward", "Baraka Shabaan", "Mbaraka Uhinga", "Meckson Charles"]
    return render_template("index.html", names=names)


@app.route("/home")
def home():
    
    return "This is home page"