# pyarkovchain
Pyarkovchain is now a module for python 3. It has 2 main classes: `ExampleData` and `MChain`. `ExampleData` helps you acess pre-fetched data, and `MChain` is the real markov chain.

```
import pyarkovchain as pc
data_class = pc.example_data.ExampleData()
markov_chain = pc.markov_chain.MChain()
```

The `MChain` class has an optional argument called `DEPTH`. This controls how much the markov chain "looks back". Higher values for the `DEPTH` argument means less broken english but more overfitting. The `MChain` class has two methods: `init` and `predict`. The `init` method generates the frequency tables for the `predict` method to use. The `init` method takes data as the argument.
