import scipy.stats as s
mean = 120
deviation = 15
z_score= (140 - mean)/deviation
probability = 1-s.norm.cdf(z_score)
percentage = probability*100
print(f"The percentage of birds that weights more than 140gm is, {percentage:.2f}%")
