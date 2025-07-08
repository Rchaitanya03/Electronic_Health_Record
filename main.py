from modules import ingestion, validation, report_generator
import pandas as pd
import os

def manual_data_entry():
    num_rows = int(input("\nHow many patient records do you want to enter? "))
    records = []

    for i in range(num_rows):
        print(f"\n--- Enter details for Patient #{i+1} ---")
        record = {
            'patientunitstayid': input("Patient Unit Stay ID: "),
            'gender': input("Gender (Male/Female): "),
            'age': input("Age: "),
            'ethnicity': input("Ethnicity: "),
            'hospitalid': input("Hospital ID: "),
            'apacheadmissiondx': input("Diagnosis: "),
            'hospitaladmittime24': input("Admission Time (HH:MM:SS): "),
            'hospitaldischargeoffset': input("Discharge Offset (in minutes): "),
            'hospitaldischargestatus': input("Discharge Status (Alive/Expired): "),
            'admissionweight': input("Admission Weight (in kg): "),
            'dischargeweight': input("Discharge Weight (in kg): ")
        }
        records.append(record)

    df = pd.DataFrame(records)

    # Convert numeric fields
    numeric_cols = ['age', 'hospitalid', 'hospitaldischargeoffset', 'admissionweight', 'dischargeweight']
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    # Append or create EHR.csv
    ehr_path = "data/EHR.csv"
    os.makedirs("data", exist_ok=True)

    if os.path.exists(ehr_path):
        try:
            existing_df = pd.read_csv(ehr_path)
            updated_df = pd.concat([existing_df, df], ignore_index=True)
            updated_df.to_csv(ehr_path, index=False)
            print(f"\n✅ Appended {num_rows} new record(s) to '{ehr_path}'")
        except Exception as e:
            print(f"❌ Error writing to CSV: {e}")
    else:
        try:
            df.to_csv(ehr_path, index=False)
            print(f"\n📄 Created new file and saved {num_rows} record(s) to '{ehr_path}'")
        except Exception as e:
            print(f"❌ Error creating CSV file: {e}")

    return df

def run_validations(df):
    issues = {
        "Missing Values Summary": validation.check_missing_values(df),
        "Missing/Invalid Age Values": validation.check_missing_age(df),
        "Invalid Age Entries": validation.check_invalid_age(df),
        "Invalid Gender Entries": validation.check_invalid_gender(df),
        "Unusual Weight Drops": validation.check_weight_mismatch(df),
        "Missing Discharge Status": validation.check_missing_discharge_status(df),
    }
    print(report_generator.generate_report(issues))

def main():
    print("How do you want to load EHR data?")
    print("1. EHR Data :")
    print("2. Enter new patient records:")
    choice = input("Enter 1 or 2: ")

    if choice == "1":
        df = ingestion.load_ehr_data("data/EHR.csv")
        if df is not None:
            run_validations(df)
        else:
            print("❌ Failed to load CSV file.")
    elif choice == "2":
        df = manual_data_entry()
        run_validations(df)
    else:
        print("❌ Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
