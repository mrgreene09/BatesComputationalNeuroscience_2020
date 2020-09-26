def meanMat(x):
    import numpy as np
    y = np.sum(x) / np.size(x);
    return y

def corr2(a,b):
    import numpy as np
    a = a - meanMat(a)
    b = b - meanMat(b)

    r = np.sum((a*b)) / np.sqrt(np.sum((a*a)) * np.sum((b*b)))
    return r