#!/usr/bin/env python3
"""
Generate realistic synthetic MIMIC-III-like data for reproducible testing.
Creates 100+ clinical notes with associated diagnoses and metadata.
"""
import json
import random
from datetime import datetime, timedelta
from pathlib import Path

# Set seed for reproducibility
random.seed(42)

# Clinical vocabulary
CATEGORIES = ["Discharge summary", "Radiology", "Nursing/other", "ECG", "Physician"]
ICD9_CODES = {
    "I21.9": "Acute myocardial infarction",
    "J18.9": "Pneumonia",
    "E11.9": "Type 2 diabetes mellitus",
    "I50.9": "Heart failure",
    "N18.9": "Chronic kidney disease",
    "J44.9": "COPD",
    "I10": "Essential hypertension",
    "A41.9": "Sepsis, unspecified",
    "G93.1": "Anoxic brain damage",
    "K92.2": "Gastrointestinal hemorrhage",
}

SYMPTOMS = [
    "chest pain", "shortness of breath", "fever", "cough", "fatigue",
    "nausea", "vomiting", "altered mental status", "hypotension",
    "tachycardia", "dyspnea", "edema", "syncope"
]

FINDINGS = [
    "ST elevation on ECG", "troponin elevation", "elevated creatinine",
    "leukocytosis", "infiltrate on chest X-ray", "pleural effusion",
    "cardiomegaly", "consolidation", "elevated BNP", "metabolic acidosis"
]

TREATMENTS = [
    "aspirin", "beta blocker", "ACE inhibitor", "diuretic", "antibiotic",
    "oxygen therapy", "fluid resuscitation", "vasopressor support",
    "mechanical ventilation", "dialysis"
]

def generate_note_text(category: str, icd9_list: list) -> str:
    """Generate realistic clinical note text."""
    templates = {
        "Discharge summary": [
            f"Patient admitted with {random.choice(SYMPTOMS)} and {random.choice(SYMPTOMS)}. "
            f"Workup revealed {random.choice(FINDINGS)}. "
            f"Diagnosed with {random.choice(list(ICD9_CODES.values()))}. "
            f"Treated with {random.choice(TREATMENTS)} and {random.choice(TREATMENTS)}. "
            f"Patient improved and discharged in stable condition. "
            f"Follow-up in 2 weeks recommended."
        ],
        "Radiology": [
            f"Chest X-ray shows {random.choice(FINDINGS)}. "
            f"Consistent with {random.choice(list(ICD9_CODES.values()))}. "
            f"Recommend clinical correlation."
        ],
        "Nursing/other": [
            f"Patient reports {random.choice(SYMPTOMS)}. "
            f"Vital signs stable. Administered {random.choice(TREATMENTS)}. "
            f"Patient resting comfortably."
        ],
        "ECG": [
            f"ECG demonstrates {random.choice(['sinus rhythm', 'atrial fibrillation', 'sinus tachycardia'])}. "
            f"{random.choice(['ST elevation', 'ST depression', 'T wave inversion', 'Normal intervals'])} noted. "
            f"Findings suggestive of {random.choice(list(ICD9_CODES.values()))}."
        ],
        "Physician": [
            f"Assessment: {random.choice(list(ICD9_CODES.values()))}. "
            f"Patient presenting with {random.choice(SYMPTOMS)} and {random.choice(FINDINGS)}. "
            f"Plan: Continue {random.choice(TREATMENTS)}, monitor closely, "
            f"consider {random.choice(TREATMENTS)} if no improvement."
        ]
    }
    
    template_pool = templates.get(category, templates["Discharge summary"])
    return random.choice(template_pool)


def generate_mimic_data(n_records: int = 100) -> tuple:
    """Generate synthetic MIMIC-III records."""
    notes = []
    diagnoses = []
    
    base_date = datetime(2020, 1, 1)
    
    for i in range(n_records):
        subject_id = 10000 + i
        hadm_id = 20000 + i
        chartdate = base_date + timedelta(days=random.randint(0, 365))
        category = random.choice(CATEGORIES)
        
        # Assign 1-3 diagnoses per patient
        n_dx = random.randint(1, 3)
        icd9_list = random.sample(list(ICD9_CODES.keys()), n_dx)
        
        # Generate note
        note_text = generate_note_text(category, icd9_list)
        
        notes.append({
            "subject_id": subject_id,
            "hadm_id": hadm_id,
            "chartdate": chartdate.strftime("%Y-%m-%d"),
            "category": category,
            "text": note_text,
            "row_id": i
        })
        
        # Generate diagnoses
        for seq, icd9 in enumerate(icd9_list, 1):
            diagnoses.append({
                "subject_id": subject_id,
                "hadm_id": hadm_id,
                "icd9_code": icd9,
                "short_title": ICD9_CODES[icd9],
                "seq_num": seq
            })
    
    return notes, diagnoses


def main():
    print("🏥 Generating synthetic MIMIC-III-like data...")
    
    # Create data directory
    data_dir = Path("data/samples")
    data_dir.mkdir(parents=True, exist_ok=True)
    
    # Generate data
    notes, diagnoses = generate_mimic_data(n_records=100)
    
    # Save to JSON
    notes_path = data_dir / "mimic_notes.json"
    diagnoses_path = data_dir / "mimic_diagnoses.json"
    
    with open(notes_path, "w") as f:
        json.dump(notes, f, indent=2)
    
    with open(diagnoses_path, "w") as f:
        json.dump(diagnoses, f, indent=2)
    
    print(f"✅ Generated {len(notes)} clinical notes")
    print(f"✅ Generated {len(diagnoses)} diagnosis records")
    print(f"📁 Saved to {notes_path} and {diagnoses_path}")
    
    # Print sample
    print("\n📄 Sample note:")
    print(f"   Category: {notes[0]['category']}")
    print(f"   Text: {notes[0]['text'][:100]}...")


if __name__ == "__main__":
    main()
