import sys
import os
from PIL import Image 
import re

try:
    if(len(sys.argv) > 3):
        print("Too many arguments. Please enter source and target path")
        exit()
    elif(len(sys.argv) < 3):
        if(not 1 < len(sys.argv)):
            print("Source path not provided")
            exit()
        elif(not 2 < len(sys.argv)):
            print("Target path not provided ")
            exit()

    source_path = sys.argv[1]
    target_path = sys.argv[2]

    if(os.path.exists(source_path) == False):
        print(f"Error: Source path ${source_path} doeen't exists !!!")
        exit()
    
    if(os.path.exists(target_path) == False):
        print(f"Creating Folder at {target_path}")
        os.mkdir(target_path)

    images = os.listdir(source_path)

    for image in images:
        img = Image.open(os.path.join(source_path, image))
        img.thumbnail((200, 200))
       
        # 1st method - replace jpg to png
        #regex = r"(?:jpg|jpeg)"
        #target_img = re.sub(regex, "png", image)

        #2nd method
        clean_img = os.path.splitext(image)[0]
        print(clean_img)
        img.save(os.path.join(target_path, clean_img+".png"), 'png')

    print("All done")

except Exception as err:
    print(err)