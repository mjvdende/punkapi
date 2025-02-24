import json
import os
from collections import OrderedDict

DIRECTORY_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'resources', 'data')


def load_data_from_directory(directory_path):
    full_data = []

    for filename in os.listdir(directory_path):
        if filename.endswith('.json'):
            file_path = os.path.join(directory_path, filename)
            with open(file_path, 'r') as file:
                data = json.load(file, object_pairs_hook=OrderedDict)
                full_data.append(data)

    return full_data


def get_db():
    return load_data_from_directory(DIRECTORY_PATH)

