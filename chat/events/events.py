from flask import Blueprint, render_template, session, url_for
from flask_socketio import emit, join_room, leave_room
from werkzeug.utils import redirect

from chat import socketio

ws = Blueprint('ws', __name__, url_prefix='/chat')


@ws.route('/')
def chat():
    name = session.get('name', '')
    room = session.get('room', '')
    if not name or not room:
        return redirect(url_for('main.home'))
    return render_template('chat.html')


@socketio.on('text', namespace='/chat')
def handle_message(message):
    room = session.get('room')
    emit('message', {'msg': f'{session.get("name")} : {message["msg"]} '}, namespace='/chat', broadcast=True)


# flask socket automatycznie emituje event connect

@socketio.on('joined', namespace='/chat')
def joined(message):
    room = session.get('room')
    join_room(room)
    emit('status', {'msg': f'{session.get("name")} has entered the room.'}, room=room)


@socketio.on('left', namespace='/chat')
def left(message):
    room = session.get('room')
    leave_room(room)
    emit('status', {'msg': f'{session.get("name")} has left the room.'}, room=room)
