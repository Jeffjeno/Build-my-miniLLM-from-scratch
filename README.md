
# Build-my-miniLLM-from-scratch

> 从零构建可进行推理增强微调的微型大语言模型（MiniLLM）Pipeline

## 目录

- [Build-my-miniLLM-from-scratch](#build-my-minillm-from-scratch)
	- [目录](#目录)
	- [项目简介](#项目简介)
	- [目录结构](#目录结构)
	- [环境要求](#环境要求)
	- [快速开始](#快速开始)
	- [数据准备](#数据准备)
	- [模型预处理与初始化](#模型预处理与初始化)
	- [推理增强方法集成](#推理增强方法集成)
	- [训练阶段设计](#训练阶段设计)
	- [推理阶段设计](#推理阶段设计)
	- [模型评估与部署](#模型评估与部署)
	- [贡献 \& 许可](#贡献--许可)

## 项目简介

本项目旨在从数据准备、模型初始化、推理增强、微调训练到模型评估与部署，构建一条完整的可复现的推理增强微调Pipeline。

## 目录结构

```text
.
├── trainer/               # 微调脚本和模型定义
│   ├── train_lora.py
│   └── model_lora.py
├── scripts/               # 数据处理脚本
│   └── dataset.py
├── download.py            # 模型下载工具
├── requirements.txt       # 依赖列表
└── README.md              # 项目说明文档
```

## 环境要求

- Python >= 3.8  
- CUDA >= 11.1（GPU 加速）  
- PyTorch >= 1.12  

安装依赖：
```bash
pip install -r requirements.txt
```

## 快速开始

1. **下载基座模型**  
   ```bash
   python download.py \
     --model_name Qwen/Qwen2.5-3B-Instruct \
     --save_dir ./qwen2.5-3b-instruct
   ```

2. **准备数据**  
   将 SFT 数据集（JSON 格式）放入 `data/` 目录，保证格式为：
   ```json
   [
     { "input": "问：...?", "output": "答：...", "loss_mask": [...] },
     ...
   ]
   ```

3. **LoRA 微调**  
   ```bash
   cd trainer
   python train_lora.py \
     --data_path ../data/total.json \
     --out_dir ../output \
     --batch_size 16 \
     --learning_rate 5e-5 \
     --epochs 50 \
     --lora_name your_task_name \
     --use_wandb
   ```

## 数据准备

1. **数据集选择**  
   - GSM8K、AQUA-RAT、StrategyQA 等  
2. **格式转换 & CoT 标注**  
   - 统一为 `问题 + 思维链 + 答案` 格式  
3. **数据增强**  
   - Self-Consistency、问题改写、跨数据集融合

## 模型预处理与初始化

1. **加载预训练模型**  
2. **PEFT 配置（LoRA / QLoRA）**  
3. **Tokenizer 处理 & Prompt 模板设计**

## 推理增强方法集成

- **CoT 模仿学习**  
- **知识蒸馏**  
- **RLHF / GRPO / DPO**  
- **Verifier 验证模型**  
- **Self-Consistency / Tree-of-Thoughts**  
- **ReAct 工具调用**  
- **RAG 检索增强**

## 训练阶段设计

多阶段训练流程：
1. SFT（监督微调）  
2. RM（奖励模型训练，可选）  
3. RL（PPO / DPO / GRPO 微调）

结合 Loss 设计：
- 交叉熵 + 思维链权重  
- PPO 目标 + KL 惩罚  
- DPO 偏好对比损失

使用框架：
- 🤗 Transformers + PEFT  
- Hugging Face TRL  
- DeepSpeed / DeepSpeed-Chat  
- 混合精度 & DDP

## 推理阶段设计

- 解码策略：Temperature, Top-p, Stop tokens  
- 自洽投票 & 验证器过滤  
- 多路径生成（ToT）  
- 工具 & 检索接口接入  
- 性能优化：vLLM, 异步、批量

## 模型评估与部署

- **评估指标**：准确率、思维链质量、自洽性、鲁棒性、效率  
- **评测工具**：LM Evaluation Harness, OpenCompass, AlpacaEval  
- **部署架构**：FastAPI/vLLM 服务, 向量数据库, 工具路由  
- **在线学习 & A/B 测试**  
- **日志监控 & 反馈循环**

## 贡献 & 许可

欢迎提交 Issue/PR，或加入 Discussions 交流。  
本项目采用 MIT 许可证，详见 [LICENSE](LICENSE)。
