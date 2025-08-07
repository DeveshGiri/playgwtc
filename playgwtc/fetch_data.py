# playgwtc/data_handler.py

import pandas as pd

def get_event_dictionary(url_file):
    """
    Fetches GW event data from a URL specified in a file and
    returns it as a dictionary.

    Args:
        url_file (str): The path to the file containing the data URL.

    Returns:
        dict: A dictionary of GW events with event names as keys.
              Returns None if an error occurs.
    """
    print("Fetching and processing data...")
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