from flask import Flask
from .blog.routes import blog
app=Flask(__name__)
app.register_blueprint(blog)

from app import routes

