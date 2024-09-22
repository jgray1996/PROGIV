import time
import yaml
import datamanager
import model
import plotter
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    filename="program.log"
)

class Main:
    """
    Main class that handles the primary operations of the program, including configuration loading,
    event loop execution, model training, anomaly detection, and plotting results.
    """

    def load_config(self, path="config/application.yaml"):
        """
        Load the application configuration from a YAML file.

        Parameters:
        path (str): The file path to the YAML configuration file.

        Returns:
        dict: The loaded configuration as a dictionary.
        """
        with open(path, "r") as conf:
            return yaml.safe_load(conf)

    def event_loop(self, training_mode=False):
        """
        The main event loop that monitors a directory for new files, processes data, 
        trains a model (if in training mode), or classifies data using a pre-trained model.

        Parameters:
        training_mode (bool): If True, the loop will train a new model instead of classifying data.
        """
        config = self.load_config()
        dmr = datamanager.DataManager()
        mod = model.Model()
        plttr = plotter.Plotter()

        new_files = []

        while True:
            # You could have broken down this method into several sub-methods; that would
            # have improved readability.
            new_files = dmr.get_filenames(config["input_directory"])
            print("Waiting for files...")
            if new_files:
                logging.info("Found new file")
                logging.info(f"Loading new file: {new_files[-1]}")
                df_i = dmr.read_dataframe(new_files, config["input_directory"])
                logging.info("Dropping low quality reads")
                df_i = dmr.drow_low_quality(df_i)
                logging.info("Formatting data")
                df_i = dmr.format_dataframe(df_i)
                broken, recovery, normal = dmr.create_fractions(df_i)
                df_i = dmr.remove_machine_status(df_i)
                df_i = dmr.fill_nans(df_i)
                outlyer_fraction = mod.calculate_anomoly_cutoff(df_i, normal)
                mat_s = mod.scale_data(df_i)
                if training_mode:
                    logging.info("Program run in TRAINING MODE")
                    print("Training model...")
                    fit = mod.train_model(mat_s, outlyer_fraction)
                    mod.save_model(fit)
                    logging.info("Model trained: saved in src/")
                    return
                else:
                    logging.info("File found, loading model")
                    fit = mod.load_model()
                    logging.info("Classifying outlyers")
                    predictions = mod.classify(fit, mat_s)
                    logging.info("Predictions saved")
                    dmr.save_predictions(
                        mat_s, df_i, predictions, config["output_directory"]
                    )
                    print("prediction saved!")
                    for sensor in config["sensors"]:
                        plot = plttr.plot_sensor_anomolies(
                            sensor, df_i, predictions, recovery, broken
                        )
                        plttr.save_plot(plot, path=config["output_directory"])
                        self.wait(1)
                        logging.info("plot saved!")
                    dmr.remove_file(path=config["input_directory"], 
                                    file=new_files[-1])
                    new_files.pop()
                    logging.info("removed training files")

            else:
                self.wait(config["interval"])

    def wait(self, s):
        """
        Pause the execution for a specified number of seconds.

        Parameters:
        s (int): Number of seconds to sleep.
        """
        time.sleep(s)

    def main(self):
        """
        The main entry point for the program. Determines the mode (training or classification)
        and starts the event loop accordingly.
        """
        mode = input("If you want to train a model enter the letter 't' else any-key: ") # where's the any key on my keyboard?
        mode = mode.lower() == 't'
        self.event_loop(training_mode=mode)


if __name__ == "__main__":
    m = Main()
    m.main()
    # or just Main().main()
