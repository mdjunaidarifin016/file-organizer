import os 
import shutil
import directory_find

def file_move(src,directory,folder):
    file_name=os.path.basename(src)
    destination_path=os.path.join(directory,folder)
    try:
        os.makedirs(destination_path,exist_ok=True)
    except PermissionError:
        print("Permission not granted while creating folder")
        return
    except OSError as o:
        print(f"Something went wrong while creating folder: {o}")
        return
    name,ext=os.path.splitext(file_name)
    final_file=os.path.join(destination_path,file_name)
    if os.path.exists(final_file):
        i=0
        while True:
            i+=1
            new_file_name=f"{name}_{i}{ext}"
            new_file=os.path.join(destination_path,new_file_name)
            if not os.path.exists(new_file):
                final_file=new_file
                break
    try:
        shutil.move(src,final_file)
    except PermissionError:
        print("Permission not granted")
    except OSError as o:
        print(f"Something went wrong while moving file: {o}")

running=True
while running:
    directory_path=input("Enter the directory:")
    if os.path.isdir(directory_path):
        try:
            file_folder_list=os.listdir(directory_path)
        except PermissionError:
            print("Permission not granted")
            continue
        except OSError as o:
            print(f"Something went wrong: {o}")
            continue
    else:
        print("Directory doesn't exist or this is not a directory")
        continue
    if not file_folder_list :
        print("folder is empty")
        continue
    else:
        for item in file_folder_list:
            full_path=os.path.join(directory_path,item)
            if os.path.isfile(full_path):
                _,ext=os.path.splitext(item)
                folder_name=directory_find.directory_finder.get(ext.lower(),"Others")
                file_move(full_path,directory_path,folder_name)
            elif os.path.isdir(full_path):
                all_files=[]
                for root,dirs,files in os.walk(full_path):
                    for file in files:
                        file_path=os.path.join(root,file)
                        all_files.append(file_path)
                for file in all_files:
                    file_name=os.path.basename(file)
                    _,ext=os.path.splitext(file_name)
                    folder_name=directory_find.directory_finder.get(ext.lower(),"Others")
                    file_move(file,directory_path,folder_name)


    while True:
        print("1.Continue")
        print("2.Exit")

        try:
            choice=int(input("Enter your choice:"))
        except ValueError:
            print("Enter a valid choice , try again!")
            continue
        if choice==1:
            break
        elif choice==2:
            print("Thank You")
            running=False
            break
        else:
            print("Enter valid choice!")
            continue
        
