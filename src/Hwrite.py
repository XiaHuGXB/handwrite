from PIL import Image, ImageFont
from handright import Template, handwrite


def hwrite(text,config):
    if config.line_spacing < config.front_size:
        config.line_spacing = config.front_size
    template = Template(
        background=Image.new(mode="1", size=(config.image_weight, config.image_height), color=1),
        font=ImageFont.truetype('../fonts/handwrite.ttf', size=config.front_size),
        left_margin=config.left_margin,
        right_margin=config.right_margin,
        top_margin=config.top_margin,
        bottom_margin=config.bottom_margin,
        word_spacing=config.word_spacing,
        line_spacing=config.line_spacing,  #line_spacing > font_size

        # random parameter
        font_size_sigma = config.font_size_sigma,
        word_spacing_sigma = config.word_spacing_sigma,
        line_spacing_sigma = config.line_spacing_sigma,
        perturb_x_sigma = config.perturb_x_sigma,
        perturb_y_sigma = config.perturb_y_sigma,
        perturb_theta_sigma = config.perturb_theta_sigma,
    )
    images = handwrite(text, template)
    return images