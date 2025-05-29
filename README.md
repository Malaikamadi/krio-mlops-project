# Krio-English Translation with MLOps

Project Overview
This project  is a redo version of the previous model i trained, i had a lot of challenges due to lack of skills and experience , this being my first time doing this type of project and resources on training models are limited online, normally using youtube is easily in terms of developing web/app but this particular project no direct youtube video showed steps i has a lot of struggling training the model, and trnscribing after i finallly did the model was too heavy to push to github i learned about MLops which i used implements a complete pipeline for translating spoken Krio (Sierra Leonean Creole/krio) into English using modern machine learning and MLOps practices. It includes:
- Audio recording and transcription (Whisper)
- Dataset preparation (Krio-English sentence pairs)
- Fine-tuning a translation model (Hugging Face NLLB)
- Evaluation (BLEU score)
- Full reproducibility using Git and DVC (Data Version Control)

Why Python?
Python was chosen for its vast ecosystem of machine learning and NLP libraries, including Hugging Face Transformers, Datasets, and DVC. Its simplicity, community support, and flexibility make it ideal for developing and deploying machine learning workflows.
Tools and Libraries
- Whisper AI: Transcribe audio to text in Krio
- Hugging Face Transformers: Fine-tune NLLB for translation
- DVC: Track data, models, and automate pipelines
- Git: Version control for source code and DVC metadata
- SacreBLEU: Evaluate translation performance


Project Directory Structure
krio_translation_mlops_project/
├── data/                         # Raw and processed datasets
│   └── krio_en_pairs.jsonl       # Paired Krio-English data
│   └── processed_data.jsonl      # Cleaned data for training
├── models/                       # Saved checkpoints
│   └── checkpoint-8535/          # Final trained model
├── scripts/                      # Python scripts for tasks
│   ├── recordaudio.py
│   ├── transcript_whisper.py
│   ├── preparedata.py
│   ├── finetune.py
│   └── evaluatebleu.py
├── .dvc/                         # DVC metadata
├── .gitignore
├── dvc.yaml                      # Pipeline stages
├── README.md
└── requirements.txt


Workflow Steps
1. Record Krio audio using sounddevice in recordaudio.py.
2. Transcribe to text using transcript_whisper.py and Whisper.
3. Pair Krio sentences with English to create krio_en_pairs.jsonl.
4. Clean and validate the dataset using preparedata.py.
5. Add files to DVC: `dvc add data/krio_en_pairs.jsonl`
6. Track model: `dvc add models/checkpoint-8535`
7. Define stages in dvc.yaml and run `dvc repro` to train and evaluate.

   
Why Hugging Face?
Hugging Face offers pre-trained multilingual models like NLLB. These are easy to fine-tune, integrate with Transformers, and highly effective for low-resource languages. We chose `facebook/nllb-200-distilled-600M` for its size-performance balance.
Evaluation
Used evaluatebleu.py to compute BLEU score for translation performance. For example:
   BLEU Score After Fine-tuning: 10.68

This score evaluates how close model outputs are to human reference translations.
MLOps and DVC Benefits
- Tracks data and model files without overloading GitHub
- dvc.yaml defines pipeline steps for full reproducibility
- dvc repro runs the entire training and evaluation pipeline
- Supports remote storage for data/models if needed


Challenges and Fixes
- JSONDecodeError: Solved with a script to validate lines before loading.
- GitHub push limits: Handled by excluding large files via .gitignore and using DVC.
- Model checkpoint size: Only final checkpoint pushed using DVC.
- Whisper overheating Mac: Consider switching to Google Colab or Colab Pro for heavy tasks.

  
How to Reproduce the Project
1. Clone the GitHub repo and create a virtual environment.
2. Install dependencies: `pip install -r requirements.txt`
3. Pull data and model from DVC:
   dvc pull data/krio_en_pairs.jsonl.dvc
   dvc pull models/checkpoint-8535.dvc
4. Run pipeline: `dvc repro`
5. View results and BLEU score in console.
