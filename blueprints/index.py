from flask import Blueprint

index_views = Blueprint('index_views', __name__, template_folder='templates')

@index_views.route('/')
def index():
    return "<html><body><p style='color: #454545'>Index</p></body></html>"

@index_views.route('/testing')
def testing():
    return 'this is a new route we made'