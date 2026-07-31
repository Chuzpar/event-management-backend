from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from . import db
from .models import Event

main = Blueprint("main", __name__)


@main.route("/")
def home():
    return jsonify({"message": "Event Management API is running"})


# GET all events
@main.route("/events", methods=["GET"])
def get_events():
    events = Event.query.all()

    event_list = []

    for event in events:
        event_list.append({
            "id": event.id,
            "title": event.title,
            "description": event.description,
            "date": event.date,
            "location": event.location
        })

    return jsonify(event_list)


# GET one event
@main.route("/events/<int:id>", methods=["GET"])
def get_event(id):

    event = Event.query.get_or_404(id)

    return jsonify({
        "id": event.id,
        "title": event.title,
        "description": event.description,
        "date": event.date,
        "location": event.location
    })


# CREATE event
@main.route("/events", methods=["POST"])
@jwt_required()
def create_event():

    data = request.get_json()

    event = Event(
        title=data["title"],
        description=data["description"],
        date=data["date"],
        location=data["location"]
    )

    db.session.add(event)
    db.session.commit()

    return jsonify({"message": "Event created successfully"}), 201


# UPDATE event
@main.route("/events/<int:id>", methods=["PUT"])
@jwt_required()
def update_event(id):

    event = Event.query.get_or_404(id)

    data = request.get_json()

    event.title = data["title"]
    event.description = data["description"]
    event.date = data["date"]
    event.location = data["location"]

    db.session.commit()

    return jsonify({"message": "Event updated successfully"})


# DELETE event
@main.route("/events/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_event(id):

    event = Event.query.get_or_404(id)

    db.session.delete(event)
    db.session.commit()

    return jsonify({"message": "Event deleted successfully"})