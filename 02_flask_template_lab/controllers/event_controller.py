from flask import render_template, Blueprint, request
from models.event import Event
from models.event_list import events, add_new_event

events_blueprint = Blueprint("events", __name__)

@events_blueprint.route('/events')
def index():
    return render_template('index.jinja', title="Events list", events=events)

@events_blueprint.route('/events', methods=["POST"])
def add_event():
    print(request.form)
    name = request.form["name"]
    description = request.form["description"]
    date = request.form["date"]
    number_of_guests = request.form["number_of_guests"]
    room = request.form["room"]
    check_recurring = request.form["recurring"]
    if check_recurring == "Yes":
        recurring = True
    else:
        recurring = False
    new_event = Event(date, name, number_of_guests, room, description, recurring)
    add_new_event(new_event)
    return "Done"