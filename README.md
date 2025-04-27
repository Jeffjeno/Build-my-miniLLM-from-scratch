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
# 🔥 推理样例对比（Base Model vs LoRA 微调后模型）

## 🧮 问题

A bag contains 4 red balls, 5 blue balls, and 6 green balls.  
If two balls are drawn one after another without replacement, what is the probability that the first ball is red and the second ball is either blue or green?

---

## ✨ 推理过程详情

<details>
<summary><strong>原始模型（Base Model）推理输出</strong></summary>

```text
To solve this problem, we need to calculate the probability of drawing a red ball first and then a ball that is either blue or green second.

First, let's determine the total number of balls in the bag:

Total number of balls = 4 (red) + 5 (blue) + 6 (green) = 15

Step 1: Probability of Drawing a Red Ball First  
P(Red first) = 4 / 15

Step 2: Probability of Drawing a Blue or Green Ball Second  
After drawing a red ball first, there are now 14 balls left in the bag, with 9 of them being either blue or green.  
P(Blue or Green second | Red first) = 9 / 14

Step 3: Combined Probability  
P(Red first and Blue or Green second) = (4/15) * (9/14) = 36/210 = 6/35

Thus, the probability that the first ball is red and the second ball is either blue or green is 6/35.
```
</details>
<details>
<summary><strong>LoRA 微调模型推理输出</strong></summary>
  
```
To find the probability that the first ball drawn is red and the second ball drawn is either blue or green, we can break down the problem into two parts:

First, let's determine the total number of balls in the bag:  
- Red balls: 4  
- Blue balls: 5  
- Green balls: 6  
Total number of balls = 15.

Probability of drawing a red ball on the first draw:  
P(Red on 1st draw) = 4 / 15

After drawing a red ball, there are now 14 balls left with 5 blue and 6 green balls remaining.  
Thus, P(Blue or Green on 2nd draw | Red on 1st draw) = (5 + 6) / 14 = 11/14

Combined probability:  
P(Red on 1st draw and Blue or Green on 2nd draw) = (4/15) * (11/14) = 44/210 = 22/105

Thus, the probability that the first ball is red and the second ball is either blue or green is 22/105.
```
</details>

---

📈 小结
	•	Base Model：推理过程中遗漏了绿球，导致最终答案偏差。
	•	LoRA 微调模型：推理细致入微，考虑到所有情况，最终答案正确且逻辑严谨。
	•	微调显著提升了模型的推理正确率和复杂问题处理能力！🚀

### 🤝 <font color="#00aa00">贡献方式</font>
欢迎大家提 Issue 或 Pull Request 🎯
请参阅我们的 贡献指南。

### 📜 <font color="#00aa00">许可证</font>
本项目遵循 MIT License。

### ⭐ <font color="#00aa00">Star</font>
如果你喜欢这个项目，记得给个 Star 支持一下！⭐ </p> 
### 📚 <font color="#00aa00">参考来源 (References)</font>

本项目部分灵感、方法和数据参考了以下优秀开源项目，特此致谢：

- 🌿 [ProverGen: Large Language Models Meet Symbolic Provers for Logical Reasoning Evaluation](https://github.com/opendatalab/ProverGen)  
  [ICLR 2025 Paper](https://openreview.net/forum?id=C25SgeXWjE)

- 🌿 [MiniMind: Building Minimal and Effective Foundation Models from Scratch](https://github.com/jingyaogong/minimind)

---

> 📌 如果您在您的研究或项目中使用了本项目，欢迎引用或标注以上参考来源 ❤️
---

