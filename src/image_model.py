import os

from PIL import Image, ImageFilter
from pillow_lut import load_cube_file, rgb_color_enhance

from .filter_bank import _FILTERS


class ImageModel:
    """
    A Wrapper Class for PIL.Image to support custom Kernels
    """

    def __init__(self):
        self.original_img = None
        self.filtered_img = None

    def apply_filter(self, filter_name, config_id, kernel_size=11):
        config = _FILTERS[filter_name][config_id]
        kernel = rgb_color_enhance(
            kernel_size,
            brightness=config["brightness"],
            exposure=config["exposure"],
            contrast=config["contrast"],
            warmth=config["warmth"],
            saturation=config["saturation"],
            vibrance=config["vibrance"],
            hue=config["hue"],
            gamma=config["gamma"],
        )

        self.filtered_img = self.original_img.filter(kernel)

        # deallocate large resources to clear memory
        del kerenel

        return self.filtered_img

    def load(self, filepath):
        self.original_img = Image.open(filepath)

    def save(self, filepath, filter_name, config_id):
        if self.filtered_img is None:
            return

        filepath = os.path.join("filepath", filter_name, f"{config_id}.jpg")
        self.filtered_img.save(filepath)
