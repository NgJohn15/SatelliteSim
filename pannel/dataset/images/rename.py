import os
count = 0
for i in range(0, 110):
    x = f"{i:05d}"
    src = "HighresScreenshot"+x+".png"
    if os.path.exists(src):
        os.rename(src, "pannel"+str(count)+".png")
        count += 1
