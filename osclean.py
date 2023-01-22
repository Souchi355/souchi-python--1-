import os
import time
os.chdir("C:/Users")
cwd=os.getcwd()
print(cwd)

for dic in os.listdir(cwd):
    if not(dic in ["All Users","Default","Default User","Public"]) and os.path.isdir(dic):
        user=dic
        break
user="C:/Users/"+user
desktop=user+"/Desktop/test"

os.chdir(desktop)

files={"docx":[],"py":[],"html":[],"css":[],"js":[],"sql":[],"pdf":[],"img":[],"other":[],}
for file in os.listdir(os.getcwd()):
    if os.path.isfile(file):
        if file[file.find("."):].lower() == ".docx":
            files["docx"].append(file)
        elif file[file.find("."):].lower() == ".py":
            files["py"].append(file)
        elif file[file.find("."):].lower() == ".html":
            files["html"].append(file)
        elif file[file.find("."):].lower() == ".css":
            files["css"].append(file)
        elif file[file.find("."):].lower() == ".js":
            files["js"].append(file)
        elif file[file.find("."):].lower() == ".sql":
            files["sql"].append(file)
        elif file[file.find("."):].lower() == ".pdf":
            files["pdf"].append(file)
        elif file[file.find("."):].lower() in [".png",".jpg",".gif"]:
            files["img"].append(file)
        else:
            files["other"].append(file)

for key in files.keys():
    os.makedirs(desktop+"/"+key)
    if key =="py":
        for f in files[key]:
            os.replace(desktop+"/"+f,desktop+"/"+key+"/"+f)