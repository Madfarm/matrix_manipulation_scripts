from scipy import stats 

meta = 36455000000
google = 79000000000
apple = 90753000000
revData = [meta, google, apple]

def trimmedMean(revData):
    #calculate 10% trimmed mean
    return stats.trim_mean(revData, 0.1)

print(f"The 10% trimmed mean from various revenue figures pulled from Apple, Google, and Meta would be {trimmedMean(revData) /  1000000000} billion")

