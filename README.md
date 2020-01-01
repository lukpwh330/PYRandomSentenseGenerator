# pyarkovchain
![pyarkovchain logo](/pyarkovchain.png)

Pyarkovchain is module for creating generic markov chains in python 3. It has 2 main classes: `ExampleData` and `MChain`. `ExampleData` helps you acess pre-fetched data, and `MChain` is the real markov chain. [Here](https://en.wikipedia.org/wiki/Markov_chain) is how a markov chain works. 

``` python
import pyarkovchain as pc
data_class = pc.example_data.ExampleData(*args)
markov_chain = pc.markov_chain.MChain(*args)
```

## Why pyarkovchain? 
Here are some reasons:

* Ease of use.
* Only uses built in python modules.
* Example data to play around with (e.g. Harry potter, The Hobbit)
* Simplicity

## The `Mchain` Class
`MChain` is the markov chain object used to generate the markov chain object. The `MChain` class has an optional argument called `DEPTH`. This controls how much the markov chain "looks back". Higher values for the `DEPTH` argument means less broken english but more overfitting. The `MChain` class has two methods: `init` and `predict`. 

``` python
import pyarkovchain as pc
depth_of_markov_chain = 3
markov_chain = pc.markov_chain.MChain(DEPTH=depth_of_markov_chain)
```

### The `init` Method
The `init` method generates the frequency tables for the `predict` method to use. The `init` method takes data as its only argument. The data given to this function should have no capital letters for best results and should be stripped of newlines. The data can just be in the form of a normal python string.

``` python
import pyarkovchain as pc
some_data = """To be, or not to be: that is the question: 
Whether ‘tis nobler in the mind to suffer
The slings and arrows of outrageous fortune,
Or to take arms against a sea of troubles,
And by opposing end them?
To die: to sleep;""" # Make raw text

processed_data = some_data.replace("\n", " ").lower() # Get rid of newlines and make it all lowercase
markov_chain = pc.markov_chain.MChain() # Make markov chain object
markov_chain.init(processed_data)
```

### The `predict` Method
After the `init` method is called, the `predict` method can be used. The `predict` method takes 2 arguments: the start of the range and the end of the range of how many words the output will be. For example, the arguments 100 and 200 tell the method that the amount of words will be randomly selected and in between the numbers 100 and 200.

``` python
import pyarkovchain as pc
markov_chain = pc.markov_chain.MChain()
markov_chain.init(some_data)
markov_chain.predict(100, 200)
```

## The `ExampleData` Class
The `ExampleData` class provides example data for the `MChain` class. This class takes the name of the example passage/book as its first argument. When pyarkovchain is installed, it comes with sample "training data". The name of this data must be provided. You may put your own data into the `pyarkovchain/example_data` folder. The data should be saved into a `.txt`. If you have a file `hello_world.txt`, just provide `"hello_world"` as the first argument. Look [here](https://github.com/MonliH/pyarkovchain#list-of-example-passagesdata) for all the avaiable passages/text examples built-in.

``` python
import pyarkovchain as pc
data_class = pc.example_data.ExampleData("harry_potter_1")  # get first book of Harry Potter
```

### The `get_raw_text` Method
The `get_raw_text` method returns the text. For example, you would call this method as an argument to the `init` method. This method takes not arguments. Note this method returns already preprocessed data (e.g. gets rid of newline and cases).

``` python
import pyarkovchain as pc
data_class = pc.example_data.ExampleData("harry_potter_1")
print(data_class.get_raw_text())

# Returns
# ...
# "they don't know we're not allowed to use magic at home. 
# i'm going to have a lot of fun with dudley this summer...."
# ...
```

## TODO List
- [x] Create variable lookahead rates (the `DEPTH` argument)

- [x] Have example passages (e.g. Harrry potter)

- [x] Allow other files in the `pyarkovchain/example_data` folder.

- [ ] Create savable models

- [ ] Be able to combine models

## List of example passages/data
* The Bible - `bible`
* Harry Potter Book 1 - `harry_potter_1`
* The Hobbit - `hobbit`
* Python code - `python_code`
