#!/usr/bin/python3

"""This module creates an Object from a “JSON file”"""
import json


def load_from_json_file(filename):
    with open(filename, 'r', encoding="UTF8") as f:
        return json.load(f)
