#backup the /xos dir to /data if sufficient space exists

import os
import filehelp
import time

targetPath = '/xos'
destinationPath = '/data/'

# get the uncompressed size in bytes of the directory to be backed up... 
targetBytes = os.path.getsize(targetPath)

#get the size in bytes of the remaining space on the destination device
remainingBytes = filehelp.get_free_space_bytes(destinationPath) 

print "xos dir size in bytes: " 
print targetBytes 
print remainingBytes

if targetBytes < remainingBytes:
	#since we have enough room to back up the target to the destination, get a filename
	#today = destinationPath + "hdmobile_"+time.strftime("%m")+time.strftime("%d")+time.strftime("%y")+"_"+time.strftime("%H")+time.strftime("%M")+time.strftime("%S")+"bak.tar.gz" 
	today = destinationPath + "hdmobile_"+time.strftime("%m")+time.strftime("%d")+time.strftime("%y")+".tar.gz" 
	filehelp.zipdir(today, targetPath)
	
