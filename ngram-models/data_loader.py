import json
from pathlib import Path


def get_vn_express_dataset(data_folder):
    # data_folder = Path('/Users/D071576/Downloads/vnexpress_dataset/')
    dataset = dict()
    for file_path in data_folder.glob('*.json'):
        topic = file_path.stem
        print(f"topic = {topic}")
        try:
            data = json.load(open(file_path))
            dataset[topic]=data
            print(f"Loaded {len(data)} articles")
        except:
            print(f"Failed to load {topic}")
            
    data = []
    for topic, articles in dataset.items():
        for article in articles:
            data.append(article['content'].strip().split())
    return data

class VNExpress_dataset:
    def __init__(self, data_folder):
        self.data = get_vn_express_dataset(data_folder=data_folder)
        self.vocabularies = set()
        for text in self.data:
            self.vocabularies.update(set(text))
        self.vocab_size = len(self.vocabularies)
