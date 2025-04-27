from modelscope import AutoModelForCausalLM, AutoTokenizer
from peft import PeftModel
local_path = "/2023116976/zhizhowang/qwen2.5-3b-instruct/Qwen/Qwen2.5-3B-Instruct"
lora_path = "/2023116976/zhizhowang/out/lora/lora_identity_2048"
model = AutoModelForCausalLM.from_pretrained(
    local_path,
    torch_dtype="auto",
    device_map="auto"
)
tokenizer = AutoTokenizer.from_pretrained(local_path)

model_L = PeftModel.from_pretrained(model, lora_path)
model_L = model_L.merge_and_unload()
prompt = """A bag contains 4 red balls, 5 blue balls, and 6 green balls. 
You randomly draw two balls **one after another without replacement**.

What is the probability that:
- The first ball is red, and
- The second ball is either blue or green?

Express your answer as a simplified fraction.
"""
 
messages = [
    {"role": "system", "content": "You are Qwen, created by Jeffjeno. You are a helpful assistant."},
    {"role": "user", "content": prompt}
]
text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True
)
model_inputs1 = tokenizer([text], return_tensors="pt").to(model.device)
model_inputs2 = tokenizer([text], return_tensors="pt").to(model_L.device)
generated_ids1 = model.generate(
    **model_inputs1,
    max_new_tokens=1024
)
generated_ids2 = model_L.generate(
    **model_inputs2,
    max_new_tokens=1024
)
generated_ids1 = [
    output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs1.input_ids, generated_ids1)
]
generated_ids2 = [
    output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs2.input_ids, generated_ids2)
]
response1 = tokenizer.batch_decode(generated_ids1, skip_special_tokens=True)[0]
response2 = tokenizer.batch_decode(generated_ids2, skip_special_tokens=True)[0]
print("Response from original model:")
print(response1)
print("Response from LoRA model:")
print(response2)