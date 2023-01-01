#!/usr/bin/env python3
import os, shutil

if __name__ == "__main__":
    
    for i in range(1, 13):
        path = f"./{i:02}"
        os.makedirs(f"{path}/")
        files = [file for file in os.listdir(".") if file.startswith(f"{i:02}-")]
        print(files)
        for file in files:
            shutil.move(f"./{file}", f"{path}/{file}")
