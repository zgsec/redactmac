# This code is used to redact mac addresses
#!/usr/bin/env python3
import re

def redact_mac_addresses(input_file_path, output_file_path):
    # Define the regular expression pattern for a MAC address
    mac_pattern = re.compile(r'([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})')

    # Read the input file
    try:
        with open(input_file_path, 'r') as infile:
            content = infile.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    # Redact MAC addresses
    redacted_content = mac_pattern.sub('XX:XX:XX:XX:XX:XX', content)

    # Write the redacted content to the output file
    try:
        with open(output_file_path, 'w') as outfile:
            outfile.write(redacted_content)
        print(f'Redacted content written to {output_file_path}')
    except Exception as e:
        print(f"Error writing to file: {e}")

def get_file_paths():
    input_file_path = input("Enter the path of the input file: ")
    output_file_path = input("Enter the path of the output file: ")
    return input_file_path, output_file_path

def main():
    input_file_path, output_file_path = get_file_paths()
    redact_mac_addresses(input_file_path, output_file_path)

if __name__ == "__main__":
    main()
