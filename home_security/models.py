from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
import uuid

db = SQLAlchemy()

class EventType(db.Model):
    __tablename__ = 'event_type'
    
    event_type_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=True)
    description = db.Column(db.Text)
    severity_level = db.Column(db.Integer)
    
    # Relationship
    events = db.relationship('Event', back_populates='event_type')

class Event(db.Model):
    __tablename__ = 'events'
    
    event_id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    timestamp = db.Column(db.TIMESTAMP, nullable=False, default=datetime.utcnow)
    event_type_id = db.Column(db.Integer, db.ForeignKey('event_type.event_type_id'))
    location = db.Column(db.String(255))
    description = db.Column(db.Text)
    status = db.Column(db.String(50), default='active')
    
    # Relationships
    event_type = db.relationship('EventType', back_populates='events')
    images = db.relationship('EventImage', back_populates='event')

class EventImage(db.Model):
    __tablename__ = 'event_images'
    
    image_id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    event_id = db.Column(db.String(36), db.ForeignKey('events.event_id'))
    image_url = db.Column(db.Text, nullable=False)
    captured_at = db.Column(db.TIMESTAMP, nullable=False, default=datetime.utcnow)
    
    # Relationship
    event = db.relationship('Event', back_populates='images') 