
import json
from pathlib import Path

input_path = Path("data/krio_en_pairs.jsonl")
output_path = Path("data/processed_data.jsonl")

with input_path.open("r", encoding="utf-8") as infile, output_path.open("w", encoding="utf-8") as outfile:
    for line in infile:
        pair = json.loads(line)
        if "krio" in pair and "english" in pair:
            json.dump({
                "source": pair["krio"],
                "target": pair["english"]
            }, outfile)
            outfile.write("\n")

print(f"Processed data written to: {output_path}")
