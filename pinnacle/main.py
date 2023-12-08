def defineCollocationPoints(steps=100):

  t = np.linspace(t0, tfinal, steps)
  [T, X] = np.meshgrid(t, x, indexing='ij')

  pdes = np.column_stack((T.flatten(), X.flatten())).astype(np.float32)
  pdes = pdes[np.argsort(pdes[:,0])]

  return pdes
