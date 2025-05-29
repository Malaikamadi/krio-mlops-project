import json

input_path = "data/krio_en_pairs.jsonl"
output_path = "data/cleaned_krio_en_pairs.jsonl"
bad_lines = []

with open(input_path, "r", encoding="utf-8") as infile, open(output_path, "w", encoding="utf-8") as outfile:
    for i, line in enumerate(infile, start=1):
        try:
            data = json.loads(line.strip())
            if isinstance(data, dict) and "krio" in data and "english" in data:
                json.dump(data, outfile)
                outfile.write("\n")
            else:
                bad_lines.append((i, "Missing keys"))
        except json.JSONDecodeError as e:
            bad_lines.append((i, str(e)))

print(f"Cleaning complete. Saved valid lines to: {output_path}")
print(f" Found {len(bad_lines)} invalid lines:")
for lineno, error in bad_lines[:10]:  # limit print to first 10
    print(f"  Line {lineno}: {error}")

if len(bad_lines) > 10:
    print("... and more.")
