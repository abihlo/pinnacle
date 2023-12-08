import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

def testModule():
	print('Test!')

def defineDomain():
	print(np.array([1,1,3]))


def defineCollocationPoints(steps=100):

  t = np.linspace(t0, tfinal, steps)
  [T, X] = np.meshgrid(t, x, indexing='ij')

  pdes = np.column_stack((T.flatten(), X.flatten())).astype(np.float32)
  pdes = pdes[np.argsort(pdes[:,0])]

  return pdes
