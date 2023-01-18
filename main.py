
from PIL import Image, ImageFont
from handright import Template, handwrite

text = "\t\t我能吞下玻璃而不伤身体。\n" \
       "郭炫斌真帅"
template = Template(
    background=Image.new(mode="1", size=(1024, 2048), color=1),
    font=ImageFont.truetype("fonts/handwrite.ttf", size=100),
)
images = handwrite(text, template)
for im in images:
    assert isinstance(im, Image.Image)
    im.save('./1.jpg')