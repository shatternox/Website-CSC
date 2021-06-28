import os
import secrets
from PIL import Image
from flask import current_app


def save_profile_image(imageForm, current_profile):
    _, fileExt = os.path.splitext(imageForm.filename)

    img_name = secrets.token_hex(8) + fileExt

    if current_profile != "default.png":
        curr_prof_path = os.path.join(
            current_app.root_path, 'static/images/profile_image', current_profile)
        os.remove(curr_prof_path)

    img_path = os.path.join(current_app.root_path,
                            'static/images/profile_image', img_name)

    img = Image.open(imageForm)
    # img.thumbnail((500,500))
    img.save(img_path)

    return img_name


def save_background_image(imageForm, current_background):
    _, fileExt = os.path.splitext(imageForm.filename)

    img_name = secrets.token_hex(8) + fileExt

    if current_background != "default-bg.jpg":
        curr_bg_path = os.path.join(
            current_app.root_path, 'static/images/background', current_background)
        os.remove(curr_bg_path)

    img_path = os.path.join(current_app.root_path,
                            'static/images/background', img_name)

    img = Image.open(imageForm)
    # img.thumbnail((1280,720))
    img.save(img_path)

    return img_name
