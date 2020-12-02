import os
from flask_socketio import SocketIO
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))
db = SQLAlchemy()
socketio = SocketIO()


def create_app():
    chat = Flask(__name__)
    chat.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(basedir, '../chat.db')}"
    chat.config['SECRET_KEY'] = "b'\xed\x0e\xb9\x15`/2=\xbe\x18\r\x83e\xb1\xde\x9d'"

    from chat.views import bp_main
    from chat.events import ws

    chat.register_blueprint(bp_main)
    chat.register_blueprint(ws)

    db.init_app(chat)
    socketio.init_app(chat)

    migrate = Migrate(chat, db)

    return chat
