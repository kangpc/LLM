from torch.utils.data import Dataset
from datasets import load_dataset

class MyDataset(Dataset):
    def __init__(self,split):
        #从磁盘加载数据
        self.dataset = load_dataset(path="csv",data_files=f"/Users/a1233/yiyan/code/Embracing-AI/AI-learn/AI-learn/bert/extra_long_text_train//data/news/{split}.csv",split="train")
    def __len__(self):
        return len(self.dataset)

    def __getitem__(self, item):
        text = self.dataset[item]["text"]
        label = self.dataset[item]["label"]
        return text,label

if __name__ == '__main__':
    dataset = MyDataset("test")
    for data in dataset:
        print(data)