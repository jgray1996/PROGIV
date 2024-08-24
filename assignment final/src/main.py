import time
import yaml
import datamanager
import model
import plotter


class Main:

    def load_config(self, path="config/application.yaml"):
        with open(path, "r") as conf:
            return yaml.safe_load(conf)

    def event_loop(self, training_mode=False):
        config = self.load_config()
        dmr = datamanager.DataManager()
        mod = model.Model()
        plttr = plotter.Plotter()

        new_files = []

        while True:
            new_files = dmr.get_filenames(config["input_directory"])
            print("Waiting for files...")
            if new_files:
                df_i = dmr.read_dataframe(new_files, config["input_directory"])
                df_i = dmr.drow_low_quality(df_i)
                df_i = dmr.format_dataframe(df_i)
                broken, recovery, normal = dmr.create_fractions(df_i)
                df_i = dmr.remove_machine_status(df_i)
                df_i = dmr.fill_nans(df_i)
                outlyer_fraction = mod.calculate_anomoly_cutoff(df_i, normal)
                mat_s = mod.scale_data(df_i)
                if training_mode:
                    print("Training model...")
                    fit = mod.train_model(mat_s, outlyer_fraction)
                    mod.save_model(fit)
                    print("Model trained and saved!")
                    print("Exiting program!")
                    return
                else:
                    print("File found, predicting outlyers...")
                    fit = mod.load_model()
                    predictions = mod.classify(fit, mat_s)
                    dmr.save_predictions(
                        mat_s, df_i, predictions, config["output_directory"]
                    )
                    print("prediction saved!")
                    plot = plttr.plot_sensor_anomolies(
                        "sensor_01", df_i, predictions, recovery, broken
                    )
                    plttr.save_plot(plot, path=config["output_directory"])
                    print("plot saved!")
                    dmr.remove_file(path=config["input_directory"], 
                                    file=new_files[-1])
                    new_files.pop()
                    print("removed training files")

            else:
                self.wait(config["interval"])

    def wait(self, s):
        time.sleep(s)

    def main(self):
        mode = input("If you want to train a model enter the letter 't' else any-key: ")
        mode = mode.lower() == 't'
        self.event_loop(training_mode=mode)


if __name__ == "__main__":
    m = Main()
    m.main()
