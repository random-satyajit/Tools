
import win32api

i=0
res={}
try:
  while True:
    ds=win32api.EnumDisplaySettings(None, i)
    res.append(f"{ds.PelsWidth}x{ds.PelsHeight}")
    i+=1
except: pass
for i in res:
  print(i)
print(res)
