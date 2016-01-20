from flask import Blueprint, render_template

plugin = Blueprint('plugin', __name__, template_folder='templates')

class Plugin(object):
    def __init__(self):
        @plugin.route('/plugin/')
        def index():
            return render_template(getTemplate("index"))

        @plugin.route('/plugin/add')
        def add():
            return render_template(getTemplate("add"))

        def getTemplate(str):
            return "plugin/" + str + ".html"
Plugin()