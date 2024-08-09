# The factory
## What is a factory?
A factory is a design pattern that deals with the creation of objects. It was invented to decrease the amount of coupling between classes. Coupling is what can happen if a complex object is being interfaced with directly. This can cause many threads of interaction to form between the controlling and the controlled object. Which in turn leads to difficultly maintainable code.  

![](https://m.media-amazon.com/images/I/51-8gPee03L.jpg)  
*A nice representation of coupling, in my opinion*
  
## How does a factory solve this issue?
A factory aims to solve coupling by abstracting away the instantiation of objects in a new and separate factory class. In which the processing computations named **products** are handled.

Imagine you could program cooking. One could create a class named `Chef` and `Chef` is able to do many things. He could, for example `cook`, `clean`, `use_oven`, `yell_at_cook` and `smoke_cigarette` as any chef typically does. The Chef is proficient at interacting with many objects in the kitchen. Think of `Knife`, `Oven`, `Whisk`, `Cigarettes` but also `Courgette`, `Truffle`, `Egg`, `Caviar`, `Milk`, `Flour`. 

### One day
On a good day, Monsieur Toddler walks into the restaurant and orders pancakes. Chef is dumbfounded, his restaurant is a place of sophistication and refine. Alas, the customer is king, and chef gets to work even though his kitchen isn't exactly made to cook pancakes. However, his kitchen is made to cook, and the chef is flexible, he just needs to give orders to the cooks! Chef grabs the great book *Cuisine a la Usine*. A fine book that contains explicit instructions of how to use the kitchen in combination with the ingredients to produce pancakes. He puts his cooks to work, and in a whirl, the finest pancakes are served, which are devoured by Monsieur Toddler. Chef hangs his apron on a hook and leaves home, vowing never to cook pancakes in his kitchen ever again.

### The moral of the story
In this story, Chef isn't bound by the things that were served on the menu. He just needed to update a new product in the cooking factory. This was done easily, and was reverted just as easily. This is what factories do. 

## Does implementing a factory follow the *Interface Segregation Principle? (ISP)*
Implementing a factory method **can** follow the ISP depending on how the factory is written. 

* Yes, if the factory method is implemented in such a way that the interface is specific.

* No, if the factory method interface is large and includes methods that a client does not need or use. This would violate the ISP because clients would be forced to implement unnecessary methods. This would defeat the use of a factory all again, just adding unnecessary complexity.