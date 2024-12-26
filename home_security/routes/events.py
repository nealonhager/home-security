from flask import request
from flask.views import MethodView
from ..models import db
from ..models.event import Event, event_schema, events_schema
from . import api

class EventAPI(MethodView):
    def post(self):
        """Create a new event"""
        event_type_id = request.json.get('event_type_id')
        location = request.json.get('location')
        description = request.json.get('description')
        status = request.json.get('status', 'active')
        
        event = Event(
            event_type_id=event_type_id,
            location=location,
            description=description,
            status=status
        )
        
        db.session.add(event)
        db.session.commit()
        
        return event_schema.dump(event), 201
    
    def get(self, event_id=None):
        """Get all events or a specific one"""
        if event_id is None:
            events = Event.query.all()
            return events_schema.dump(events)
        
        event = Event.query.get_or_404(event_id)
        return event_schema.dump(event)
    
    def put(self, event_id):
        """Update an event"""
        event = Event.query.get_or_404(event_id)
        
        event.event_type_id = request.json.get('event_type_id', event.event_type_id)
        event.location = request.json.get('location', event.location)
        event.description = request.json.get('description', event.description)
        event.status = request.json.get('status', event.status)
        
        db.session.commit()
        
        return event_schema.dump(event)
    
    def delete(self, event_id):
        """Delete an event"""
        event = Event.query.get_or_404(event_id)
        db.session.delete(event)
        db.session.commit()
        return '', 204

# Register the routes
event_view = EventAPI.as_view('event_api')
api.add_url_rule('/events', view_func=event_view, methods=['GET', 'POST'])
api.add_url_rule('/events/<string:event_id>', view_func=event_view, methods=['GET', 'PUT', 'DELETE']) 