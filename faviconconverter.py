from PIL import Image
import sys
import os

def main(input_path):
    img = Image.open(input_path)
    favicon = img.resize((48, 48), Image.LANCZOS)

    base = os.path.splitext(input_path)[0]
    output = base + "_favicon.png"

    favicon.save(output, "PNG")
    print(f"Favicon saved at: {output}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python faviconconverter.py <image_path>")
    else:
        main(sys.argv[1])
