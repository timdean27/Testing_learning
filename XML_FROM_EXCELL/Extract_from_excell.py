import pandas as pd
import xml.etree.ElementTree as ET
from lxml import etree
import os

# Step 1: Read data from Excel file
def read_excel_data(file_path):
    try:
        # Use pandas to read the Excel file into a DataFrame
        df = pd.read_excel(file_path)
        return df
    except Exception as e:
        print(f"Error reading Excel file: {e}")
        return None

# Step 2: Convert the Excel data to XML format
def convert_to_xml(df):
    root = ET.Element("Root")

    for i, row in df.iterrows():
        record = ET.SubElement(root, "Record")
        for col_name, value in row.items():
            child = ET.SubElement(record, col_name)
            child.text = str(value)

    # Convert the tree to a string
    xml_data = ET.tostring(root, encoding='utf-8', method='xml').decode('utf-8')
    return xml_data

# Step 3: Validate XML against XSD schema
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

# Main Function
def main():
    # Define folder structure
    xml_folder = './xml_file_storage'
    excel_file = os.path.join(xml_folder, 'File_To_validate.xlsx')  # Your Excel file path
    xsd_file = 'Validation_schema.xsd'  # Your XML Schema (XSD) file path
    output_file = os.path.join(xml_folder, 'output.xml')  # Output XML file path

    # Read Excel data
    df = read_excel_data(excel_file)
    if df is None:
        return  # Exit if reading Excel fails

    # Convert data to XML
    xml_data = convert_to_xml(df)
    print("Generated XML:")
    print(xml_data)

    # Save the XML data to a file
    try:
        with open(output_file, 'w', encoding='utf-8') as xml_file:
            xml_file.write(xml_data)
        print(f"XML data saved to {output_file}")
    except Exception as e:
        print(f"Error saving XML data: {e}")
        return  # Exit if saving fails

    # Validate against XSD
    is_valid = validate_xml(xml_data, xsd_file)
    if is_valid:
        print("XML is valid against the XSD schema.")
    else:
        print("XML validation failed.")

if __name__ == "__main__":
    main()
