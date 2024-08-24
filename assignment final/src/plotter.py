import matplotlib.pyplot as plt
from datetime import datetime


class Plotter:
    """
    A class to handle plotting and saving sensor anomaly visualizations.
    """

    def plot_sensor_anomolies(self, sensor, df_object, predictions, recovery, broken):
        """
        Plot sensor data along with annotations for predicted anomalies, 
        recovery periods, and broken statuses.

        Parameters:
        sensor (str): The name of the sensor column to plot.
        df_object (pandas.DataFrame): The DataFrame containing the sensor data and predictions.
        predictions (numpy.ndarray): The array of predictions indicating anomalies.
        recovery (pandas.DataFrame): The DataFrame containing rows where the machine is recovering.
        broken (pandas.DataFrame): The DataFrame containing rows where the machine is broken.

        Returns:
        matplotlib.pyplot: The generated plot object.
        """
        df_object["predictions"] = predictions
        anomoly_rows = df_object[df_object.predictions == -1]
        plot = plt.figure(figsize=(25, 3))
        plot = plt.plot(df_object[sensor], color="grey")
        plot = plt.plot(
            recovery[sensor],
            linestyle="none",
            marker="o",
            color="yellow",
            markersize=5,
            label="recovering",
            alpha=0.5,
        )
        plot = plt.plot(
            broken[sensor],
            linestyle="none",
            marker="X",
            color="red",
            markersize=20,
            label="broken",
        )
        plot = plt.plot(
            anomoly_rows[sensor],
            linestyle="none",
            marker="X",
            color="blue",
            markersize=4,
            label="anomoly predicted",
            alpha=0.1,
        )
        plot = plt.title(sensor)
        plot = plt.legend()
        return plt

    def save_plot(self, plot, path):
        """
        Save the generated plot to a file with a timestamp in the filename.

        Parameters:
        plot (matplotlib.pyplot): The plot object to save.
        path (str): The directory path where the plot image will be saved.

        Returns:
        None
        """
        now = datetime.now().strftime("%H_%M_%S")
        plot.savefig(f"{path}{now}.png")
