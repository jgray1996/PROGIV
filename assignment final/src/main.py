import time
import yaml
import datamanager
import model
import plotter

class Main:

    def load_config(self, path="config/application.yaml"):
        with open(path, "r") as conf:
            return yaml.safe_load(conf)

    def event_loop(self):
        config = self.load_config()
        dmr = datamanager.DataManager()
        mod = model.Model()
        plttr = plotter.Plotter()

        old_files = []
        new_files = []

        while True:
            new_files = dmr.get_filenames(config["input_directory"])

            if dmr.new_file(old_files, new_files):
                # Read file
                df_i = dmr.read_dataframe(new_files)
                # Prepare data
                df_i = dmr.drow_low_quality(df_i)
                df_i = dmr.format_dataframe(df_i)
                # Extract fractions
                broken, recovery, normal = dmr.create_fractions(df_i)
                # Filter data
                df_i = dmr.remove_machine_status(df_i)
                df_i = dmr.fill_nans(df_i)
                # Scale data
                outlyer_fraction = mod.calculate_anomoly_cutoff(df_i, normal)
                mat_s = mod.scale_data(df_i)
                # Fit model
                fit = mod.train_model(mat_s, outlyer_fraction)
                # save model
                mod.save_model(fit)
                fit = mod.load_model()
                # Predict
                predictions = mod.classify(fit, mat_s)
                print("done!")
                # Write predictions
                dmr.save_predictions(mat_s, df_i, predictions, config["output_directory"])
                # Create plots
                plot = plttr.plot_sensor_anomolies("sensor_01", df_i, predictions, recovery, broken)
                # Save plots
                plttr.save_plot(plot, path=config["output_directory"])
                # Remove old files
                old_files = new_files

            else:
                self.wait(config["interval"])

    def wait(self, s):
        time.sleep(s)

    def main(self):
        self.event_loop()

if __name__ == "__main__":
    print("initialising...")
    m = Main()
    print("waiting for file...")
    m.main()
