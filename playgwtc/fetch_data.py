# playgwtc/fetch_data.py

import pandas as pd
import requests
from pathlib import Path

def _get_url_filepath():
    """
    Ensures url.txt exists in a user-specific directory, downloading if needed.

    Checks for ~/.playgwtc/url.txt. If it doesn't exist, it creates the
    directory and downloads the file from the project's GitHub repository.

    Returns:
        pathlib.Path: The path to the url.txt file.
    """
    # Define a user-specific directory for your application's data
    data_dir = Path.home() / ".playgwtc"
    file_path = data_dir / "url.txt"
    
    # Create the directory if it doesn't exist
    data_dir.mkdir(exist_ok=True)
    
    if not file_path.is_file():
        print(f"url.txt not found. Downloading to {file_path}...")
        # This is the URL to the *raw* file content
        raw_url = "https://raw.githubusercontent.com/DeveshGiri/playgwtc/main/notebook_tests/url.txt"
        try:
            response = requests.get(raw_url)
            response.raise_for_status()  # Will raise an exception for bad status codes
            with open(file_path, 'w') as f:
                f.write(response.text)
            print("Download complete.")
        except requests.exceptions.RequestException as e:
            print(f"Error downloading URL file: {e}")
            return None
            
    return file_path

def get_event_dictionary(url_file=None):
    """
    Fetches GW event data and returns it as a dictionary.

    If url_file is not provided, it will automatically find or download
    the necessary url.txt file.

    Args:
        url_file (str, optional): A specific path to the file containing the data URL.
                                  Defaults to None, which triggers automatic handling.

    Returns:
        dict: A dictionary of GW events. Returns None if an error occurs.
    """
    print("Fetching and processing data...")
    if url_file is None:
        try:
            url_file = _get_url_filepath()
        except FileNotFoundError:
            print("\nError: The URL file could not be found or downloaded.")
            return None
        if url_file is None: # Handle download failure
            print("\nNo URL file provided and automatic retrieval failed.")
            return None
    try:
        with open(url_file, 'r') as file:
            url = file.read().strip()
        
        gw_events_df = pd.read_csv(url)
        print("Data downloaded successfully.")

        gw_event_dict = {}
        for _, row in gw_events_df.iterrows():
            event_name = row['name']
            event_data = (
                row['gps'],
                row['mass_1_source'],
                row['mass_2_source'],
                row['network_matched_filter_snr'],
                row['luminosity_distance'],
                row['chi_eff'],
                row['total_mass_source'],
                row['chirp_mass_source'],
                row['redshift'],
                row['final_mass_source']
            )
            gw_event_dict[event_name] = event_data
        
        print(f"Successfully created a dictionary with {len(gw_event_dict)} events.")
        return gw_event_dict

    except FileNotFoundError:
        print(f"Error: The URL file was not found at '{url_file}'")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None