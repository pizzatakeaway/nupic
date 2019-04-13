import os
import numpy as np
import pandas as pd
import json
import datetime
from nupic.frameworks.opf.common_models.cluster_params import getScalarMetricWithTimeOfDayAnomalyParams
from nupic.encoders.scalar import ScalarEncoder
from nupic.algorithms.spatial_pooler import SpatialPooler
from nupic.algorithms.backtracking_tm import BacktrackingTM
from nupic.algorithms.anomaly_likelihood import AnomalyLikelihood
#from nupic.multivariate_modules.utils import computeRawAnomalyScore

PATH_repo = os.getcwd()
PATH_data_folder = PATH_repo + '/ab_experiments/data/NAB/'
PATH_data_file = 'realKnownCause/machine_temperature_system_failure.csv'
PATH_data = os.path.join(PATH_data_folder, PATH_data_file)
PATH_labels = os.path.join(PATH_data_folder, 'labels/combined_windows.json')

df = pd.read_csv(PATH_data) #parse_dates=True
with open(PATH_labels) as f:
    labels = json.loads(f.read())

# check columns format
df['value'] = pd.to_numeric(df['value'])
df['timestamp'] = pd.to_datetime(df['timestamp'], format="%Y-%m-%d %H:%M:%S")



df['labels'] = np.zeros_like(df.value)
# set values within the range = 1
for i in range(len(labels[PATH_data_file])):
    df.loc[(df['timestamp'] >= labels[PATH_data_file][i][0]) & 
           (df['timestamp'] <= labels[PATH_data_file][i][1]), 'labels'] = 1

# df to dict
data = df.to_dict(orient='records')
