from scipy.stats import norm
percentile = 90
z_score = norm.ppf(percentile/100)
print(z_score)