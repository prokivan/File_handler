import csv
import json
import pickle


class FileHandler:
    def __init__(self, file_path):
        self.file_path = file_path

    def load(self):
        raise NotImplementedError('Method "load" must be implemented in the inheriting class')

    def save(self, data):
        raise NotImplementedError('Method "save" must be implemented in the inheriting class')


class CSVFileHandler(FileHandler):
    def load(self):
        with open(self.file_path, 'r') as csv_file:
            reader = csv.reader(csv_file)
            return [row for row in reader]

    def save(self, data):
        with open(self.file_path, 'w') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerows(data)


class JsonFileHandler(FileHandler):
    def load(self):
        with open(self.file_path, 'r') as json_file:
            return json.load(json_file)

    def save(self, data):
        with open(self.file_path, 'w') as json_file:
            json.dump(data, json_file, indent=4)


class PickleFileHandler(FileHandler):
    def load(self):
        with open(self.file_path, 'rb') as pickle_file:
            return pickle.load(pickle_file)

    def save(self, data):
        with open(self.file_path, 'wb') as pickle_file:
            pickle.dump(data, pickle_file)


class TxtFileHandler(FileHandler):
    def load(self):
        with open(self.file_path, 'r') as txt_file:
            return [line.strip().split(',') for line in txt_file.readlines()]

    def save(self, data):
        with open(self.file_path, 'w') as txt_file:
            for row in data:
                txt_file.write(','.join(row) + '\n')
