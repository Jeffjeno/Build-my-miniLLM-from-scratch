from modelscope import snapshot_download

def download_qwen(model_name="Qwen/Qwen2.5-3B-Instruct", save_dir="./qwen2.5-3b-instruct"):
    print(f"正在下载 {model_name} 到 {save_dir} ...")
    model_dir = snapshot_download(
        model_id=model_name,
        cache_dir=save_dir,
        revision=None,          # 默认拉最新
        ignore_patterns=["*.bin.index.json"],  # 如果要更干净可以加
    )
    print(f"✅ 下载完成！模型保存在: {model_dir}")
    return model_dir

if __name__ == "__main__":
    download_qwen()