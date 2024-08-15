import time
import threading
import subprocess
from pynput import keyboard

class AutoScroll:
    def __init__(self, scroll_delay=0.5):
        self.scroll_delay = scroll_delay
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
            subprocess.call(['xdotool', 'click', '5'])
            time.sleep(self.scroll_delay)

auto_scroll = AutoScroll()

def on_press(key):
    try:
        if key.char == 'k':
            auto_scroll.start_scrolling()
        elif key.char == 's':
            auto_scroll.stop_scrolling()
    except AttributeError:
        pass

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
