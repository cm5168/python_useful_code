import os,sys
cur_dir = os.getcwd()
nList = os.listdir(cur_dir)
print(cur_dir,nList)
extentions = ['mp4','avi']

for item in nList:
    if item == "asd":
        pass
    try:
        subList = os.listdir(cur_dir+"\\"+item)
        for file in subList:
            fList = file.split(".")
            if fList[-1].lower() in extentions:
                print("Moving %s.%s"%(item,fList[-1].lower()))
                os.rename(cur_dir+"\\%s\\%s"%(item,file),cur_dir+"\\%s.%s"%(item,fList[-1].lower()))
    except:
        pass