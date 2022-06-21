#!../.venv/bin/python
import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'resume.settings')

import django
django.setup()
from django.core.management import call_command


PATH = 'static/'
modified = False
call_command("collectstatic", interactive=False)


class EventHandler(FileSystemEventHandler):

    def __init__(self):
        super().__init__()
    
    def on_any_event(self, event):
        global modified
        modified = True
        print(event.event_type, event.src_path)


if __name__ == "__main__":
    event_handler = EventHandler()
    observer = Observer()
    observer.schedule(event_handler, PATH, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(2)
            if modified:
                call_command("collectstatic", interactive=False)
                modified = False
    finally:
        observer.stop()
        observer.join()