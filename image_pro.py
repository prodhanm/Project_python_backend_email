from pathlib import Path
from PIL import Image, ImageFilter

dir = Path(r"./image/")
dir2 = Path(r"/s_image/")
#dir2.mkdir()
size = (500,500)

def image_load(dir):
    logo = Image.open(dir/"logo.png")
    logo.load()
    for index, file in enumerate(dir.glob("*.jpg"), 1):
        img = Image.open(file)
        img.load()
        cropped_img = img.crop((0,0,2500,4000))
        logo_conv = logo.convert("L")
        logo_func = logo_conv.point(lambda x:255 if x > 50 else 0)
        logo_filter = logo_func.filter(ImageFilter.CONTOUR)
        logo_trans = logo_filter.point(lambda x: 0 if x ==255 else 255)
        cropped_img.paste(logo_trans, (0,0), logo_trans)
        cropped_img.thumbnail(size)
        print(cropped_img.size)
        #cropped_img.save(f"{dir}/{dir2}/mufassa{index}.jpg")

image_load(dir)