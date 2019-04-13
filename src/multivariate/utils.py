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

def idx_active_cols(inputArr):
    """
    This function takes an 1d or nd-array and returns a 1d-array with the index for ACTIVE bits/columns: 
    
    Parameters
    ----------
    inputArr:   np.array (1d or nD)
            
    Output
    ------
    tmActiveColsIdx: 1d np.arraz
        Array with index of active cols.
        
    """
    #tmObject.reshape(tmObject.numberOfCols, tm.cellsPerColumn)
    activeColsVec = []  # initialize vector

    for i in range(inputArr.shape[0]):
        # assign 1 if any 1 (active cell) in the column,
        # 0 otherwise
        if np.any(inputArr[i]>0):
        # if np.any(tm.compute(spSDR[track[3]['sp_active']], enableLearn=True, enableInference=True).reshape(256, 3)[i]>0):
            activeColsVec.append(1)
        else:
            activeColsVec.append(0)
    # return index of active Columns        
    tmActiveColsIdx = np.flatnonzero(np.array(activeColsVec))
    return tmActiveColsIdx
