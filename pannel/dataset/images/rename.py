import os
count = 0
dir = "aux_images"

# for i in range(0, 110):
#     x = f"{i:05d}"
#     src = "HighresScreenshot"+x+".png"
#     if os.path.exists(src):
#         os.rename(src, "pannel"+str(count)+".png")
#         count += 1


directory = 'usb_images'
new_name = "usb"
for filename in os.listdir(directory):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        print(os.path.join(directory, filename))
        x = filename[6:-4]
        print(x)
        os.rename(os.path.join(directory, filename), os.path.join(directory, new_name+x+".png"))