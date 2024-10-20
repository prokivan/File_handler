import sys
from icecream import ic
from file_handlers import CSVFileHandler, JsonFileHandler, PickleFileHandler, TxtFileHandler


def get_file_handler(file_path):
    if file_path.endswith('.csv'):
        return CSVFileHandler(file_path)
    elif file_path.endswith('.json'):
        return JsonFileHandler(file_path)
    elif file_path.endswith('.pkl'):
        return PickleFileHandler(file_path)
    elif file_path.endswith('.txt'):
        return TxtFileHandler(file_path)
    else:
        raise ValueError("Unsupported file format!")


# (json, pkl)
def apply_changes_to_dicts(data, changes):
    keys = ['id', 'name', 'city']
    for change in changes:
        y, key_idx, value = change.split(',')
        y = int(y)
        key_idx = int(key_idx)
        key = keys[key_idx]
        data[y][key] = value
    return data


# (csv, txt)
def apply_changes_to_lists(data, changes):
    for change in changes:
        x, y, value = change.split(',')
        x = int(x)
        y = int(y)

        data[y][x] = value
    return data


def main():
    if len(sys.argv) < 4:
        print("Usage: python reader.py <input_file> <output_file> <change_1> <change_2> ... <change_n>")
        return

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    changes = sys.argv[3:]

    handler = get_file_handler(input_file)

    data = handler.load()

    if isinstance(data, list) and isinstance(data[0], dict):
        modified_data = apply_changes_to_dicts(data, changes)
    else:
        modified_data = apply_changes_to_lists(data, changes)

    ic(modified_data)

    handler = get_file_handler(output_file)
    handler.save(modified_data)
