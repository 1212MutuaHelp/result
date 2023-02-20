# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。
import torch
from torch.utils.data import Dataset
import pdfplumber
import os


def Readpdf(pdf_item_path):
    with pdfplumber.open(pdf_item_path) as pdf:
        for i, page in enumerate(pdf.pages):
            print(i)
            print(page.extract_text())
    pdf.close()



class MyData(Dataset):
    def __init__(self, root_dir, label_dir):  # 构造函数，root是train目录，label是科研/非科研目录
        self.root_dir = root_dir
        self.label_dir = label_dir
        self.path = os.path.join(self.root_dir, self.label_dir)
        self.pdf_path = os.listdir(self.path)  # path获取路径，pdf_path生成一个列表

    def __getitem__(self, item):  # 读取每一个pdf
        pdf_name=self.pdf_path[item]            #每个pdf的名称
        pdf_item_path=os.path.join(self.path,pdf_name)  #每个pdf的相对路径
        label=self.label_dir


        return label                            #返回一个pdf对应的label

    def __len__(self):
        return len(self.pdf_path)




# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    root_dir="dataset//train"
    scientific_label_dir="scientific"
    other_label_dir="other"
    scientific_dataset=MyData(root_dir,scientific_label_dir)
    #Readpdf(os.path.join(root_dir,scientific_label_dir,scientific_dataset.pdf_path[0]))
    other_dataset=MyData(root_dir,other_label_dir)
    train_dataset=scientific_dataset+other_dataset