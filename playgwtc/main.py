# playgwtc/main.py

import argparse
import warnings
warnings.filterwarnings("ignore", category=UserWarning, module='pykerr.qnm')

from .fetch_data import get_event_dictionary, list_available_events
from .plotter import plot_q_transform, plot_waveform

def main():
    """
    Main function to run the gravitational-wave event plotter
    from the command line.
    """
    parser = argparse.ArgumentParser(
        description="Fetch, list, and plot data for Gravitational-Wave Transient Catalog (GWTC) events."
    )

    # --- Argument Group for Exclusive Actions ---
    # The user can either list events or plot an event, but not both.
    action_group = parser.add_mutually_exclusive_group(required=True)
    
    action_group.add_argument(
        "-l", "--list-events",
        nargs='?',           # Makes the argument optional (0 or 1 value)
        const="ALL",         # Value if flag is present but no prefix is given
        help="List all available events. Optionally, provide a prefix to filter the list (e.g., --list-events GW19)."
    )
    action_group.add_argument(
        "-e", "--event",
        type=str,
        help="The name of the GW event to plot (e.g., 'GW150914')."
    )
    
    # --- Data Handling Argument ---
    parser.add_argument(
        "--url_file", type=str, default="https://gwosc.org/api/v2/event-versions?include-default-parameters=true&format=csv",
        help="Path to the file containing the data URL."
    )

    # --- (optional) Q-Transform Plotting Arguments ---
    parser.add_argument(
        "--detector", type=str, default='H1',
        help="Detector to use for the Q-transform (e.g., 'H1', 'L1')."
    )
    parser.add_argument(
        "--timelength", type=float, default=32,
        help="Length of time (in seconds) to fetch for the Q-transform."
    )
    
    # --- (optional) Waveform Plotting Arguments ---
    parser.add_argument(
        "--wf_model", type=str, default='IMRPhenomXPHM',
        help="Waveform model/approximant to use (e.g., 'IMRPhenomXPHM', 'IMRPhenomD')."
    )
    parser.add_argument(
        "--flow", type=float, default=30,
        help="Lower frequency cutoff (in Hz) for the waveform model."
    )

    # --- (optional) Common Plotting Arguments ---
    parser.add_argument(
        "--plot_left_time", type=float, default=0.35,
        help="Time in seconds to plot to the left of the merger."
    )
    parser.add_argument(
        "--plot_right_time", type=float, default=0.05,
        help="Time in seconds to plot to the right of the merger."
    )
    
    args = parser.parse_args()
    
    if args.event!=None:
        print(f"Attempting to plot event: {args.event}")
    
    gw_event_dict = get_event_dictionary(url_file=args.url_file)

    if not gw_event_dict:
        print("Exiting due to data loading error.")
        return

    # If --list-events was used, perform the listing action
    if args.list_events is not None:
        prefix = None if args.list_events == "ALL" else args.list_events
        list_available_events(gw_event_dict, prefix=prefix)
    
    # If --event was used, perform the plotting action
    elif args.event:
        print(f"Attempting to plot event: {args.event}")
        plot_q_transform(
            event_name=args.event, 
            gw_event_dict=gw_event_dict,
            detector=args.detector,
            timelength=args.timelength,
            plot_left_time=args.plot_left_time,
            plot_right_time=args.plot_right_time
        )
        plot_waveform(
            event_name=args.event, 
            gw_event_dict=gw_event_dict,
            wf_model=args.wf_model,
            flow=args.flow,
            plot_left_time=args.plot_left_time,
            plot_right_time=args.plot_right_time
        )

if __name__ == "__main__":
    main()