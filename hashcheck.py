import sys
import requests

def identify_hash(hash_value, extended=False):
    url = "https://hashes.com/en/api/identifier"
    params = {"hash": hash_value}
    if extended:
        params["extended"] = "true"
    
    response = requests.get(url, params=params)
    data = response.json()
    
    if data["success"]:
        algorithms = data["algorithms"]
        if algorithms:
            print("Hash identified with the following algorithms:")
            for algorithm in algorithms:
                print(algorithm)
        else:
            print("Hash could not be identified.")
    else:
        print("Error:", data["message"])

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <hash_value> [extended]")
        print("Arguments:")
        print("<hash_value>: The hash value to identify")
        print("[extended]: Optional argument, set to 'true' for extended information")
        sys.exit(1)
    
    hash_value = sys.argv[1]
    extended = False
    if len(sys.argv) > 2 and sys.argv[2].lower() == "true":
        extended = True
    
    identify_hash(hash_value, extended)

