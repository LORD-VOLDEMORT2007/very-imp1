import os , shutil

os.mkdir("C:/Ai_program_training_images")

class1_images_location = "C:/Ai_program_training_images/class1"
class2_images_location = "C:/Ai_program_training_images/class2"

def moving_into_folder_class1(from_path1):            
    if os.path.exists(class1_images_location):
        print("moving")
        shutil.move(from_path1 , class1_images_location)
    else:
        os.mkdir("C:/Ai_program_training_images/class1")
        shutil.move(from_path1 , class1_images_location)

def moving_into_folder_class2(from_path2):              
    if os.path.exists(class2_images_location):
        print("moving")
        shutil.move(from_path2 , class2_images_location)
    else:
        os.mkdir("C:/Ai_program_training_images/class2")
        shutil.move(from_path2 , class2_images_location)