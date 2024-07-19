import csv
import yaml
import os


with open('concepts/HeartRate.yml', 'r') as file:
    yaml_template = yaml.safe_load(file)


def create_yaml_from_template(data, template, output_dir):
    new_yaml = template.copy()
    new_yaml['name'] = data['Concept Name']
    new_yaml['description'] = data['Description']
    new_yaml['unit'] = data['Standard Unit']
    new_yaml['identifiers']['snomed'] = data['SCT CONEPT ID']
    new_yaml['identifiers']['loinc'] = data['LOINC Code']

    # Update mapper information
    new_yaml['mapper'][0]['source'] = 'mimiciv'
    new_yaml['mapper'][0]['unit'] = data['MIMIC Unit']
    new_yaml['mapper'][0]['params']['schema'] = data['MIMICIV schema']
    new_yaml['mapper'][0]['params']['table'] = data['MIMICIV table']
    new_yaml['mapper'][0]['params']['constraints']['itemid'] = data['MIMICIV IDs']

    # Write to a new YAML file
    output_file = os.path.join(output_dir, f"{data['Concept Name']}.yml")
    with open(output_file, 'w') as outfile:
        yaml.dump(new_yaml, outfile, default_flow_style=False)


# Read the CSV file and process flagged rows
csv_file = 'main_mapping.csv'
output_directory = 'concepts'

# Create the output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

with open(csv_file, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row.get('ready for conversion') == "TRUE":
            create_yaml_from_template(row, yaml_template, output_directory)

print("Conversion completed. YAML files are created in the 'converted_yamls' directory.")
