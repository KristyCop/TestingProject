import json;

def getTestData(file):
    TEST_DATA = []

    with open(file,'r') as f:
        TEST_DATA=json.load(f)
    return TEST_DATA

    