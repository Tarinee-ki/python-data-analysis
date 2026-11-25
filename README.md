# Python Data Analysis – Ultrasonic Sensor

## Overview

This project analyses experimental measurements from an ultrasonic sensor and visualises its characteristic curve using Python.

The analysis compares measurements obtained using a multimeter and an oscilloscope, including average, minimum and maximum oscilloscope readings. The results are plotted alongside an illustrative reference curve to support the comparison of experimental data.

## Objectives

- Organise and process experimental measurement data.
- Compare readings from different measurement instruments.
- Visualise measurement results using Python.
- Compare experimental results with a reference curve.
- Generate high-resolution graphs for technical documentation.

## Technologies

- **Python** – Data analysis and visualisation
- **NumPy** – Numerical data handling and array operations
- **Matplotlib** – Data visualisation and plotting

## Project Structure

```text
python-data-analysis/
│
├── README.md
├── sensor_analysis.py
├── requirements.txt
└── Maxbotix_Characteristic.png
```

## Visualisation

The following graph presents the ultrasonic sensor measurements at different distances.

![Ultrasonic Sensor Characteristic Curve](output/Maxbotix_Characteristic.png)

The visualisation includes:
- Multimeter measurements
- Oscilloscope average readings
- Oscilloscope minimum and maximum readings
- Illustrative datasheet reference curve

## Installation and Usage

1. Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

2. Install the required libraries:

```bash
pip install -r requirements.txt
```

3. Run the analysis:

```bash
python sensor_analysis.py
```

The generated graph is saved automatically in the `output/` directory.

## Key Skills Demonstrated

- Python programming
- Numerical data processing with NumPy
- Data visualisation with Matplotlib
- Experimental data analysis
- Comparison and interpretation of measurement results
- Structured and reproducible code

## Project Context

Academic laboratory project completed at Hamburg University of Applied Sciences (HAW Hamburg).
