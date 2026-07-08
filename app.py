from flask import Flask, render_template, request, redirect
from pymongo import MongoClient
import os

app = Flask(__name__)

client = MongoClient("mongodb+srv://ragavharish749_db_user:TdmMgQrqTLqUQKX6@student-db.xzn9oa4.mongodb.net/?appName=student-db")

db = client["student_db"]
students = db["students"]

@app.route("/")
def home():
    data = students.find()
    return render_template("index.html", students=data)

@app.route("/add", methods=["POST"])
def add():
    name = request.form["name"]

    students.insert_one({
        "name": name
    })

    return redirect("/")

@app.route("/delete/<name>")
def delete(name):
    students.delete_one({"name": name})
    return redirect("/")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)