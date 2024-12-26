from flask import request
from flask.views import MethodView
from ..models import db, EventImage
from ..schemas import event_image_schema, event_images_schema
from . import api

class EventImageAPI(MethodView):
    def post(self, event_id):
        """Create a new event image"""
        image_url = request.json.get('image_url')
        
        event_image = EventImage(
            event_id=event_id,
            image_url=image_url
        )
        
        db.session.add(event_image)
        db.session.commit()
        
        return event_image_schema.dump(event_image), 201
    
    def get(self, event_id=None, image_id=None):
        """Get all images for an event or a specific image"""
        if image_id is not None:
            image = EventImage.query.get_or_404(image_id)
            return event_image_schema.dump(image)
        
        images = EventImage.query.filter_by(event_id=event_id).all()
        return event_images_schema.dump(images)
    
    def put(self, image_id):
        """Update an event image"""
        image = EventImage.query.get_or_404(image_id)
        
        image.image_url = request.json.get('image_url', image.image_url)
        
        db.session.commit()
        
        return event_image_schema.dump(image)
    
    def delete(self, image_id):
        """Delete an event image"""
        image = EventImage.query.get_or_404(image_id)
        db.session.delete(image)
        db.session.commit()
        return '', 204

# Register the routes
event_image_view = EventImageAPI.as_view('event_image_api')
api.add_url_rule('/events/<string:event_id>/images', view_func=event_image_view, methods=['GET', 'POST'])
api.add_url_rule('/images/<string:image_id>', view_func=event_image_view, methods=['GET', 'PUT', 'DELETE']) 