
from flask import render_template, request, redirect, url_for
from comms import comments
from redis import Redis

@comments.route("/")
def landing():
    r = Redis(decode_responses=True)
    students = r.smembers("students")
    return render_template("comments.html", students=sorted(list(students)))


@comments.route("/add_comment", methods=["POST"])
def add_comment():
    comment = request.form['comment']
    student = request.form['student']
    r = Redis(decode_responses=True)
    r.rpush(f"feedback:{student}", comment)
    return redirect(url_for('landing'))

