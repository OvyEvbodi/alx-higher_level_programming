#!/usr/bin/python3

"""This module creates an Object from a “JSON file”"""
import json


def load_from_json_file(filename):
    """creates an Object from a “JSON file"""
    with open(filename, 'r') as f:
        return json.load(f)
