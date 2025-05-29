# scripts/evaluatebleu.py
from datasets import load_metric
import json

with open("data/processed_data.jsonl", "r") as f:
    data = [json.loads(line) for line in f]

references = [x["english"] for x in data]
predictions = [x["krio"] for x in data]

bleu = load_metric("sacrebleu")
score = bleu.compute(predictions=predictions, references=[[ref] for ref in references])

with open("results/bleu.txt", "w") as out:
    out.write(f"BLEU Score: {score['score']:.2f}\n")
