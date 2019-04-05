import pyarkovchain as pc

data = pc.example_data.ExampleData("harry_potter_1").get_raw_text()
chain = pc.markov_chain.MChain(DEPTH=3)
chain.init(data)
prediction = chain.predict(900, 1000)
print(prediction)
