from noun import noun

sigma = noun("sigma", ["s", "i", "g", "m", "a"], "sigma", "neuter")

sigma.setGender("masculine")
print(sigma.search())

sigma.add()
print(sigma.search())