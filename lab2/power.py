from scipy import stats

def power(sample1, sample2, reps, size, alpha):
    acc = 0
    for i in range(reps):
        ## Calculate the Standard Deviation
        #Calculate the variance to get the standard deviation

        #For unbiased max likelihood estimate we have to divide the var by N-1, and therefore the parameter ddof = 1
        var_a = sample1.var(ddof=1)
        var_b = sample2.var(ddof=1)

        #std deviation
        s = np.sqrt((var_a + var_b)/2)

        ## Calculate the t-statistics
        t = (a.mean() - b.mean())/(s*np.sqrt(2/N))

        ## Compare with the critical t-value
        #Degrees of freedom
        df = 2*N - 2

        #p-value after comparison with the t
        p = 1 - stats.t.cdf(t,df=df)

    if (p < 1-alpha):
        acc+=1

    return acc
