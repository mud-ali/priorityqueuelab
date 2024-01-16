from flask import Flask, request, redirect, url_for
import sqlite3
import json

from db_utils.db_init import create_tables
from db_utils.db_insert import insert_topic_details

app = Flask(__name__)

db = sqlite3.connect('db/debate.db')
create_tables(db)

@app.route("/submit_topic", methods=["GET","POST"])
def submit_topic():
    if request.method == "POST":
        topic_name = request.form['topic_name']
        topic_desc = request.form['topic_desc']
        q1 = request.form['q1']
        a1 = request.form['a1']
        q2 = request.form['q2']
        a2 = request.form['a2']
        q3 = request.form['q3']
        a3 = request.form['a3']

        insert_topic_details(db, topic_name, topic_desc, q1, a1, q2, a2, q3, a3)

        return redirect(url_for('/'), code=200)


@app.route("/store_opinion", methods = ["GET", "POST"])
def store_opinion():
    return

@app.route("/signin", methods=["POST"])
def sign_in():
    # todo check stuff
    return redirect(url_for("/"))

@app.route("/join", methods=["GET", "POST"])
def join_debate():
    # TODO  match people
    return redirect(url_for("/debate"))