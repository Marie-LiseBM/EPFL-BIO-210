import numpy as np
import timeit

#N = int(1e6)
numexperiments=13
Ns=np.logspace(2,8,numexperiments)
results=np.empty((numexperiments,4))

for j in range(numexperiments):
    N=int(Ns[j])
    results[j,0]=N

    print("Running test with N =", str(N))
    start = timeit.default_timer()
    data = range(N)
    output = []
    for d in data:
        output.append(17 * d)


    stop = timeit.default_timer()
    results[j,1]=stop-start
    print("Method loop: ", round(stop - start,6),' seconds')

    start = timeit.default_timer()
    output = [17 * d for d in range(N)]
    stop = timeit.default_timer()
    results[j,2]=stop-start
    print("Method list comprehension: ", round(stop - start,6),' seconds')

    start = timeit.default_timer()
    output = 17 * np.arange(N)
    stop = timeit.default_timer()
    results[j,3]=stop-start
    print("Method numpy: ", round(stop - start,6),' seconds')

import matplotlib.pyplot as plt

for j in [1,2,3]:
    plt.loglog(results[:,0],results[:,j],label=['loop','list compr.','numpy'][j-1],lw=3,alpha=.8)

plt.ylabel("Run time in seconds (log)")
plt.xlabel('Samples for computation (log)')
plt.legend()
plt.savefig("Lecture2_RuntimeComparison.png")
plt.show()
