
from flask import Blueprint, request, render_template, url_for, redirect, abort
from .controller import controller

index = Blueprint("index", __name__)

@index.get("/")
def handle_index_view():
    return render_template("index.html")


api = Blueprint("api", __name__, url_prefix = "/api")

@api.get("/recommend/<username>")
def handle_get_recommended_items(username: str):
    recommended_items = controller.get_recommendation_for(username)
    if recommended_items != None:    
        return [{"title": i.title, "url": i.url} for i in recommended_items]
    
    return abort(400)

@api.put("/view")
def handle_view_item():
    username = request.form["username"]
    title = request.form["title"]
    if controller.update_view_history(username, title):
        return "OK"
    
    return abort(400)

@api.get("/users")
def handle_get_users():
    return controller.users

@api.get("/users/<username>")
def handle_change_user(username: str):
    if controller.set_current_user(username):
        return redirect(url_for("api.handle_get_recommended_items", username = controller.current_user))        

    return abort(400)    

@api.put("/users/<username>")
def handle_create_user(username: str):
    if controller.create_user(username):
        return redirect(url_for("api.handle_get_recommended_items", username = controller.current_user), code=303)
    
    return abort(400)