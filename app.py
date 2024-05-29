from flask import Flask, render_template
import json

app = Flask(__name__)

posts = ["post1", "post2", "post3"]

@app.route("/")

def index():
    with open("data/Hostel.json", "r", encoding="utf-8") as f:
        datos = json.load(f)
    return render_template("index.html", datos=datos)

@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/contact/")
def contact():
    return render_template("contact.html")


#def index():
#    return render_template("index.html",num_posts=len(posts))

@app.route("/p/<string:slug>/")
def show_post(slug):
    return render_template("post_view.html", slug_title=slug)
    
@app.route("/admin/post/")
@app.route("/admin/post/<int:post_id>")
def post_form(post_id=None):
    return render_template("admin/post_form.html", post_id=post_id)