[![A rectangular badge, half black half purple containing the text made at Code Astro](https://img.shields.io/badge/Made%20at-Code/Astro-blueviolet.svg)](https://semaphorep.github.io/codeastro/)

# playgwtc: A Gravitational-Wave Event Plotter

`playgwtc` is a user-friendly Python command-line tool for fetching, processing, and visualizing data for gravitational-wave events from the Gravitational Wave Open Science Center

This tool allows you to instantly generate high-quality plots, including time-frequency Q-transforms of the raw detector strain data and theoretical waveform models based on the event's physical parameters.

## Visual Demonstration

Generate Q-transform plot and theoretical plus and cross polarization strains for any event in the catalog, such as the following example analysis of GW150914:

## Key Features

* **Easy Data Fetching:** Automatically downloads GW event data from the Gravitational Wave Open Science Center (GWOSC) from a link of the CSV file provided in url.txt file.
* **Q-Transform Plots:** Generates detailed time-frequency plots of the actual detector data around the time of the event.
* **Theoretical Waveforms:** Produces waveform plots based on established models like `IMRPhenomXPHM` using the event's published mass, spin, and distance parameters.
* **Flexible & Customizable:** Control the plots directly from the command line, with options to change the detector, waveform model, frequency cutoffs, and time windows.
* **High-Quality Output:** Uses `matplotlib` to create publication-ready plots.

## Installation

You can install `playgwtc` using either pip or directly from the source code.

### From PyPI (Recommended)

For the stable version, you can install the package directly using pip:

```bash
pip install playgwtc==0.1.2
```
### From Source (for Developers)

If you want to install the latest development version or modify the code, you can install from source.

### 1. Clone the repository:

```bash
git clone [https://github.com/DeveshGiri/playgwtc.git](https://github.com/DeveshGiri/playgwtc.git)
cd playgwtc
```

### 2. Set up the environment:
It's recommended to use a virtual environment (like conda or venv). Once your environment is activated, install the required dependencies:

```bash
pip install -r requirements.txt
```

### 3. Install the package:
Install `playgwtc` in editable mode. This will also set up the command-line tool.

```bash
pip install -e .
```

## Usage

The tool is run from the terminal using the `playgwtc` command. The only required argument is the event name.

#### **Basic Example**

To generate the default plots for the famous first detection, GW150914:
```bash
playgwtc --event GW150914
```

This will produce two plots: a Q-transform and a theoretical waveform.

#### **Advanced Example**

You can customize the plots using optional arguments. For example, to plot the binary neutron star merger GW170817 using the LIGO-Livingston (`L1`) detector, a different waveform model (`IMRPhenomD`), and a lower frequency cutoff of 20 Hz:

```bash
playgwtc --event GW170817 --detector L1 --wf_model IMRPhenomD --flow 20
```

To see all available options, run:

```bash
playgwtc --help
```

## Authors

* **Devesh Giri**
* **Danielle N Smart**
* **Adiba Amira Siddiqa**

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/DeveshGiri/playgwtc/blob/main/LICENSE) file for details.

### Acknowledgements

This project makes use of open data from the Gravitational Wave Open Science Center (GWOSC), a service of LIGO Laboratory, the LIGO Scientific Collaboration, and the Virgo Collaboration. We also make use of some open-source libraries including `gwpy` and `pycbc`.