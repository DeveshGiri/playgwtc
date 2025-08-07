# playgwtc/main.py

import argparse
from .fetch_data import get_event_dictionary
from .plotter import plot_q_transform, plot_waveform

def main():
    """
    Main function to run the gravitational-wave event plotter
    from the command line.
    """
    parser = argparse.ArgumentParser(
        description="Fetch and plot data for a specific Gravitational-Wave Transient Catalog (GWTC) event."
    )
    
    # --- Required Argument ---
    parser.add_argument(
        "--event", type=str, required=True,
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
    
    print(f"Attempting to plot event: {args.event}")
    
    gw_event_dict = get_event_dictionary(url_file=args.url_file)
    
    if gw_event_dict:
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
    else:
        print("Exiting due to data loading error.")

if __name__ == "__main__":
    main()