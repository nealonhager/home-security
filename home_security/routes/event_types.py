from flask import request
from flask.views import MethodView
from ..models import db
from ..models.event_type import EventType, event_type_schema, event_types_schema
from . import api

class EventTypeAPI(MethodView):
    def post(self):
        """Create a new event type"""
        name = request.json.get('name')
        description = request.json.get('description')
        severity_level = request.json.get('severity_level')
        
        event_type = EventType(
            name=name,
            description=description,
            severity_level=severity_level
        )
        
        db.session.add(event_type)
        db.session.commit()
        
        return event_type_schema.dump(event_type), 201
    
    def get(self, event_type_id=None):
        """Get all event types or a specific one"""
        if event_type_id is None:
            event_types = EventType.query.all()
            return event_types_schema.dump(event_types)
        
        event_type = EventType.query.get_or_404(event_type_id)
        return event_type_schema.dump(event_type)
    
    def put(self, event_type_id):
        """Update an event type"""
        event_type = EventType.query.get_or_404(event_type_id)
        
        event_type.name = request.json.get('name', event_type.name)
        event_type.description = request.json.get('description', event_type.description)
        event_type.severity_level = request.json.get('severity_level', event_type.severity_level)
        
        db.session.commit()
        
        return event_type_schema.dump(event_type)
    
    def delete(self, event_type_id):
        """Delete an event type"""
        event_type = EventType.query.get_or_404(event_type_id)
        db.session.delete(event_type)
        db.session.commit()
        return '', 204

# Register the routes
event_type_view = EventTypeAPI.as_view('event_type_api')
api.add_url_rule('/event-types', view_func=event_type_view, methods=['GET', 'POST'])
api.add_url_rule('/event-types/<int:event_type_id>', view_func=event_type_view, methods=['GET', 'PUT', 'DELETE']) 