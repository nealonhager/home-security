from flask import Blueprint

api = Blueprint('api', __name__)

from . import event_types, events, images, scheduler

__all__ = ['api'] 