import os
import shutil
import datetime
import schedule
import time

source_dir = "/home/mittesh/Pictures/Screenshots"
destination_dir = "/home/mittesh/Backups"

def copy_folder_to_directory(source, dest):
    today = datetime.date.today()
    dest_dir = os.path.join(dest, str(today))
    
    try:
        shutil.copytree(source, dest_dir)
        print(f"Folder copied to: {dest_dir}")
    except FileExistsError:
        print(f"Folder already exists in: {dest}")

schedule.every().day.at("17:48").do(lambda: copy_folder_to_directory(source_dir, destination_dir)) 
# Python immediately evaluates copy_folder_to_directory(source_dir, destination_dir) and passes the result (which is None in this case, assuming the function doesn't return anything) to the do method. This results in the function being executed immediately, rather than being scheduled.
# To avoid this, you can pass the function itself and its arguments to the do method using a lambda function or schedule's built-in Job.do method that can handle arguments.

while True:
    schedule.run_pending()
    time.sleep(60) #seconds