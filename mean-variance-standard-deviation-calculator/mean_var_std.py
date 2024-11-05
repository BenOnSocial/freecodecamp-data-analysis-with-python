import numpy as np

def calculate(list):
  input = np.array(list)

  if input.size != 9:
    raise ValueError('List must contain nine numbers.');

  reshaped = input.reshape((3, 3))

  calculations = {
      'mean': [reshaped.mean(axis=0).tolist(), reshaped.mean(axis=1).tolist(), reshaped.mean()],
      'variance': [reshaped.var(axis=0).tolist(), reshaped.var(axis=1).tolist(), reshaped.var()],
      'standard deviation': [reshaped.std(axis=0).tolist(), reshaped.std(axis=1).tolist(), reshaped.std()],
      'min': [reshaped.min(axis=0).tolist(), reshaped.min(axis=1).tolist(), reshaped.min()],
      'max': [reshaped.max(axis=0).tolist(), reshaped.max(axis=1).tolist(), reshaped.max()],
      'sum': [reshaped.sum(axis=0).tolist(), reshaped.sum(axis=1).tolist(), reshaped.sum()]
  }

  return calculations
