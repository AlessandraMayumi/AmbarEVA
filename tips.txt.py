"""
http://apiadvisor.climatempo.com.br/doc/index.html
https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/

from app import db
db.create_all()

from app import db, create_app
def create_app():
    app = Flask(__name__)
    db.init_app(app)
    return app
db.create_all(app=create_app())
"""

# /cidade?id=3477
# http://apiadvisor.climatempo.com.br/api/v1/forecast/locale/3477/days/15?token=b22460a8b91ac5f1d48f5b7029891b53