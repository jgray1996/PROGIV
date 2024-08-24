# How to run

## adjust config file.
The config file is located in the directory `config/application.yaml`. Adjust parameters to your liking.

## install required packages  
This program has the following dependencies  
*  sklearn
*  pandas
*  numpy
*  matplotlib

## Running the program.
### 1 - Training the model
On the first run you need to train a model. Run the program as such:  
`python src/main.py`  
Enter the letter `t` to train the model and be sure you added the training data in the specified `input directory`  
A moddel will be fit and the program will terminate when done.  

### 2 - Classify with trained model
Run the progam as such:  
`python src/main.py` 
press any key but the letter "t".
Make sure your files to be classified are in the specified input directory. 

