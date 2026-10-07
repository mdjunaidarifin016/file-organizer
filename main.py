import os 
import shutil
import directory_find

def move_file(src,directory,file):
    name,ext=os.path.splitext(file)
    folder_name=directory_find.directory_finder.get(ext.lower(),"Others")
    dst=os.path.join(directory,folder_name)
    if os.path.dirname(src)==dst :
        return
    try:
        os.makedirs(dst,exist_ok=True)
    except PermissionError:
        print("Permission not granted while creating folder")
        return
    except OSError as o:
        print(f"Something went wrong while creating folder : {o}")
        return
    i=0
    final_file=os.path.join(dst,file)
    if os.path.exists(final_file):
        while True:
            i+=1
            new_file_name=f"{name}_{i}{ext}"
            new_file=os.path.join(dst,new_file_name)
            if not os.path.exists(new_file):
                final_file=new_file
                break
    try:
        shutil.move(src,final_file)
    except PermissionError:
        print("Permission not granted while moving file")
        return
    except OSError as O:
        print(f"Something went wrong while moving file : {O}")
        return

running=True
while running:
    directory_path=input("Enter directory path:")
    if os.path.isdir(directory_path):
        try:
            file_folder_list=os.listdir(directory_path)
        except PermissionError:
            print("Permission Error")
            continue
        except OSError as o:
            print(f"Something went wrong : {o}")
            continue
    else:
        print("Directory doesnt exist or this is not a directory")
        continue
    if not file_folder_list:
        print("Folder is empty")
        continue
    else:
        for item in file_folder_list:
            item_path=os.path.join(directory_path,item)
            if os.path.isfile(item_path):
                move_file(item_path,directory_path,item)
            elif os.path.isdir(item_path):
                file_paths=[]
                for root,dirs,files in os.walk(item_path):
                    for file in files:
                        file_path=os.path.join(root,file)
                        file_paths.append(file_path)
                for file_path in file_paths:
                    file_name=os.path.basename(file_path)
                    move_file(file_path,directory_path,file_name)

    while True:
        print("1.Continue")
        print("2.exit")

        try:
           choice=int(input("Enter your choice:"))
        except ValueError:
            print("Enter a valid choice!")
            continue
        if choice==1:
            break
        elif choice==2:
            print("Thank You")
            running=False
            break
        else:
            print("Enter a valid choice")
