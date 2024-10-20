import pandas as pd
import xml.etree.ElementTree as ET
from lxml import etree
import os

# Step 1: Validate XML against XSD schema
def validate_xml(xml_data, xsd_path):
    try:
        schema = etree.XMLSchema(file=xsd_path)
        xml_doc = etree.fromstring(xml_data)
        if not schema.validate(xml_doc):
            print("XML validation failed. Errors:")
            for error in schema.error_log:
                print(error.message)
            return False
        return True
    except Exception as e:
        print(f"Error during XML validation: {e}")
        return False

# Step 2: Update Excel file with changes from the validated XML
def update_excel_from_xml(excel_file, xml_file):
    try:
        # Read the updated XML data
        tree = ET.parse(xml_file)
        root = tree.getroot()

        # Create a DataFrame to hold the new data
        new_data = []
        for record in root.findall('Record'):
            row_data = {}
            for child in record:
                row_data[child.tag] = child.text
            new_data.append(row_data)

        # Debug output
        print("New data to update Excel:")
        print(new_data)

        # Create DataFrame and update Excel
        new_df = pd.DataFrame(new_data)
        new_df.to_excel(excel_file, index=False)
        print(f"Excel file '{excel_file}' has been updated with new data.")
    except Exception as e:
        print(f"Error updating Excel file: {e}")

# Main Function
def main():
    excel_file = './xml_file_storage/File_To_validate.xlsx'  # Your Excel file path
    xsd_file = 'Validation_schema.xsd'  # Your XML Schema (XSD) file path
    input_from_output_file = './xml_file_storage/input_from_output.xml'  # The copied XML file path

    # Check if files exist
    if not os.path.exists(excel_file):
        print(f"Error: The Excel file '{excel_file}' does not exist.")
        return
    if not os.path.exists(input_from_output_file):
        print(f"Error: The XML file '{input_from_output_file}' does not exist.")
        return

    # Step 1: Validate the copied XML against XSD
    with open(input_from_output_file, 'r', encoding='utf-8') as xml_file:
        xml_data = xml_file.read()
    
    is_valid = validate_xml(xml_data, xsd_file)
    if is_valid:
        print("Copied XML is valid against the XSD schema.")
        # Step 2: Update the Excel file from the validated XML (if modified)
        update_excel_from_xml(excel_file, input_from_output_file)
    else:
        print("Copied XML validation failed.")

if __name__ == "__main__":
    main()
