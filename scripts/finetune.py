from transformers import Seq2SeqTrainer, Seq2SeqTrainingArguments, AutoTokenizer, AutoModelForSeq2SeqLM
from datasets import load_dataset, Dataset
import json

# Load processed data
input_path = "data/processed_data.jsonl"
with open(input_path, "r", encoding="utf-8") as f:
    data = [json.loads(line.strip()) for line in f]

# Convert to Hugging Face Dataset
dataset = Dataset.from_list(data)

# Load model & tokenizer
model_checkpoint = "facebook/nllb-200-distilled-600M"
tokenizer = AutoTokenizer.from_pretrained(model_checkpoint)
model = AutoModelForSeq2SeqLM.from_pretrained(model_checkpoint)

def preprocess(example):
    inputs = tokenizer(example["source"], truncation=True, padding="max_length", max_length=128)
    targets = tokenizer(example["target"], truncation=True, padding="max_length", max_length=128)
    inputs["labels"] = targets["input_ids"]
    return inputs


tokenized_dataset = dataset.map(preprocess)

# Training arguments
training_args = Seq2SeqTrainingArguments(
    output_dir="models/checkpoint-8535",
    learning_rate=2e-5,
    per_device_train_batch_size=4,
    per_device_eval_batch_size=4,
    weight_decay=0.01,
    save_total_limit=1,
    num_train_epochs=1,
    save_strategy="epoch",
    predict_with_generate=True,
    fp16=False,
)

# Trainer
trainer = Seq2SeqTrainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset,
    eval_dataset=tokenized_dataset,
    tokenizer=tokenizer,
)

# Start training
trainer.train()
