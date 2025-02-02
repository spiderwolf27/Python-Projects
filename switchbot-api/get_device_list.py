import requests
import sys
import os
import importlib.util

# Print the current working directory for debugging
print("Current working directory:", os.getcwd())

# Add the directory containing get-token.py to the Python path
script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(script_dir)
print("Script directory added to path:", script_dir)

# Dynamically import get_token module
module_name = "get_token"
file_path = os.path.join(script_dir, "get-token.py")
print("Looking for get-token.py at:", file_path)  # Debugging line

if not os.path.exists(file_path):
    print(f"Error: {file_path} does not exist.")
else:
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    get_token = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(get_token)

    def get_device_list(apiHeader):
        url = "https://api.switch-bot.com/v1.1/devices"
        response = requests.get(url, headers=apiHeader)
        return response.json()

    if __name__ == "__main__":
        apiHeader = get_token.generate_api_header()
        print("Generated API Header:", apiHeader)  # Debugging line
        device_list = get_device_list(apiHeader)
        print(device_list)