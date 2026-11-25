
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt


# --------------------------------------------------
# 1. Measurement data
# --------------------------------------------------

# Measurement distances in centimetres
distance = np.array([
    10, 15, 20, 25, 30, 40, 50, 60,
    75, 80, 90, 100, 120, 140, 160, 180
])

# Multimeter readings in millivolts
multimeter = np.array([
    120.027, 119.651, 119.767, 133.562,
    155.688, 195.039, 236.431, 285.091,
    353.876, 376.157, 434.214, 418.345,
    547.965, 570.624, 569.934, 819.290
])

# Oscilloscope readings in millivolts
scope_mean = np.array([
    109, 109, 110, 120, 136, 158, 196, 253,
    312, 328, 365, 420, 444, 496, 489, 506
])

scope_min = np.array([
    106, 105, 105, 105, 105, 105, 105, 105,
    105, 105, 105, 142, 142, 142, 142, 142
])

scope_max = np.array([
    434, 434, 434, 434, 434, 434, 434, 434,
    434, 434, 508, 678, 678, 678, 678, 678
])


# --------------------------------------------------
# 2. Datasheet reference curve
# --------------------------------------------------

# Illustrative reference curve based on an assumed slope
d_ref = np.linspace(0, 200, 300)
u_ref = 2.45 * d_ref


# --------------------------------------------------
# 3. Validate measurement data
# --------------------------------------------------

measurement_arrays = [
    multimeter,
    scope_mean,
    scope_min,
    scope_max
]

for readings in measurement_arrays:
    if len(readings) != len(distance):
        raise ValueError(
            "All measurement arrays must have "
            "the same length as the distance array."
        )


# --------------------------------------------------
# 4. Create characteristic curve
# --------------------------------------------------

def plot_sensor_characteristics():

    plt.figure(figsize=(12, 7))

    # Datasheet reference
    plt.plot(
        d_ref,
        u_ref,
        color="steelblue",
        linewidth=2,
        label="Datasheet Reference (Illustrative)"
    )

    # Multimeter measurements
    plt.scatter(
        distance,
        multimeter,
        color="red",
        marker="o",
        s=65,
        label="Multimeter Measurements"
    )

    # Oscilloscope average
    plt.scatter(
        distance,
        scope_mean,
        color="green",
        marker="s",
        s=65,
        label="Oscilloscope Average"
    )

    # Oscilloscope maximum
    plt.scatter(
        distance,
        scope_max,
        color="darkgreen",
        marker="+",
        s=95,
        label="Oscilloscope Maximum"
    )

    # Oscilloscope minimum
    plt.scatter(
        distance,
        scope_min,
        color="orange",
        marker="*",
        s=95,
        label="Oscilloscope Minimum"
    )

    # Chart title and labels
    plt.title(
        "Ultrasonic Sensor Characteristic Curve\n"
        "Supply Voltage V_DD = 5.0 V",
        fontsize=14
    )

    plt.xlabel("Distance d (cm)", fontsize=12)
    plt.ylabel("Output Voltage U_out (mV)", fontsize=12)

    # Axis limits
    plt.xlim(0, 205)
    plt.ylim(0, 900)

    # Grid and legend
    plt.grid(
        True,
        linestyle="--",
        alpha=0.4
    )

    plt.legend(loc="upper left")
    plt.tight_layout()

    return plt.gcf()


# --------------------------------------------------
# 5. Save and display graph
# --------------------------------------------------

def main():

    # Create output directory
    output_folder = Path("output")
    output_folder.mkdir(parents=True, exist_ok=True)

    # Generate graph
    figure = plot_sensor_characteristics()

    # Save graph
    output_path = output_folder / "Maxbotix_Characteristic.png"

    figure.savefig(
        output_path,
        dpi=300,
        bbox_inches="tight"
    )

    print(f"Graph successfully saved to: {output_path}")

    # Display graph
    plt.show()


if __name__ == "__main__":
    main()
