import os
from django.utils import timezone
from PIL import Image
from django.core.exceptions import ValidationError

def validate_image_size(image):
    max_size = 5 * 1024 * 1024  # 5MB
    if image.size > max_size:
        raise ValidationError('Image size must be no more than 5MB')

def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.pdf', '.doc', '.docx']
    if ext.lower() not in valid_extensions:
        raise ValidationError('Unsupported file extension.')

def compress_image(image):
    img = Image.open(image)
    if img.mode in ('RGBA', 'P'):
        img = img.convert('RGB')
    
    # Set a maximum dimension while maintaining aspect ratio
    max_dimension = 1200
    ratio = min(max_dimension/float(img.size[0]), max_dimension/float(img.size[1]))
    new_size = tuple([int(x*ratio) for x in img.size])
    
    if ratio < 1:  # Only resize if image is larger than max dimension
        img = img.resize(new_size, Image.Resampling.LANCZOS)
    
    return img 