import numpy as np
from scipy import special

b = 1 / 9.5
t_m = 87.25


def af(r, t_0):
    eta = np.exp(b * (t_0 - t_m))
    print(1 - r / b)
    # return np.exp(eta) / b * special.expn(1 + r / b, eta)
    # return eta ** (r / b) * np.exp(eta) / b * special.gammaincc(-r / b, eta)
    print(special.gamma(1 - r / b) * special.gammaincc(1 - r / b, eta))
    return (
        1
        - np.exp(eta)
        * eta ** (r / b)
        * special.gamma(1 - r / b)
        * special.gammaincc(1 - r / b, eta)
    ) / r


print(af(0.25 / 100, t_0=65))
