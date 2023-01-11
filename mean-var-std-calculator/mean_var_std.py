import numpy as np


def calculate(list):
  calculations = {}
  calcList = {
    'mean': 'mean',
    'variance': 'var',
    'standard deviation': 'std',
    'max': 'max',
    'min': 'min',
    'sum': 'sum'
  }
  try:
    mat = np.reshape(list, (3, 3))

    for calc, method in calcList.items():
      calculations[calc] = [
        getattr(mat, method)(axis=0).tolist(),
        getattr(mat, method)(axis=1).tolist(),
        getattr(mat, method)()
      ]

    return calculations
  except (ValueError):
    raise ValueError('List must contain nine numbers.')
