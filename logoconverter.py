from PIL import Image
import sys
import os

sizes = {
    "website_header": (250, 100),
    "social_media": (400, 400),
    "retina": (500, 200),
    "app_icon": (1024, 1024)
}

def main(input_path):
    img = Image.open(input_path)

    base_dir = os.path.join(os.path.dirname(input_path), "exported_logos")
    os.makedirs(base_dir, exist_ok=True)

    for name, size in sizes.items():
        resized_img = img.resize(size, Image.LANCZOS)
        output_path = os.path.join(base_dir, f"{name}.png")
        resized_img.save(output_path, "PNG")
        print(f"Saved: {output_path}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python logoconverter.py <image_path>")
    else:
        main(sys.argv[1])

