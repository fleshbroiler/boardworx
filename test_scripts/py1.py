#
#	Andy St John 
#	for XOS      



import tarfile

def reset(tarinfo):
    tarinfo.uid = tarinfo.gid = 0
    tarinfo.uname = tarinfo.gname = "root"
    return tarinfo

tar = tarfile.open("test1.tar.gz", "w:gz")
tar.add('ncc', filter=reset)
tar.close()
