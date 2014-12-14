import tarfile
import os
import time

def reset(tarinfo):
    	tarinfo.uid = tarinfo.gid = 0
    	tarinfo.uname = tarinfo.gname = "root"
 	return tarinfo

def zipdir(flename):
	tar = tarfile.open("/home/andy/dev/data/" +flename, "w:gz")
	tar.add('/home/andy/dev/xos', filter=reset)
	tar.close()
   	return

#today's date formatted as a filename
today = time.strftime("%m")+time.strftime("%d")+time.strftime("%y")+"_"+time.strftime("%H")+time.strftime("%M")+time.strftime("%S")

files = os.listdir('/home/andy/dev/xos') 
for fn in files:
	#print fn

print 'fin'
