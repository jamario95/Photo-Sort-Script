import os
import shutil
from datetime import datetime
import sys

def sort_by_date(folder_path):
    #Listing all the files in the directory
    files = os.listdir(folder_path)

    # FIltering only for image files
    image_extensions = [".jpg", ".jepg", ".png"]
    image_files = [file for file in files if os.path.splitext(file)[1].lower() in image_extensions]
    print("Image Files:", image_files)

    #Sorting images by modification time
    image_files.sort(key=lambda x: os.path.getmtime(os.path.join(folder_path, x)))

    #Create a folder for each year
    for file in image_files:
        file_path = os.path.join(folder_path, file)
        modification_time = os.path.getmtime(file_path)
        date = datetime.fromtimestamp(modification_time)
        year = str(date.year)


       # Create directory for each year if not exists
        destination_folder = os.path.join(folder_path, year)
        os.makedirs(destination_folder, exist_ok=True)

        # Move the file to the respective folder
        shutil.move(file_path, os.path.join(destination_folder, file))







if __name__ == "__main__":

    # Path to the folder using command line argument
    folder_path = sys.argv[1]

    # Sorting function
    sort_by_date(folder_path)


