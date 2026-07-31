from . import db
from . import db, bcrypt

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)

    full_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(20), default="attendee")

    events = db.relationship("Event", backref="organizer", lazy=True)
    registrations = db.relationship("Registration", backref="user", lazy=True)
    def set_password(self, password):
      self.password_hash = bcrypt.generate_password_hash(password).decode("utf-8")

    def check_password(self, password):
      return bcrypt.check_password_hash(self.password_hash, password)

class Category(db.Model):
    __tablename__ = "categories"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    image_url = db.Column(db.String(255))
    status = db.Column(db.String(20), default="active")

    events = db.relationship("Event", backref="category", lazy=True)


class Event(db.Model):
    __tablename__ = "events"

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text)
    date = db.Column(db.String(50))
    location = db.Column(db.String(150))

    organizer_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"))

    registrations = db.relationship("Registration", backref="event", lazy=True)


class Registration(db.Model):
    __tablename__ = "registrations"

    id = db.Column(db.Integer, primary_key=True)

    ticket_type = db.Column(db.String(50))
    status = db.Column(db.String(20), default="registered")
    payment_status = db.Column(db.String(20), default="pending")
    registered_at = db.Column(db.String(50))

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    event_id = db.Column(db.Integer, db.ForeignKey("events.id"))