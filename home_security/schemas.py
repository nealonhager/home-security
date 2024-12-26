from flask_marshmallow import Marshmallow
from marshmallow import fields

ma = Marshmallow()

class EventTypeSchema(ma.Schema):
    class Meta:
        fields = ('event_type_id', 'name', 'description', 'severity_level')

class EventImageSchema(ma.Schema):
    class Meta:
        fields = ('image_id', 'event_id', 'image_url', 'captured_at')
    
    captured_at = fields.DateTime(format='iso')

class EventSchema(ma.Schema):
    class Meta:
        fields = ('event_id', 'timestamp', 'event_type_id', 'location', 'description', 
                 'status', 'event_type', 'images')
    
    timestamp = fields.DateTime(format='iso')
    event_type = fields.Nested(EventTypeSchema)
    images = fields.Nested(EventImageSchema, many=True)

# Initialize schema instances
event_type_schema = EventTypeSchema()
event_types_schema = EventTypeSchema(many=True)
event_schema = EventSchema()
events_schema = EventSchema(many=True)
event_image_schema = EventImageSchema()
event_images_schema = EventImageSchema(many=True) 