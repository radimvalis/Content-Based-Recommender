
from flask import Blueprint, render_template

index = Blueprint("index", __name__)

@index.get("/")
def handle_index_view():
    return render_template("index.html")