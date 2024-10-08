import os
import cv2


def convert_mov(input_file, output_file):
    try:

        file_size = os.path.getsize(input_file)
        max_size = 500 * 1024 * 1024

        if file_size > max_size:
            print("The file exceeds 500MB. Please create an account to proceed.")
            return

        if not input_file.lower().endswith('.mov'):
            raise ValueError(f"Error: {input_file} is not a .MOV file.")

        input_video = cv2.VideoCapture(input_file)

        if not input_video.isOpened():
            raise FileNotFoundError(f"Could not open the file: {input_file}")

        width = int(input_video.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(input_video.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = input_video.get(cv2.CAP_PROP_FPS)

        mp4_codec = cv2.VideoWriter_mp4_fourcc(*'mp4v')
        output_video = cv2.VideoWriter(
            output_file, mp4_codec, fps, (width, height))

        while True:
            ret, frame = input_video.read()
            if not ret:
                break

            output_video.write(frame)

        input_video.release()
        output_video.release()

        print(f"Converted")

    except FileNotFoundError as fnf_error:
        print(fnf_error)
    except Exception as e:
        print(f"Ocurrió un error al convertir el archivo: {e}")


convert_mov("input_file.mov", "output_file.mp4")
