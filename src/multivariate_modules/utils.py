def computeRawAnomalyScore(activeColumns, prevPredictedColumns):
  """
  Computes the raw anomaly score.
  The raw anomaly score is the fraction of active columns not predicted.
  
  Parameters
  -----------
  activeColumns : np.array 
    Array of active column indices.
  prevPredictedColumns : np.array 
    Array of columns indices predicted in prev step
  
  Returns
  -------
  score : float 
    Anomaly score between 0 and 1.

  """
  
  nActiveColumns = len(activeColumns)
  if nActiveColumns > 0:
    # Test whether each element of a 1-D array is also present in a second
    # array. Sum to get the total # of columns that are active and were
    # predicted.
    score = np.in1d(activeColumns, prevPredictedColumns).sum()
    # Get the percent of active columns that were NOT predicted, that is
    # our anomaly score.
    score = (nActiveColumns - score) / float(nActiveColumns)
  else:
    # There are no active columns.
    score = 0.0
