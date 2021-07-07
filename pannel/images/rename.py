import os

for i in range(0, 202):
    x = f"{i:05d}"
    src = "HighresScreenshot"+x+".png"
    if os.path.exists(src):
        os.rename(src, "pannel"+str(i)+".png")
