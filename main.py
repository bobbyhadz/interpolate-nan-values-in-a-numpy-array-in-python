# Interpolating NaN values in a NumPy Array in Python

import numpy as np


def interpolate_nan(array_like):
    array = array_like.copy()

    nans = np.isnan(array)

    def get_x(a):
        return a.nonzero()[0]

    array[nans] = np.interp(get_x(nans), get_x(~nans), array[~nans])

    return array


# 👇️ [1.  1.  1.5 2.  2.  2.5 3.  3.  3. ]
print(
    interpolate_nan(
        np.array([1, 1, np.NaN, 2, 2, np.NaN, 3, 3, np.NaN])
    )
)