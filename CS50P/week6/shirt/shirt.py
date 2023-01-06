import sys
from PIL import Image, ImageOps
import os


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) >= 4:
        sys.exit("To many command-line arguments")
    else:
        ext1 = os.path.splitext(sys.argv[1])
        ext2 = os.path.splitext(sys.argv[2])
        if ext1[1] == ext2[1]:
            change_file(sys.argv[1], sys.argv[2])
        else:
            sys.exit("Input and output have different extensions")


def change_file(input, output):
    shirt = Image.open("shirt.png")
    puppet = Image.open(input)
    muppet_resize = ImageOps.fit(puppet, shirt.size, Image.Resampling.BICUBIC, bleed=0.0, centering=(0.5, 0.5))
    muppet_resize.paste(shirt, box=None, mask=shirt)
    muppet_resize.save(sys.argv[2])


if __name__ == "__main__":
    main()
