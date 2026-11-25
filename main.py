import pandas as pd

df = pd.read_csv("insurance.csv")

ages = df["age"].tolist()

n = len(ages)

mean = sum(ages) / n

deviations = []

for age in ages:
    deviation = age - mean
    deviations.append(deviation)

squared_deviations = []

for deviation in deviations:
    squared = deviation**2
    squared_deviations.append(squared)

total = sum(squared_deviations)

variance = total / n

print("Mean:", mean)
# print("Variance:", variance)
print("Pandas Variance:", df["age"].var(ddof=0))
