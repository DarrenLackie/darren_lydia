from flask import render_template, Blueprint, request
from models.event import Event
from models.event_list import events, add_new_event
import datetime

events_blueprint = Blueprint("events", __name__)

@events_blueprint.route('/events')
def index():
    return render_template('index.jinja', title="Events list", events=events)

@events_blueprint.route('/events', methods=["POST"])
def add_event():
    print(request.form)
    name = request.form["name"]
    description = request.form["description"]
    date_to_split = request.form["date"]
    number_of_guests = request.form["number_of_guests"]
    room = request.form["room"]
    check_recurring = request.form["recurring"]
    if check_recurring == "Yes":
        recurring = True
    else:
        recurring = False
    date_elements = date_to_split.split("-", 3)
    date_year = int(date_elements[0])
    date_month = int(date_elements[1])
    date_day = int(date_elements[2])
    new_event = Event(datetime.date(date_year, date_month, date_day), name, number_of_guests, room, description, recurring)
    add_new_event(new_event)
    return "Done"