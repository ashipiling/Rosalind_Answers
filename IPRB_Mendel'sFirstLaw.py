k = 2
m = 2
n = 2
total = float(k+m+n)
if total != 0:
    print (1 - (n/total)*((n-1)/(total-1)) - (n/total)*(m/(total-1)) - (m/total)*((m-1)/(total-1))*0.25)