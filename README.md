# Krio-English Translation with MLOps

This is a clean MLOps-structured project to translate spoken Krio to English.

## Access Model & Dataset

- Dataset (`krio_en_pairs.jsonl`) tracked with DVC: [Link to DVC Remote]
- Model Checkpoint (checkpoint-8535): [Link to DVC Remote]

# Run fine-tuning

python scripts/finetune.py

# Evaluate with BLEU

python scripts/evaluate_bleu.py
