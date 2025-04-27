<p align="center">
  <img src="https://img.shields.io/badge/SFT--Dataset-SFT%20Ready-brightgreen?style=flat-square" alt="SFTdataset Badge">
  <img src="https://img.shields.io/github/license/Jeffjeno/Build-my-miniLLM-from-scratch?style=flat-square" alt="License">
  <img src="https://img.shields.io/github/stars/Jeffjeno/Build-my-miniLLM-from-scratch?style=flat-square" alt="Stars">
</p>


<h1 align="center">🍀 <font color="#00aa00">SFTdataset</font> 🍀</h1>

<p align="center">
🌿 Part of the <b>Build My Mini LLM from Scratch</b> Project 🌿
</p>

---

## 🌱 <font color="#00aa00">项目简介</font>

本仓库用于存放 **Supervised Fine-Tuning (SFT)** 阶段使用的数据集，支持微调大型语言模型（LLMs），特别适配自定义推理、问答和思维链（CoT）任务。

---

## ✨ <font color="#00aa00">功能亮点</font>

- 📚 **高质量数据**：涵盖推理、推断、思维链等任务
- ⚙️ **灵活处理**：提供数据预处理脚本，可快速适配不同模型
- 🚀 **无缝集成**：兼容 Transformers、PyTorch 等主流训练框架
- 🛠️ **开放扩展**：支持新增任务类型与自定义数据增强

---

## 🚀 <font color="#00aa00">快速开始</font>

### 1. 克隆仓库

```bash
git clone https://github.com/Jeffjeno/Build-my-miniLLM-from-scratch.git
cd Build-my-miniLLM-from-scratch/SFTdataset
```
2. 安装依赖
```bash

pip install -r requirements.txt
```
3. 使用示例
加载并预处理数据集：

```python

from sftdataset import load_dataset
```
# 加载数据
```
dataset = load_dataset("data/medium.json")
```
# 查看样本
```
print(dataset[0])
```
集成到 LLM 训练管道：

```python

from transformers import Trainer, TrainingArguments
```
# 定义模型和训练参数
```
model = ...
training_args = TrainingArguments(
    output_dir="./results",
    num_train_epochs=3,
    per_device_train_batch_size=8,
    save_steps=10,
    save_total_limit=2,
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=dataset,
)

trainer.train()
```
📂 <font color="#00aa00">目录结构</font>
```text

SFTdataset/
├── data/               # 原始数据集（easy.json, medium.json, hard.json）
├── processed_data/     # 预处理和分词后的数据
├── scripts/            # 数据处理辅助脚本
├── requirements.txt    # 项目依赖
└── README.md           # 文档说明
```
📚 <font color="#00aa00">数据格式示例</font>
```json

{
  "id": 0,
  "options": ["A) True", "B) False", "C) Uncertain"],
  "answer": "B",
  "question": "Based on the above information, is the following statement true, false, or uncertain? Brecken has never experienced heartbreak.",
  "reasoning": "fact1: Brecken has experienced heartbreak.\nrule: Either Brecken has experienced heartbreak or he has never experienced heartbreak, but not both.\nconclusion: Brecken has experienced heartbreak.\n\nTherefore, it is false that Brecken has never experienced heartbreak. The correct option is: B.",
  "context": "Brecken has experienced heartbreak. Either Brecken has experienced heartbreak or he has never experienced heartbreak, but not both.",
  "nl2fol": {
    "Brecken has experienced heartbreak.": "has_experienced_heartbreak(Brecken)",
    "Either Brecken has experienced heartbreak or he has never experienced heartbreak, but not both.": "has_experienced_heartbreak(Brecken) ⊕ has_never_experienced_heartbreak(Brecken)"
  },
  "conclusion_fol": "has_never_experienced_heartbreak(Brecken)"
}
```
🤝 <font color="#00aa00">贡献方式</font>
欢迎大家提 Issue 或 Pull Request 🎯
请参阅我们的 贡献指南。

📜 <font color="#00aa00">许可证</font>
本项目遵循 MIT License。

⭐ <font color="#00aa00">Star</font>
如果你喜欢这个项目，记得给个 Star 支持一下！⭐ </p> 
