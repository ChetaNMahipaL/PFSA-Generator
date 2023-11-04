import re
import json
import pytest
import argparse
from typing import Dict


def construct(file_str: str) -> Dict[str, Dict[str, float]]:

    """Takes in the string representing the file and returns pfsa
    The given example is for the statement "A cat"
    """

    dict = {}
    
    # TODO: FILE IN THIS FUNCTION
    file_str=file_str.lower()
    # print(file_str)
    res = re.split('\s+', file_str)
    # print(res)

    # new_list = [item[] for item in res]
    # new_list=set(new_list)
    if res[0] == "":
        dict = { "*" : {} }
        # print(dict)
        return dict
    for item in res:
        # print(item)
        for j in range(-1,len(item)):
            # print(j)
            if j == (-1):
                list = dict.keys()
                if "*" not in list:
                    temp_1 = {"*" : {item[:(j+2)] : 1} }
                    dict.update(temp_1)
                else:
                    list_1 = dict["*"].keys()
                    if item[:(j+2)] in list_1:
                        dict["*"][item[:(j+2)]] += 1
                    else:
                        temp = {item[:(j+2)] : 1}
                        dict["*"].update(temp)
            elif j == (len(item) - 1):
                list = dict.keys()
                if item[:(j+1)] not in list:
                    temp_1 = { item[:(j+1)]: { (item[:(j+1)]+"*") : 1} }
                    dict.update(temp_1)
                else:
                    list_1 = dict[item[:(j+1)]].keys()
                    if (item[:(j+1)]+"*") in list_1:
                        dict[item[:(j+1)]][(item[:(j+1)]+"*")] += 1
                    else:
                        temp = {(item[:(j+1)]+"*") : 1}
                        dict[item[:(j+1)]].update(temp)
            else:
                list = dict.keys()
                if item[:(j+1)] not in list:
                    temp_1 = {item[:(j+1)] : {item[:(j+2)] : 1} }
                    dict.update(temp_1)
                else:
                    list_1 = dict[item[:(j+1)]].keys()
                    if item[:(j+2)] in list_1:
                        dict[item[:(j+1)]][item[:(j+2)]] += 1
                    else:
                        temp = {item[:(j+2)] : 1}
                        dict[item[:(j+1)]].update(temp)
    
    key_main = dict.keys()
    for key in key_main:
        key_sec=dict[key].keys()
        j=0
        for key_s in key_sec:
            j += dict[key][key_s]
        for key_s in key_sec:
            dict[key][key_s] /= j
            dict[key][key_s] = round(dict[key][key_s], 2)





    return dict # {
    #     "*": {"a": 0.5, "c": 0.5},
    #     "a": {"a*": 1.0},
    #     "c": {"ca": 1.0},
    #     "ca": {"cat": 1.0},
    #     "cat": {"cat*": 1.0},
    # }


def main():
    """
    The command for running is `python pfsa.py text.txt`. This will generate
    a file `text.json` which you will be using for generation.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("file", type=str, help="Name of the text file")
    args = parser.parse_args()

    with open(args.file, "r") as file:
        contents = file.read()
        output = construct(contents)

    name = args.file.split(".")[0]          # to get filename without extension

    with open(f"{name}.json", "w") as file:
        json.dump(output, file)             # used to serialize the data and write it to the file in JSON format
    # construct("")


if __name__ == "__main__":
    main()


STRINGS = ["A cat", "A CAT", "", "A", "A A A A"]
DICTIONARIES = [
    {
        "*": {"a": 0.5, "c": 0.5},
        "a": {"a*": 1.0},
        "c": {"ca": 1.0},
        "ca": {"cat": 1.0},
        "cat": {"cat*": 1.0},
    },
    {
        "*": {"a": 0.5, "c": 0.5},
        "a": {"a*": 1.0},
        "c": {"ca": 1.0},
        "ca": {"cat": 1.0},
        "cat": {"cat*": 1.0},
    },
    {
        "*": {},
    },
    {
        "*": {"a": 1.0},
        "a": {"a*": 1.0},
    },
    {
        "*": {"a": 1.0},
        "a": {"a*": 1.0},
    },
]


@pytest.mark.parametrize("string, pfsa", list(zip(STRINGS, DICTIONARIES)))
def test_output_match(string, pfsa):
    """
    To test, install `pytest` beforehand in your Python environment.

    Run `pytest pfsa.py` Your code must pass all tests. There are additional
    hidden tests that your code will be tested on during VIVA.
    """
    result = construct(string)
    assert result == pfsa