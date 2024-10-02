import pyheif
from PIL import Image


def convert_heic(input_file, output_file):
    try:
        heif_file = pyheif.read(input_file)
        image = Image.frombytes(
            heif_file.mode,
            heif_file.size,
            heif_file.data,
            "raw",
            heif_file.mode,
            heif_file.stride,
        )

        image.save(output_file, "JPG")
        print(f"Succesfully converted: {output_file}")

    except pyheif.error.HeifError:
        # pyheif could not read a .heic file
        print(f"Error: {input_file} is not a valid HEIC file.")

    except FileExistsError:
        # If user leaves it blank
        print(f"Error: {input_file} does not exist.")

    except Exception as e:
        print(f"Error: An error occurred: {e}")  # others


convert_heic("input_file.heic", "output_file.jpg")
