import os

import cv2
import numpy as np
from filter_bank import _FILTERS, FILTER_NAMES
from PIL import Image, ImageFilter
from pillow_lut import load_cube_file, rgb_color_enhance


class ImageModel:
    """
    A Wrapper Class for PIL.Image to support custom Kernels

    Attributes
    ----------
    original: the original image of type PIL.Image
    filtered: the filtered image of type PIL.Image

    """

    def __init__(self, filepath=None):

        self.original = None
        self.filtered = None

        if filepath is not None:
            self.original = Image.open(filepath)

    def apply_filter(self, filter_id, config_id, kernel_size=11):
        config = _FILTERS[filter_id][config_id]

        if FILTER_NAMES[filter_id].lower() == "vignette":
            self.filtered = self.appy_vignette(
                sigma=config["size"],
                brightness=config["brightness"],
                contrast=config["contrast"],
            )
        else:
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

            self.filtered = self.original.filter(kernel)

            # deallocate large resources to clear memory
            del kernel

        return self.filtered

    def appy_vignette(self, sigma, brightness, contrast):
        img = np.copy(np.asarray(self.original))
        h, w, c = img.shape

        kernel = cv2.getGaussianKernel(500, sigma)
        kernel = kernel * kernel.T

        mask = 255 * (kernel / np.linalg.norm(kernel))
        mask = cv2.resize(mask, (w, h))

        for i in range(3):
            img[:, :, i] = img[:, :, i] * mask

        img = Image.fromarray(np.uint8(img))

        kernel = rgb_color_enhance(
            5,
            brightness=brightness,
            exposure=0.0,
            contrast=contrast,
            warmth=0.0,
            saturation=0.0,
            vibrance=0.0,
            hue=0.00,
            gamma=1.0,
        )
        img = img.filter(kernel)

        del kernel

        return img

    def load(self, filepath):
        self.original = Image.open(filepath)

    def save(self, filename, filter_id, config_id):
        if self.filtered is None:
            return

        dirpath = os.path.join('static', filename, FILTER_NAMES[filter_id])
        os.makedirs(dirpath, exist_ok=True)
        filepath = os.path.join(dirpath, f"{config_id}.jpg")
        self.filtered.save(filepath)
        return filepath
