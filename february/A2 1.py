from scipy.stats import norm
mean = 175
deviation = 8
max_height = 185
z_score= (max_height - mean)/deviation
taller = 1-norm.cdf(z_score)
percentage = taller*100
print("males taller than",max_height,percentage)
