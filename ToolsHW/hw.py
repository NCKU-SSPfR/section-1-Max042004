import sys
import webbrowser

VIDEO_URL = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"


def open_video():
    """
    Open the specified video URL in the default web browser.
    """
    webbrowser.open(VIDEO_URL)


def main():
    """
    Continuously prompt the user for the result of 1 * 1 until it's correct or
    until the user types 'exit'.
    """
    while True:
        user_input = input("1 times 1 = ? ")

        if user_input.lower() == "exit":
            sys.exit()

        if user_input == "1":
            print("Correct! Enjoy the video!")
            open_video()
            break
        else:
            print("Wrong! Try again.")


if __name__ == "__main__":
    main()
