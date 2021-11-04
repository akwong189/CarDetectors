import os, shutil

def partition_dirs(path):
    directories = os.listdir(path)

    for directory in directories:
        full_dir = path + f"/{directory}"
        manufacturer_name = directory.split(" ")[0]
        print(manufacturer_name)

        files = os.listdir(full_dir)
        for file in files:
            shutil.copy(full_dir + f"/{file}", f"../data/{manufacturer_name}")


f = open("../external/data/names.csv")
names = f.read().split("\n")

manufacturers = set()

for name in names:
    if name != "":
        manufacturers.add(name.split(" ")[0])


for manufacturer in manufacturers:
    os.makedirs(f"../data/{manufacturer}", exist_ok=True)

# partition_dirs("../external/data/car_data/car_data/train")
partition_dirs("../external/data/car_data/car_data/test")