import os
import sys

def get_paths():
    return sorted([file for file in os.listdir(os.getcwd()) if file.endswith(".json")],
                  key = lambda x: (x[0], x[1:-5]))

print(get_paths())