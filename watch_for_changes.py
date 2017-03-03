import sys
import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
import logging
from watchdog.events import LoggingEventHandler
import os
import shutil
from shutil import make_archive

# PatternMatchingEventHandler is a class which inherits FileEventHandler(from .Net) and we can use those methods
# Basically the events are :create, modified, deleted, moved

# The below methods can be executed 
# on_any_event : It can be executed on all the above stated events, if they are defined
# on_created : When a file/directory is created the method will execute
# on_moved : This method can be executed when a file/directory is moved
# on_deleted: Executed when a file/directory is deleted
# on_modified: Executed when a file/directory is modified

# Above all methods can have three parameter and the first parameter is event object as first parameter
"""
	event_type : modified | created | moved | deleted
	is_directory : True | False
	src_path : Path to observe the file (which file/folder should be monitored)

"""

class MyHandler(PatternMatchingEventHandler):
    #patterns = ["*.xml", "*.lxml", "*.py", "*pyc"]
    patterns = ["*"]

    def process(self, event):
        """
        event.event_type 
            'modified' | 'created' | 'moved' | 'deleted'
        event.is_directory
            True | False
        event.src_path
            path/to/observed/file
        """
        # the file will be processed there
        print event.src_path, event.event_type

        if os.path.isfile("/Users/bhargavsaidama/twitter.zip") == True: 
            os.remove("/Users/bhargavsaidama/twitter.zip")
            print ("existing file is removed ")
            shutil.make_archive("twitter", "zip", "/Users/bhargavsaidama/twitter")
            print ("delete existing zip file and created a new zip file")
        else:
            print ("There is no zip file at the moment")
            shutil.make_archive("twitter","zip", "/Users/bhargavsaidama/twitter")
            print (" A new zip file is created now ")


          # print now only for degug

    def on_any_event(self, event):
        self.process(event)

#    def on_created(self, event):
#        self.process(event)

    


if __name__ == '__main__':
    args = sys.argv[1:]
    observer = Observer()
    observer.schedule(MyHandler(), path=args[0] if args else '.', recursive = True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()

# To tar a file by using python script 
"""
    from shutil import make_archive


    shutil.make_archive('twitter', "zip", '/Users/bhargavsaidama/twitter')
"""
