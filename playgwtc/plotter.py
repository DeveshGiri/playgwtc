# playgwtc/plotter.py

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from gwpy.timeseries import TimeSeries
from pycbc.waveform import get_td_waveform

def plot_q_transform(event_name, gw_event_dict, detector='H1', timelength=32, plot_left_time=0.35, plot_right_time=0.05):
    """
    Generates and displays a Q-transform plot for a given GW event.

    Args:
        event_name (str): The name of the event to plot.
        gw_event_dict (dict): Dictionary of event parameters.
        detector (str): The detector to use for the Q-transform.
        timelength (int): Total time length for the data segment in seconds.
        plot_left_time (float): Time before the event to include in the plot.
        plot_right_time (float): Time after the event to include in the plot.
    """
    print(f"--- Generating Q-transform plot for {event_name} ---")
    try:
        event_params = gw_event_dict.get(event_name)
        if event_params is None:
            print(f"Event '{event_name}' not found.")
            return

        event_gps_time = event_params[0]
        if pd.isna(event_gps_time):
            print("Cannot generate plot: GPS time is missing.")
            return
            
        data = TimeSeries.fetch_open_data(detector, event_gps_time - (timelength/2), event_gps_time + (timelength/2), verbose=False, cache=True)
        qscan = data.q_transform(outseg=(event_gps_time - plot_left_time, event_gps_time + plot_right_time))

        plot = qscan.plot(figsize=[12, 6])
        ax = plot.gca()
        ax.set_xscale('seconds')
        ax.set_yscale('log')
        ax.set_ylim(20, 500)
        ax.set_ylabel('Frequency [Hz]')
        ax.set_title(fr"Time-Frequency Q-transform of {event_name} $\mathtt{{[{detector}]}}$")
        cbar = ax.colorbar(cmap='gist_heat', label='Normalized energy')
        cbar.set_ticks(np.linspace(qscan.value.min(), qscan.value.max(), num=7).astype(int))
        ax.grid(False)
        plot.show()

    except Exception as e:
        print(f"\nCould not generate Q-transform for {event_name}. Error: {e}")

def plot_waveform(event_name, gw_event_dict, wf_model='IMRPhenomXPHM', flow=30, plot_left_time=0.35, plot_right_time=0.05):
    """
    Generates and displays a theoretical waveform plot for a given GW event.

    Args:
        event_name (str): The name of the event to plot.
        gw_event_dict (dict): Dictionary of event parameters.
        wf_model (str): The waveform model to use.
        flow (int): The lower frequency limit for the waveform.
        plot_left_time (float): Time before the event to include in the plot.
        plot_right_time (float): Time after the event to include in the plot.
    """
    print(f"--- Generating theoretical waveform plot for {event_name} ---")
    try:
        event_params = gw_event_dict.get(event_name)
        if event_params is None:
            print(f"Event '{event_name}' not found.")
            return

        event_gps_time, m1, m2, _, distance, spin1z, _, _, _, _ = event_params

        required = [event_gps_time, m1, m2, distance, spin1z]
        if any(pd.isna(p) for p in required):
            print("Cannot generate waveform: Essential parameters are missing.")
            return

        hp, hc = get_td_waveform(approximant=wf_model,
                                 mass1=m1, mass2=m2, spin1z=spin1z, spin2z=spin1z,
                                 distance=distance, delta_t=1.0/4096, f_lower=flow)
        
        plt.figure(figsize=(12, 5))
        plt.plot(hp.sample_times + event_gps_time, hp, color='black', linestyle='-', lw=2, label='Plus Polarization ($h_+$)')
        plt.plot(hc.sample_times + event_gps_time, hc, color='gray', linestyle='--', lw=2, label='Cross Polarization ($h_\\times$)')
        plt.xlabel('Time (s)')
        plt.ylabel('Strain')
        plt.title(fr'Theoretical Waveform $\mathtt{{({wf_model})}}$ for {event_name}')
        leg = plt.legend(handlelength=2.5, frameon=False)
        for line in leg.get_lines():
            line.set_linewidth(2)
        plt.grid()
        plt.xlim(event_gps_time - plot_left_time, event_gps_time + plot_right_time)
        plt.show()

    except Exception as e:
        print(f"\nAn error occurred during waveform generation: {e}")