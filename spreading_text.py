from PIL import Image


def convert_to_pixels(image_path):
    img = Image.open(image_path)
    width, height = img.size

    img = img.convert('RGB')

    pixel_image = Image.new('RGB', (width, height))
    pixels = pixel_image.load()

    for x in range(width):
        for y in range(height):
            pixel = img.getpixel((x, y))
            pixels[x, y] = pixel

    pixel_image.show()
    pixel_image.save("pixelated_" + image_path)


if __name__ == "__main__":
    image_path = input("Podaj ścieżkę do obrazka: ")
    convert_to_pixels(image_path)
