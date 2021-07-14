import os
count = 0
directory = "pannel/ports/validation/images/temp"

new_name = "img"
for filename in os.listdir(directory):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        print(os.path.join(directory, filename))
        x = int(filename[3:-4])
        print(x)
        os.rename(os.path.join(directory, filename), os.path.join(directory, new_name+str(x)+".png"))