import time
import yaml
import datamanager

class Main:

    def load_config(self, path="config/application.yaml"):
        with open(path, "r") as conf:
            return yaml.safe_load(conf)

    def event_loop(self):
        config = self.load_config()
        dmr = datamanager.DataManager()

        old_files = []
        new_files = []

        while True:
            new_files = dmr.get_filenames(config["input_directory"])

            if dmr.new_file(old_files, new_files):
                # Read each file
                # Transform
                # Predict
                # Write predictions
                # Create plots
                # Save plots
                # Remove old files
                old_files = new_files

            else:
                self.wait(config["interval"])

    def wait(self, s):
        time.sleep(s)

    def main(self):
        self.event_loop()


m = Main()
m.main()
