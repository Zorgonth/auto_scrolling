import time
import threading
import subprocess
import argparse
from pynput import keyboard

class AutoScroll:
    def __init__(self, scroll_delay=0.1, scroll_amount=1):
        self.scroll_delay = scroll_delay
        self.scroll_amount = scroll_amount
        self.scrolling = False
        self.scroll_thread = None

    def start_scrolling(self):
        if not self.scrolling:
            self.scrolling = True
            self.scroll_thread = threading.Thread(target=self._scroll)
            self.scroll_thread.start()

    def stop_scrolling(self):
        if self.scrolling:
            self.scrolling = False
            self.scroll_thread.join()

    def _scroll(self):
        while self.scrolling:
            for _ in range(self.scroll_amount):
                subprocess.call(['xdotool', 'key', 'Down'])
            time.sleep(self.scroll_delay)

def on_press(key):
    try:
        if key.char == 'k':
            auto_scroll.start_scrolling()
        elif key.char == 's':
            auto_scroll.stop_scrolling()
    except AttributeError:
        pass

def main(scroll_delay, scroll_amount):
    global auto_scroll
    auto_scroll = AutoScroll(scroll_delay=scroll_delay, scroll_amount=scroll_amount)
    
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Auto-scroll a page using keyboard inputs.")
    parser.add_argument("scroll_delay", type=float, nargs='?', default=0.1, help="Time delay between scrolls (in seconds).")
    parser.add_argument("scroll_amount", type=int, nargs='?', default=1, help="Number of scroll actions per interval.")
    
    args = parser.parse_args()
    main(scroll_delay=args.scroll_delay, scroll_amount=args.scroll_amount)
