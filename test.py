from number_gen import numberGen

gen = numberGen()
nums = [1, 2, 3, 51, 52, 53]
rand = [gen.getSpec(x) for x in nums]
print(rand)