import cv2
import time
import sys
import subprocess
import numpy as np

AUDIO_OFFSET = 4.5
VIDEO_FILE = "chika_full.mp4"
AUDIO_FILE = "chika_audio2.mp3"
ASCII_CHARS = np.array(list("@#S%?*+;:-. "))
WIDTH = 80
HEIGHT = int(WIDTH * 0.45)


def play_audio(audio_path):
    return subprocess.Popen(
        ["ffplay", "-nodisp", "-autoexit", "-loglevel", "quiet", audio_path],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
    )

def main():
    cap = cv2.VideoCapture(VIDEO_FILE)
    fps = cap.get(cv2.CAP_PROP_FPS)

    sys.stdout.write("\033[?25l\033[2J")
    sys.stdout.flush()

    audio_process = play_audio(AUDIO_FILE)
    start_time = time.time() + AUDIO_OFFSET

    try:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret: break

            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            lower_green = np.array([35, 40, 40])
            upper_green = np.array([85, 255, 255])
            mask = cv2.inRange(hsv, lower_green, upper_green)

            small_color = cv2.resize(frame, (WIDTH, HEIGHT), interpolation=cv2.INTER_NEAREST)
            small_mask = cv2.resize(mask, (WIDTH, HEIGHT), interpolation=cv2.INTER_NEAREST)

            gray = cv2.cvtColor(small_color, cv2.COLOR_BGR2GRAY)
            indices = (gray * (len(ASCII_CHARS) - 1) // 255).astype(int)

            output = bytearray(b"\033[H")
            for y in range(HEIGHT):
                for x in range(WIDTH):
                    if small_mask[y, x] > 0:
                        output += b" "
                    else:
                        b, g, r = small_color[y, x]
                        char = ASCII_CHARS[indices[y, x]].encode()
                        color_code = f"\033[38;2;{r};{g};{b}m".encode()
                        output += color_code + char
                output += b"\n"

            actual_elapsed = time.time() - start_time
            expected_elapsed = cap.get(cv2.CAP_PROP_POS_FRAMES) / fps

            if actual_elapsed < expected_elapsed:
                time.sleep(expected_elapsed - actual_elapsed)

            sys.stdout.buffer.write(output)
            sys.stdout.buffer.flush()

            if audio_process.poll() is not None: break

    except KeyboardInterrupt:
        pass
    finally:
        audio_process.terminate()
        cap.release()
        sys.stdout.write("\033[0m\033[?25h\n")
        sys.stdout.flush()


if __name__ == "__main__":
    main()