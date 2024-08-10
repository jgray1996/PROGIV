# The local settings object  
The Settings class is a singleton object because its instance is called once and persisted through the use of other classes. However, this breaks the single-use principle, making it not a SOLID practice.
![refactoring guru](https://refactoring.guru/images/patterns/content/singleton/singleton-comic-1-en.png?id=157509c5693a657ba465c7a9d58a7c25)  
*Source: refactoring.guru*

# Hospital types object 
`hospital_types.py` is a module containing two static values. The logicality of this decision depends on its use. In this case, I would say yes, because this module presumably builds upon existing conventions (code for hospital). Also, this way allows easy maintainability of the kinds of hospitals that are available. Which, in turn, is useful for creating factories. One point of notice is the very java-esque project structure, including the `hospital_types.py` module. Storing these values in a factory module itself or in a separate file is, in my opinion, more a matter of convention and preference than logicality.

# Alternative to singleton objects, a static value module.
If change was necessary, I would suggest the use of a YAML file, separating configuration and logic fully, instead of a hybrid config module. The pros of doing this consist of an easily maintainable list of configurations. These configurations are also easy to find and version-traceable through git. The cons of storing settings in a config file could be, added complexity, added dependencies and some security issues in which people could tend to add a little bit too much information to the file. Examples of this are API keys, usernames, passwords and anything personal and sensitive. 