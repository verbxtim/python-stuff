# made to easily find OBS stream key (and send it in a web request)
import os
import json
import requests

subpath = "obs-studio\\basic\\profiles\\";
path1 = os.path.join(os.getenv("APPDATA"), subpath);
path2 = os.path.join(path1, os.listdir(path1)[0] + "\\");
path3 = os.path.join(path2, "service.json");

f = open(path3)
 
data = json.load(f)
print(str(data['settings']))

f.close()
