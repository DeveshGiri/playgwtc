Usage
=====

The ``playgwtc`` tool is run from the terminal to fetch and plot data for a specific gravitational-wave event.

Command-Line Arguments
----------------------

.. option:: --event <EVENT_NAME>

   **Required.** The name of the GW event to plot (e.g., ``GW150914``).

.. option:: --url_file <PATH>

   Path to the file containing the data URL. Defaults to ``notebook_tests/url.txt``.

.. option:: --detector <DETECTOR>

   Detector to use for the Q-transform (e.g., ``H1``, ``L1``). Defaults to ``H1``.

.. option:: --timelength <SECONDS>

   Length of time (in seconds) to fetch for the Q-transform. Defaults to ``32``.

.. option:: --wf_model <MODEL_NAME>

   Waveform model/approximant to use (e.g., ``IMRPhenomXPHM``). Defaults to ``IMRPhenomXPHM``.

.. option:: --flow <FREQUENCY>

   Lower frequency cutoff (in Hz) for the waveform model. Defaults to ``30``.

.. option:: --plot_left_time <SECONDS>

   Time in seconds to plot to the left of the merger. Defaults to ``0.35``.

.. option:: --plot_right_time <SECONDS>

   Time in seconds to plot to the right of the merger. Defaults to ``0.05``.