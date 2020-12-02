from flask import Blueprint, render_template
from flask_socketio import emit

from chat import socketio

ws = Blueprint('ws', __name__, url_prefix='/chat')


@ws.route('/')
def chat():
    text = 'chat'
    return render_template('chat.html', text=text)


@socketio.on('message', namespace='/chat')
def handle_message(message):
    print('received message: ' + str(message))
    emit('connected', {'klucz': str(message)}, namespace='/chat', broadcast=True)
