import sys
from PIL import Image, ImageOps

def main():

    if len(sys.argv) < 3:
        sys.exit("Too few command line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command line arguments")

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    valid_ext = [".jpg", ".jpeg", ".png"]

    if not input_file.lower().endswith(tuple(valid_ext)):
        sys.exit("Invalid input")
    if not output_file.lower().endswith(tuple(valid_ext)):
        sys.exit("Invalid output")

    if input_file.split(".")[-1].lower() != output_file.split(".")[-1].lower():
        sys.exit("Input and output have different extensions")

    try:
        image = Image.open(input_file)
        shirt = Image.open("shirt.png")

    except FileNotFoundError:
        sys.exit("Input does not exist")

    image = ImageOps.fit(image, shirt.size)

    image.paste(shirt, shirt)
    image.save(output_file)

if __name__ == "__main__":
    main()
