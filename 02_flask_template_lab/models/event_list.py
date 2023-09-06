from models.event import Event

event1 = Event("2nd February", "Birthday Party", 10, "The big room", "Darren's birthday, don't forget to bring a present.", True)
event2 = Event("28th August", "Birthday Curry", 4, "Lydia's kitchen", "Lydia's birthday, bring a bottle.", True)

events = [event1, event2]

def add_new_event(event):
    events.append(event)