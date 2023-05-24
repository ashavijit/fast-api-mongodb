import os
from uuid import uuid4
from PIL import Image

static = "static"


def save_pic(file, folderName: str = "", fileName: str = ""):
    random_name = str(uuid4())
    _, f_ext = os.path.splitext(file.filename)
    pic_name = (random_name if fileName == "" else fileName) + f_ext

    path = os.path.join(static, folderName)
    if not os.path.exists(path):
        os.makedirs(path)

    pic_path = os.path.join(path, pic_name)

    out_size = (200, 200)
    i = Image.open(file.file)

    i.thumbnail(out_size)
    i.save(pic_path)

    return f"{static}/{folderName}/{pic_name}"
