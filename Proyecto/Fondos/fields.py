from django.db.models.fields.files import ImageField, ImageFieldFile
from PIL import Image
import os

def _add_thumb(s):
    parts = s.split(".")
    parts.insert(-1, "thumb")
    if parts[-1].lower() not in ['jpeg', 'jpg']:
        parts[-1] = 'jpg'
    return ".".join(parts)
