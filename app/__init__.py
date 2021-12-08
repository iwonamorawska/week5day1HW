from flask import Flask
from config import Config

from .blog.routes import blog
from .auth.routes import auth

from .models import db

from flask_migrate import Migrate

app=Flask(__name__)

app.register_blueprint(blog)
app.register_blueprint(auth)

app.config.from_object(Config)

db.init_app(app)

migrate= Migrate(app, db)

from app import routes
from app import models
