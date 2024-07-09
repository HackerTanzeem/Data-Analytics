from scipy.stats import norm
mean = 100
deviation = 15
z_score_85 = (85-mean)/deviation
z_score_115 = (115-mean)/deviation
portion_between = norm.cdf(z_score_115) - norm.cdf(z_score_85)
print(portion_between)