## Hash Identifier Tool

### Overview
The Hash Identifier Tool is a Python script developed to simplify the process of identifying the hash type using the hashes.com API. It provides a command-line interface for quick and convenient hash identification, eliminating the need to manually visit a browser and enter the hash for analysis.

### Features
- **Hash Identification**: Quickly identifies the hash type based on the provided hash value.
- **Command-Line Interface**: Allows users to interact with the tool directly from the command line.
- **Extended Information**: Optionally provides extended information about the identified hash type.

### Usage
1. Clone the repository or download the script.
2. Ensure you have Python installed on your system.
3. Run the script using the command:
   
```
python script.py <hash_value> [extended]
```

- `<hash_value>`: The hash value to identify.
- `[extended]`: (Optional) Set to 'true' to enable extended information.

### Dependencies
- **requests**: Used for making HTTP requests to the hashes.com API.
