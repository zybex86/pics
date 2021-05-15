from pathlib import Path
from PIL import Image, ImageOps


def generate_thumbnail(file_path, max_height):
    size = (max_height, max_height)
    thumbnail = ImageOps.fit(Image.open(file_path), size, Image.ANTIALIAS)
    thumbnail.save(f'{Path(file_path).stem}_thumb_{max_height}.jpg', 'JPEG')
    return thumbnail
