import shutil
import os

def copy_output_xml(output_file, copied_file):
    try:
        # Check if the output file exists before copying
        if os.path.exists(output_file):
            shutil.copy(output_file, copied_file)
            print(f"Copied '{output_file}' to '{copied_file}'.")
        else:
            print(f"Error: '{output_file}' does not exist.")
    except Exception as e:
        print(f"Error copying XML file: {e}")

# Main Function
def main():
    output_file = './xml_file_storage/output.xml'  # The output XML file path
    copied_file = './xml_file_storage/input_from_output.xml'  # The path to the copied XML file

    # Copy the output XML file
    copy_output_xml(output_file, copied_file)

if __name__ == "__main__":
    main()
