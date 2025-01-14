import cv2
import numpy as np
import pyautogui
import time
import ctypes

def screen_recorder(output_file="output.avi", fps=20):
    screen_width, screen_height = pyautogui.size()

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_file, fourcc, fps, (screen_width, screen_height))
    ctypes.windll.user32.MessageBoxW(0, "Recording... Press 'Ctrl+C' to stop.", "Recording", 1)

    try:
        while True:
            img = pyautogui.screenshot()

            frame = np.array(img)

            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

            out.write(frame)
    except KeyboardInterrupt:
        print("\nRecording stopped.")

    out.release()
    print(f"Recording saved as {output_file}")

if __name__ == "__main__":
    screen_recorder(output_file="screen_record.avi", fps=20)
