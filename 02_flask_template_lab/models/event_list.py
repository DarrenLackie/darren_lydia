from models.event import Event
import datetime


event1 = Event(datetime.date(2020, 5, 17), "Birthday Party", 10, "The big room", "Darren's birthday, don't forget to bring a present.", True)
event2 = Event(datetime.date(2020, 6, 18), "Birthday Curry", 4, "Lydia's kitchen", "Lydia's birthday, bring a bottle.", True)

events = [event1, event2]

def add_new_event(event):
    events.append(event)