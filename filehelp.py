import os

# returns the free space in bytes 
def get_free_space_bytes(directory):
        st = os.statvfs(directory)
        return st.f_bavail * st.f_frsize

# returns the free space in megabytes
def get_free_space_mb(directory):
        st = os.statvfs(directory)
        return st.f_bavail * st.f_frsize/1024/1024
