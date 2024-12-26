# Home Security System

A Flask-based API for managing home security events, event types, and related images.

## Installation

1. Make sure you have Python 3.12+ and Poetry installed
2. Clone this repository
3. Install dependencies:
```bash
poetry install
```

## Configuration

Create a `.env` file in the root directory with the following variables:
```
DATABASE_URL=mysql://user:password@localhost/home_security
FLASK_APP=home_security.app
FLASK_ENV=development
```

## Running the Application

```bash
poetry run api
```

## Available Scripts

- `poetry run api` - Start the Flask API server
- `poetry run db-wipe` - Wipe all database tables
- `poetry run db-wipe-events` - Wipe only events table
- `poetry run db-wipe-types` - Wipe only event types table
- `poetry run db-wipe-images` - Wipe only event images table

## API Documentation

### Event Types

#### GET /api/event-types
Get all event types

Response:
```json
[
    {
        "id": 1,
        "name": "Motion Detected",
        "description": "Motion sensor triggered",
        "severity_level": "medium"
    }
]
```

#### POST /api/event-types
Create a new event type

Request:
```json
{
    "name": "Motion Detected",
    "description": "Motion sensor triggered",
    "severity_level": "medium"
}
```

#### GET /api/event-types/<id>
Get a specific event type

#### PUT /api/event-types/<id>
Update an event type

#### DELETE /api/event-types/<id>
Delete an event type

### Events

#### GET /api/events
Get all events

Response:
```json
[
    {
        "id": 1,
        "event_type_id": 1,
        "location": "Front Door",
        "description": "Movement detected",
        "status": "active",
        "timestamp": "2024-01-01T12:00:00"
    }
]
```

#### POST /api/events
Create a new event

Request:
```json
{
    "event_type_id": 1,
    "location": "Front Door",
    "description": "Movement detected",
    "status": "active"
}
```

#### GET /api/events/<id>
Get a specific event

#### PUT /api/events/<id>
Update an event

#### DELETE /api/events/<id>
Delete an event

### Event Images

#### GET /api/events/<event_id>/images
Get all images for an event

#### POST /api/events/<event_id>/images
Add an image to an event

Request:
```json
{
    "image_url": "https://example.com/image.jpg"
}
```

#### GET /api/images/<id>
Get a specific image

#### PUT /api/images/<id>
Update an image

#### DELETE /api/images/<id>
Delete an image
