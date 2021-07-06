import os

filepath = "images/train"
for i in range(0, 68):
    x = f"{i:05d}"
    src = os.path.sep.join([filepath, "HighresScreenshot"+x+".png"])
    if os.path.exists(src):
        os.rename(src, os.path.sep.join([filepath, "sat_train_"+str(197+i)+".png"]))
