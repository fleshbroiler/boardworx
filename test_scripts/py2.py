#
#	Andy St John for XOS/Bob Tatar
#	12/09/2014 

# 	provide backup capability to HDMOBILE device
#       target of backup is /xos directory
#	destination is /data  

#	define a function to evaluate any backups with the same date and return an index value for the new backup
#	or, use minute and second 
#	NOTE: As implemented this creates a file with this naming schema: 121014_222802.tar.gz, where the name 
#       is MMDDYY_HHMMSS. HH is 24 hour format. 


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

# filename is today's date,if a matching file(s) is found at the destination, append n+1 to date

#today's date formatted as a filename
today = time.strftime("%m")+time.strftime("%d")+time.strftime("%y")+"_"+time.strftime("%H")+time.strftime("%M")+time.strftime("%S")
 
#for path,dirs,files in os.walk('xos'):
#for path,dirs,files in os.walk('xos'):
#for files in os.listdir('/home/andy/dev/xos') 
files = os.listdir('/home/andy/dev/xos') 
for fn in files:
	token = fn
	#print token
	if token.find(today) == -1:   
		# no matching date,      
		zipdir( today+".tar.gz" )


