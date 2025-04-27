import json
import os
import shutil
from datasets import Dataset
from tqdm import tqdm

#########
local_path = 'zhizhowang/OpenDataLab___ProverQA/dev/hard.json'
save_path = 'zhizhowang/SFTdataset/hard.json'
with open(local_path,'r',encoding = 'utf-8') as f:
    data = json.load(f)

print(data[0].keys())

sft_data =[]
for item in tqdm(data):
    answer = item["answer"]
    question = item["question"]
    reasoning = item["reasoning"]
    options = item["options"]
    context = item["context"]
    option_text = f"options:\n{options}"
    
    usr_contents = f'background:\n{context}\n\nquestion:\n{question}{option_text}'
    assistant_contents = f"OK,let's reason step by step.\n\n{reasoning}The final answer is:\n{answer}"
    sft_sample = {
        "conversations":[
            {"role": "system","content":"You are an expert in logical reasoning. Please analyze the background knowledge in detail, reason step by step, and finally draw a clear conclusion."},
            {"role":"user","content":usr_contents},
            {"role":"assistant","content":assistant_contents}
        ]
    }
    sft_data.append(sft_sample)
# 👉 自动创建文件夹
os.makedirs(os.path.dirname(save_path), exist_ok=True)

with open(save_path,'w',encoding="utf-8")as f:
     json.dump(sft_data, f, ensure_ascii=False, indent=2)

print(f"SFT数据处理完成,保存到: {save_path}")