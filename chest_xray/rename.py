import os

path = "E:/Important files/GITHUB/Chest_Xray_Disease_Detection/chest_xray/test_Copy/NORMAL"
i = 0
for filename in os.listdir(path):
    print (filename)
    os.rename(filename, ('normal'+str(i)+'.jpeg'))
    i = i+1
