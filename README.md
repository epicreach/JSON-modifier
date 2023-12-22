# JSON-datacopier

## How to use

    Simply clone the rep and run. You have 2 options **Remove key-value pairs from objects** or ** Remove objects with key-value pairs**

    **Remove key-value pairs from objects**
    This makes a copy of the JSON file and removes the key-value pair you specify from every object that contains it.
    For example if your JSON file looks like this:
    [
     {
        "name": "John",
        "job": "Janitor",
        "income": 1234,
        "married": True
     },
     {
        "name": "Carl",
        "job": "Musician",
        "income": 0,
        "married": False
     }
    ]

    and you input "name" and "income" as filters the copied JSON file will look like this:
    [
     {
        "job": "Janitor",
        "married": True
     },
     {
        "job": "Musician",
        "married": False
     }
    ]


    **Remove objects with key-value pairs**

    This will remove any object who has a specified value for whatever key you speciified. So if you input "name" for key and "John" for value. It will remove any objects who has John as the value for "name". It will save the new JSON file as a copy

## Saving

    The copied JSON file will be saved in the same folder as the main.py file.

## Encoding

    If you're having issues copying due to encoding issue, change the encoding='utf-8' in
    ´´´
    with open(json_file_path, 'r', encoding='utf-8') as in_file:
    ´´´
    to whatever encoding you need
