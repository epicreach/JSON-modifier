import json
import os


def main():
    userinput = input("Remove key-value pairs(f) from objects or remove objects with key-value(r)? (f/r): ")
    if(userinput == "r"):
        remove_objects_with_value()
    elif(userinput == "f"):
        copy_json_with_filter()
    else:
        print("Invalid input. Please enter 'f' or 'r'.")
        main()

def remove_objects_with_value():
    filepath = get_file_path()
    key_to_check = input("Enter key to check: ")
    userinput = input("Enter value to remove: ")
    if(userinput == "true"):
        value_to_remove = True
    elif(userinput == "false"):
        value_to_remove = False
    elif(userinput == "null"):
        value_to_remove = None
    else:
        value_to_remove = userinput
    new_file_name = input("Enter new file name: ")
    remove_objects(filepath, key_to_check, value_to_remove, f"{new_file_name}.json")

   
def remove_objects(json_file_path, key_to_check, value_to_remove, output_file_name):
    """
    Remove objects from a JSON file based on a specified key-value pair.

    Args:
        json_file_path (str): The path to the JSON file.
        key_to_check (str): The key to check in each object.
        value_to_remove (str): The value to remove objects with.
        output_file_name (str): The name of the output file.

    Returns:
        None

    Raises:
        Exception: If an error occurs during the removal process.
    """
    try:
        with open(json_file_path, 'r', encoding='utf-8') as in_file:
            data = json.load(in_file)
            new_data = [obj for obj in data if obj.get(key_to_check) != value_to_remove]

        script_dir = os.path.dirname(os.path.abspath(__file__))
        output_file_path = os.path.join(script_dir, output_file_name)

        with open(output_file_path, 'w', encoding='utf-8') as out_file:
            json.dump(new_data, out_file, indent=2)

        print(f"Successfully removed objects with {key_to_check}={value_to_remove} from {json_file_path}. Result saved to {output_file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

def copy_json_with_filter():
    filepath = get_file_path()
    keys_to_copy = get_keys()
    new_file_name = input("Enter new file name: ")
    copy_selected_keys(filepath, keys_to_copy, f"{new_file_name}.json")
 
    
def get_file_path():
    while True:
        filepath = input("Enter path to JSON file: ")
        if filepath.endswith(".json") and os.path.isfile(filepath):
            return filepath
        else:
            print("Invalid file path. Please enter a valid path to a JSON file.")

def get_keys():
    keys = []
    while True:
        key = input("Enter key to copy (press enter to stop): ")
        if key == "":
            break
        keys.append(key)
    return keys

def copy_selected_keys(json_file_path, selected_keys, output_file_name):
    """
    Copy selected key-value pairs from a JSON file to a new file.

    Parameters:
    json_file_path (str): The path to the JSON file.
    selected_keys (list): A list of keys to be selected.
    output_file_name (str): The name of the output file.

    Returns:
    None
    """
    try:
        with open(json_file_path, 'r', encoding='utf-8') as in_file:
            data = json.load(in_file)
            new_data = [{key: value for key, value in obj.items() if key in selected_keys} for obj in data]

        script_dir = os.path.dirname(os.path.abspath(__file__))
        output_file_path = os.path.join(script_dir, f'{output_file_name}')

        with open(output_file_path, 'w',encoding='utf-8') as out_file:
            json.dump(new_data, out_file, indent=2)

        print(f"Successfully copied selected key-value pairs from {json_file_path} to {output_file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")




if __name__ == "__main__":
    main()
