from flask import Flask
from .config import Config
from .models import db
from flask_bootstrap import Bootstrap
from app.mysql_service import intert_producto #delete_producto,get_producto


def create_app():
    app = Flask(__name__)
    bootstrap = Bootstrap(app)

    db.init_app(app)

    app.config.from_object(Config)

    with app.app_context():
        db.create_all()

    #intert_producto(1,'Silla roble','silla pequeña','silla comoda')
    # delete_producto(1)
    # producto = get_producto(2)
    # productos = get_producto()
    return app