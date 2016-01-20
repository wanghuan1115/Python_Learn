from flask import Flask
from app.views.home import home
from app.views.plugin import plugin

app = Flask(__name__)
app.register_blueprint(home)
app.register_blueprint(plugin)
