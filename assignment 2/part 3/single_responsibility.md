# Do the following classes adhere to the Single responsibility principle?
## `CcsClassification.py`
### Intended use of the class
"Class to handle the Ccs classification information from the corresponded CcsClass information file"
### Actual use of the class
* reading files  
* handling dataframes  
* Providing methods for retrieving column names.  

### Conclusion
No, this class does not adhere to the single responsibility principle.

## `CcsHospitalDataExtracter.py`
### Intended use of the class
"Extract hospital data"
### Actual use of the class
* Manage hospital types  
* Fetching data  
* Reading data  
* Plotting data  

### Conclusion
No, this class does not adhere to the single responsibility principle.

## `CcsHospitalInfo.py`
### Intended use of the class
Kinda unclear
### Actual use of the class
* Data storage  
* Data retrieval  
* Data processing  
* reading and writing csv-files  

### Conclusion
No, this class does not adhere to the single responsibility principle.

# Grand conclusion
No, these classes do not adhere to the single responsibility principle.
