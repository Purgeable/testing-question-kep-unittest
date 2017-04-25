"""File paths for CSV file and parsing definitions."""

import os

# datafile location

def get_default_csv_path():
    """Source data CSV file"""
    return os.path.join('data','tab.csv')


# specfile locations

PARSING_DEFINITIONS_FOLDER = 'parsing_definitions'
DEFAULT_SPEC_FILE = "__spec.txt"
SPEC_FILENAME_MUST_CONTAIN = "spec"

def get_default_spec_folder():
    return PARSING_DEFINITIONS_FOLDER 

def get_main_spec_filepath(folder):
    path = os.path.join(folder, DEFAULT_SPEC_FILE)
    if os.path.exists(path):
        return path
    else:
        raise FileNotFoundError(path)
        
def get_additional_specs_filepaths(folder):
    """Returns list of filepaths of additional parsing definitions 
       found in *folder*."""
    paths = [os.path.join(folder, f) 
             for f in os.listdir(folder)             
             if SPEC_FILENAME_MUST_CONTAIN in f
             and f != DEFAULT_SPEC_FILE]    
    return [p for p in paths if os.path.isfile(p)]


import unittest
class TestPaths(unittest.TestCase):
    
    def test_default_dir(self):
        _dir = get_default_spec_folder()
        assert get_main_spec_filepath(_dir) == 'parsing_definitions\\__spec.txt'
        
if __name__ == '__main__':
    unittest.main()    
