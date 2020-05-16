from os import listdir
from os.path import isfile

my_path = "/home/yingzhi/Desktop/senior_project/darknet/build/darknet/x64/data/obj/"
output_path = "/home/yingzhi/Desktop/senior_project/darknet/build/darknet/x64/data/train.txt"

only_files = [f for f in listdir(my_path)]

only_image = [f for f in only_files if ".txt" not in f]

with open(output_path, "w") as f:
    for img in only_image:
        f.write("data/obj/" + img + "\n")
    print("Done!")

