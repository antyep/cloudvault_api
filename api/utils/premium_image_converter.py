import os
import pyheif
from PIL import Image


def convert_heic(input_file, output_file):
    try:
        file_size = os.path.getsize(input_file)
        max_size = 200 * 1024 * 1024

        if file_size > max_size:
            print("The file exceeds 200MB. Please create an account to proceed.")
            return

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
        print(f"Successfully converted: {output_file}")

    except pyheif.error.HeifError:
        print(f"Error: {input_file} is not a valid HEIC file.")

    except FileNotFoundError:
        print(f"Error: {input_file} does not exist.")

    except Exception as e:
        print(f"Error: An error occurred: {e}")


convert_heic("input_file.heic", "output_file.jpg")
