import os
from PIL import Image
import subprocess
import platform
import logging
import shutil

from utils.logger import configure_logger

configure_logger()
logger = logging.getLogger(__name__)

class IconGenerator:
    def __init__(self, input_path, output_dir):
        self.input_path = input_path
        self.output_dir = output_dir
        self.image = Image.open(input_path)
        self.sizes = [16, 32, 64, 128, 256]

    def convert_to_icns(self):
        logger.info("Converting to ICNS")
        icns_dir = os.path.join(self.output_dir, 'icns')
        os.makedirs(icns_dir, exist_ok=True)
        if platform.system() == "Darwin":  # macOS
            for size in self.sizes:
                icns_path = os.path.join(icns_dir, f'icon_{size}x{size}.icns')
                iconset_dir = os.path.join(icns_dir, f'icon_{size}x{size}.iconset')
                os.makedirs(iconset_dir, exist_ok=True)

                try:
                    icon_path = os.path.join(iconset_dir, f'icon_{size}x{size}.png')
                    logger.info(f"Creating icon: {icon_path}")
                    self.image.resize((size, size)).save(icon_path)
                    logger.info(f"Creating ICNS: {icns_path}")
                    result = subprocess.run(['iconutil', '-c', 'icns', iconset_dir, '-o', icns_path], capture_output=True, text=True)
                    if result.returncode != 0:
                        logger.error(f"iconutil failed: {result.stderr}")
                        continue
                    shutil.rmtree(iconset_dir)  # Use shutil.rmtree to remove the iconset directory
                except subprocess.CalledProcessError as e:
                    logger.error(f"Failed to generate ICNS for size {size}x{size}: {e}")
        else:
            logger.error("ICNS conversion only supported on macOS! You can also use a tool like https://iconverticons.com/")

    def convert_to_ico(self):
        logger.info("Converting to ICO")
        ico_dir = os.path.join(self.output_dir, 'ico')
        os.makedirs(ico_dir, exist_ok=True)
        for size in self.sizes:
            ico_path = os.path.join(ico_dir, f'icon_{size}x{size}.ico')
            self.image.resize((size, size)).save(ico_path, format='ICO')
            logger.info(f"ICO saved: {ico_path}")

    def convert_to_gif(self):
        logger.info("Converting to GIF")
        gif_dir = os.path.join(self.output_dir, 'gif')
        os.makedirs(gif_dir, exist_ok=True)
        for size in self.sizes:
            gif_path = os.path.join(gif_dir, f'icon_{size}x{size}.gif')
            self.image.resize((size, size)).save(gif_path, format='GIF')
            logger.info(f"GIF saved: {gif_path}")

    def generate_all(self):
        logger.info("Generating all icons")
        self.convert_to_icns()
        self.convert_to_ico()
        self.convert_to_gif()

if __name__ == "__main__":
    input_path = 'icon.png'
    output_dir = 'generated/'
    generator = IconGenerator(input_path, output_dir)
    generator.generate_all()