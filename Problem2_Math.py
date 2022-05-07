
from flask import Flask,render_template, request
import statistics
import numpy as np


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/min",methods = ['GET','POST'])
def minimum():
    if request.method == 'POST':
        mylist = request.form["nums"]
        quant = request.form["quant"]
        my_list = mylist.split(",")
        del my_list[int(quant):]
        result = min(map(int, my_list))
        return render_template("min.html",nums = result) 

@app.route("/max",methods = ['GET','POST'])
def maximum():
    if request.method == 'POST':
        mylist = request.form["nums"]
        quant = request.form["quant"]
        my_list = mylist.split(",")
        del my_list[int(quant):]
        result = max(map(int, my_list))
        return render_template("max.html",nums = result) 

@app.route("/avg",methods = ['GET','POST'])
def average():
    if request.method == 'POST':
        mylist = request.form["nums"]
        my_list = mylist.split(",")
        result = sum(map(int, my_list))/ len(my_list)
        return render_template("avg.html",nums = result) 

@app.route("/median",methods = ['GET','POST'])
def median():
    if request.method == 'POST':
        mylist = request.form["nums"]
        my_list = mylist.split(",")
        result = statistics.median(map(int, my_list))
        return render_template("median.html",nums = result) 

@app.route("/percentile",methods = ['GET','POST'])
def percentile():
    if request.method == 'POST':
        quant = request.form["quant"]
        mylist = request.form["nums"]
        my_list = list(map(int,mylist.split(","))) 
        result = np.percentile(my_list, int(quant))
        return render_template("percentile.html",nums = result, quant = quant) 

if __name__ == '__main__':
    app.run()
