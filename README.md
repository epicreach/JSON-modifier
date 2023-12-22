# JSON-datacopier

## How to use

Simply clone the repository and run. You have 2 options:

- **Remove key-value pairs from objects**: This makes a copy of the JSON file and removes the specified key-value pair from every object that contains it. For example, if your JSON file looks like this:

  ```json
  [
    {
      "name": "John",
      "job": "Janitor",
      "income": 1234,
      "married": true
    },
    {
      "name": "Carl",
      "job": "Musician",
      "income": 0,
      "married": false
    }
  ]
  ```

  and you input "name" and "income" as filters, the copied JSON file will look like this:

  ```json
  [
    {
      "job": "Janitor",
      "married": true
    },
    {
      "job": "Musician",
      "married": false
    }
  ]
  ```

- **Remove objects with key-value pairs**: This will remove any object that has a specified value for the specified key. For example, if you input "name" for the key and "John" for the value, it will remove any objects that have "John" as the value for "name". The new JSON file will be saved as a copy.

## Saving

The copied JSON file will be saved in the same folder as the `main.py` file.

## Encoding

If you're having issues copying due to encoding problems, you can change the encoding in the following line of code:
