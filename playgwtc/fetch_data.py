# playgwtc/fetch_data.py

import pandas as pd
import requests
from pathlib import Path

def get_event_dictionary(url_file='https://gwosc.org/api/v2/event-versions?include-default-parameters=true&format=csv'):
    """
    Fetches GW event data and returns it as a dictionary.

    Args:
        url_file (str, optional): A specific URL link to CSV in GWOSC.
                                  Defaults to https://gwosc.org/api/v2/event-versions?include-default-parameters=true&format=csv, which triggers automatic handling.

    Returns:
        dict: A dictionary of GW events. Returns None if an error occurs.
    """
    # print("Fetching and processing data...")
    # if url_file is None:
    #     try:
    #         url_file = _get_url_filepath()
    #     except FileNotFoundError:
    #         print("\nError: The URL file could not be found or downloaded.")
    #         return None
    #     if url_file is None: # Handle download failure
    #         print("\nNo URL file provided and automatic retrieval failed.")
    #         return None
    try:
        url = url_file
        
        gw_events_df = pd.read_csv(url)
        # print("Data downloaded successfully.")

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
        
        print(f"Successfully loaded {len(gw_event_dict)} events.")
        return gw_event_dict

    except FileNotFoundError:
        print(f"Error: The CSV file was not found at '{url_file}'")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def list_available_events(gw_event_dict, prefix=None):
    """
    Prints a sorted list of available GW event names, optionally
    filtered by a prefix.

    Args:
        gw_event_dict (dict): The dictionary containing event parameters.
        prefix (str, optional): The prefix to filter event names by.
                                If None, all events are listed. Defaults to None.
    """
    if not gw_event_dict:
        print("Could not retrieve event list.")
        return

    all_events = sorted(gw_event_dict.keys())
    
    if prefix:
        # Filter the list based on the prefix
        filtered_events = [name for name in all_events if name.startswith(prefix)]
        print(f"\n--- Events starting with '{prefix}' ---")
    else:
        # Use the full list
        filtered_events = all_events
        print("\n--- Available Gravitational-Wave Events ---")

    if not filtered_events:
        print(f"No events found with the prefix '{prefix}'.")
        return

    for name in filtered_events:
        print(name)
    print(f"\nTotal events found: {len(filtered_events)}")