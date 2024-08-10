# Examples of Liskov's Substitution Principle
The Liskov Substitution Principle states: *"objects of a superclass shall be replaceable with objects of its subclasses without breaking the application."*  
If we take a look at the project Karel we can see some examples of enheritance taking place. These are the classes:  
* `HsmrParser` (Base class)
* `HsmrParserFactory`  
* `HsmrPdfParser` : `HsmrParser`  
* `HsmrTextParser` : `HsmrParser`  

In this case the `read_file` method available in all the classes have distinct implemenentations. For instance if this method is called from the baseclass an exeption is thrown. Thus, breaking the LSP while still providing the client all of the same API. Karel fixes this issue by implementing a factory class which handles calling the right instance of HsmrReport, either being `pdf` or `text`. This prevents the user of implementing a subclass, avoiding iffy use of baseclasses.