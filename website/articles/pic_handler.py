import os
import secrets
from PIL import Image
from flask import current_app


def save_article_image(imageForm, current_image):
    _, fileExt = os.path.splitext(imageForm.filename)

    img_name = secrets.token_hex(8) + fileExt

    if current_image != "article.png":
        curr_image_path = os.path.join(
            current_app.root_path, 'static/images/article', current_image)
        os.remove(curr_image_path)

    img_path = os.path.join(current_app.root_path,
                            'static/images/article', img_name)

    img = Image.open(imageForm)
    # img.thumbnail((500,500))
    img.save(img_path)

    return img_name
