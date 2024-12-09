
from flask import render_template, request, redirect, url_for
from comms import comments
@comments.route("/")
def landing():
    return "Hello world!"
