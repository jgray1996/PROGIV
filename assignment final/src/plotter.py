import matplotlib.pyplot as plt
from datetime import datetime


class Plotter:

    def plot_sensor_anomolies(self, sensor, df_object, predictions, recovery, broken):
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
        now = datetime.now().strftime("%H_%M_%S")
        plot.savefig(f"{path}{now}.png")
