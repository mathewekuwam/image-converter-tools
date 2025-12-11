from PIL import Image
import sys
import os

def make_background_transparent(img, bg_color=(40, 40, 40), tolerance=60):
    img = img.convert("RGBA")
    datas = img.getdata()
    newData = []

    for item in datas:
        if all(abs(item[i] - bg_color[i]) <= tolerance for i in range(3)):
            newData.append((255, 255, 255, 0))  # Transparent pixel
        else:
            newData.append(item)

    img.putdata(newData)
    return img


def main(input_path):
    img = Image.open(input_path)

    transparent_img = make_background_transparent(img)

    base = os.path.splitext(input_path)[0]
    transparent_png = base + "_transparent.png"
    ico_path = base + ".ico"

    transparent_img.save(transparent_png, "PNG")
    transparent_img.resize((48, 48), Image.LANCZOS).save(ico_path, "ICO")

    print(f"Transparent PNG -> {transparent_png}")
    print(f"Favicon ICO -> {ico_path}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python TransparentPNGICO.py <image_path>")
    else:
        main(sys.argv[1])
