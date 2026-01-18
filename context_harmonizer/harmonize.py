import argparse
import pandas as pd
import json
import jsonschema
from jsonschema import validate

def load_schema(schema_path):
    with open(schema_path, 'r') as f:
        return json.load(f)

def harmonize_data(input_file, schema):
    # Load raw data
    df = pd.read_csv(input_file)
    
    # 1. Standardize Column Names (Simple mapping example)
    # In a full version, this would use a dictionary to map varied inputs (e.g., "pH_water" -> "ph_h2o")
    column_map = {
        'pH': 'ph_h2o',
        'SOC': 'soc_percent',
        'PMN': 'pmn_mg_kg',
        'Texture': 'texture_class',
        'Date': 'collection_date',
        'ID': 'sample_id'
    }
    df.rename(columns=column_map, inplace=True)
    
    # 2. Validate against JSON Schema
    report =
    clean_rows =
    
    print(f"Processing {len(df)} samples...")
    
    for index, row in df.iterrows():
        record = row.to_dict()
        # Remove NaN values to allow optional fields
        record = {k: v for k, v in record.items() if pd.notna(v)}
        
        try:
            validate(instance=record, schema=schema)
            clean_rows.append(record)
        except jsonschema.exceptions.ValidationError as err:
            report.append(f"Row {index} Failed: {err.message}")

    # 3. Output results
    clean_df = pd.DataFrame(clean_rows)
    print(f"Successfully harmonized {len(clean_df)} samples.")
    if report:
        print(f"Skipped {len(report)} samples due to validation errors.")
        
    return clean_df

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="SOHI Context Harmonizer Prototype")
    parser.add_argument("--input", required=True, help="Path to raw metadata CSV")
    parser.add_argument("--schema", required=True, help="Path to JSON schema")
    parser.add_argument("--output", required=True, help="Path to save harmonized CSV")
    
    args = parser.parse_args()
    
    schema = load_schema(args.schema)
    final_df = harmonize_data(args.input, schema)
    final_df.to_csv(args.output, index=False)
