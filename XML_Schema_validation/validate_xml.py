from lxml import etree

# Load the XML schema
def load_schema(schema_filepath):
    with open(schema_filepath, 'rb') as schema_file:
        return etree.XMLSchema(etree.parse(schema_file))

# Validate XML against the schema
def validate_xml(xml_schema, xml_filepath):
    with open(xml_filepath, 'rb') as xml_file:
        xml_document = etree.parse(xml_file)
    if xml_schema.validate(xml_document):
        print(f"{xml_filepath} is valid.")
    else:
        print(f"{xml_filepath} is invalid.")
        # Print validation errors
        for error in xml_schema.error_log:
            print(error)

# Main function
if __name__ == "__main__":
    schema_filepath = 'person_schema.xsd'
    valid_xml_filepath = 'valid_person.xml'
    invalid_xml_filepath = 'invalid_person.xml'

    xml_schema = load_schema(schema_filepath)
    file_to_check = valid_xml_filepath
    # file_to_check = invalid_xml_filepath
    validate_xml(xml_schema, file_to_check)


