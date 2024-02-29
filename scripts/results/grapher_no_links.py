
# We will use the following Python libraries:
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

# Path to where the results are hosted online
# This loads the data into a Pandas dataframe
# You have seperate files for all trials and all
# robots, so these have to be loaded in individually

min_time = 0
max_time = 1200

#TTH 2 6
#trial 1, robot 1 2 3
TTH_2_6_T1_R1= pd.read_csv('', sep=',', header=None)
TTH_2_6_T1_R2 =pd.read_csv('', sep=',', header=None)
TTH_2_6_T1_R3 =pd.read_csv('', sep=',', header=None)

#trial 2, robot 1 2 3
TTH_2_6_T2_R1= pd.read_csv('', sep=',', header=None)
TTH_2_6_T2_R2 =pd.read_csv('', sep=',', header=None)
TTH_2_6_T2_R3= pd.read_csv('', sep=',', header=None)

#trial 3, robot 1 2 3
TTH_2_6_T3_R1= pd.read_csv('', sep=',', header=None)
TTH_2_6_T3_R2 =pd.read_csv('', sep=',', header=None)
TTH_2_6_T3_R3 =pd.read_csv('', sep=',', header=None)

#trial 4, robot 1 2 3
TTH_2_6_T4_R1= pd.read_csv('', sep=',', header=None)
TTH_2_6_T4_R2 =pd.read_csv('', sep=',', header=None)
TTH_2_6_T4_R3 =pd.read_csv('', sep=',', header=None)

#trial 5, robot 1 2 3
TTH_2_6_T5_R1= pd.read_csv('', sep=',', header=None)
TTH_2_6_T5_R2 =pd.read_csv('', sep=',', header=None)
TTH_2_6_T5_R3 =pd.read_csv('', sep=',', header=None)

#trial 6, robot 1 2 3
TTH_2_6_T6_R1= pd.read_csv('', sep=',', header=None)
TTH_2_6_T6_R2 =pd.read_csv('', sep=',', header=None)
TTH_2_6_T6_R3 =pd.read_csv('', sep=',', header=None)

#trial 7, robot 1 2 3
TTH_2_6_T7_R1= pd.read_csv('', sep=',', header=None)
TTH_2_6_T7_R2 =pd.read_csv('', sep=',', header=None)
TTH_2_6_T7_R3= pd.read_csv('', sep=',', header=None)

#trial 8, robot 1 2 3
TTH_2_6_T8_R1= pd.read_csv('', sep=',', header=None)
TTH_2_6_T8_R2 =pd.read_csv('', sep=',', header=None)
TTH_2_6_T8_R3 =pd.read_csv('', sep=',', header=None)

#trial 9, robot 1 2 3
TTH_2_6_T9_R1= pd.read_csv('', sep=',', header=None)
TTH_2_6_T9_R2 =pd.read_csv('', sep=',', header=None)
TTH_2_6_T9_R3 =pd.read_csv('', sep=',', header=None)

#trial 10, robot 1 2 3
TTH_2_6_T10_R1= pd.read_csv('', sep=',', header=None)
TTH_2_6_T10_R2 =pd.read_csv('', sep=',', header=None)
TTH_2_6_T10_R3 =pd.read_csv('', sep=',', header=None)

#TTH 100 200
#trial 1, robot 1 2 3
TTH_100_200_T1_R1 =pd.read_csv('', sep=',', header=None)
TTH_100_200_T1_R2 =pd.read_csv('', sep=',', header=None)
TTH_100_200_T1_R3 =pd.read_csv('', sep=',', header=None)

#trial 2, robot 1 2 3
TTH_100_200_T2_R1 =pd.read_csv('', sep=',', header=None)
TTH_100_200_T2_R2 =pd.read_csv('', sep=',', header=None)
TTH_100_200_T2_R3 =pd.read_csv('', sep=',', header=None)

#trial 3, robot 1 2 3
TTH_100_200_T3_R1 =pd.read_csv('', sep=',', header=None)
TTH_100_200_T3_R2 =pd.read_csv('', sep=',', header=None)
TTH_100_200_T3_R3 =pd.read_csv('', sep=',', header=None)

#trial 4, robot 1 2 3
TTH_100_200_T4_R1 =pd.read_csv('', sep=',', header=None)
TTH_100_200_T4_R2 =pd.read_csv('', sep=',', header=None)
TTH_100_200_T4_R3 =pd.read_csv('', sep=',', header=None)

#trial 5, robot 1 2 3
TTH_100_200_T5_R1 =pd.read_csv('', sep=',', header=None)
TTH_100_200_T5_R2 =pd.read_csv('', sep=',', header=None)
TTH_100_200_T5_R3 =pd.read_csv('', sep=',', header=None)

#trial 6, robot 1 2 3
TTH_100_200_T6_R1 =pd.read_csv('', sep=',', header=None)
TTH_100_200_T6_R2 =pd.read_csv('', sep=',', header=None)
TTH_100_200_T6_R3 =pd.read_csv('', sep=',', header=None)

#trial 7, robot 1 2 3
TTH_100_200_T7_R1 =pd.read_csv('', sep=',', header=None)
TTH_100_200_T7_R2 =pd.read_csv('', sep=',', header=None)
TTH_100_200_T7_R3 =pd.read_csv('', sep=',', header=None)

#trial 8, robot 1 2 3
TTH_100_200_T8_R1 =pd.read_csv('', sep=',', header=None)
TTH_100_200_T8_R2 =pd.read_csv('', sep=',', header=None)
TTH_100_200_T8_R3 =pd.read_csv('', sep=',', header=None)

#trial 9, robot 1 2 3
TTH_100_200_T9_R1 =pd.read_csv('', sep=',', header=None)
TTH_100_200_T9_R2 =pd.read_csv('', sep=',', header=None)
TTH_100_200_T9_R3 =pd.read_csv('', sep=',', header=None)

#trial 10, robot 1 2 3
TTH_100_200_T10_R1 =pd.read_csv('', sep=',', header=None)
TTH_100_200_T10_R2 =pd.read_csv('', sep=',', header=None)
TTH_100_200_T10_R3 =pd.read_csv('', sep=',', header=None)

#NP
#trial 1, robot 1 2 3
NP_T1_R1 =pd.read_csv('', sep=',', header=None)
NP_T1_R2 =pd.read_csv('', sep=',', header=None)
NP_T1_R3 =pd.read_csv('', sep=',', header=None)

#trial 2, robot 1 2 3
NP_T2_R1 =pd.read_csv('', sep=',', header=None)
NP_T2_R2 =pd.read_csv('', sep=',', header=None)
NP_T2_R3 =pd.read_csv('', sep=',', header=None)

#trial 3, robot 1 2 3
NP_T3_R1 =pd.read_csv('', sep=',', header=None)
NP_T3_R2 =pd.read_csv('', sep=',', header=None)
NP_T3_R3 =pd.read_csv('', sep=',', header=None)

#trial 4, robot 1 2 3
NP_T4_R1 =pd.read_csv('', sep=',', header=None)
NP_T4_R2 =pd.read_csv('', sep=',', header=None)
NP_T4_R3 =pd.read_csv('', sep=',', header=None)

#trial 5, robot 1 2 3
NP_T5_R1 =pd.read_csv('', sep=',', header=None)
NP_T5_R2 =pd.read_csv('', sep=',', header=None)
NP_T5_R3 =pd.read_csv('', sep=',', header=None)

#trial 6, robot 1 2 3
NP_T6_R1 =pd.read_csv('', sep=',', header=None)
NP_T6_R2 =pd.read_csv('', sep=',', header=None)
NP_T6_R3 =pd.read_csv('', sep=',', header=None)

#trial 7, robot 1 2 3
NP_T7_R1 =pd.read_csv('', sep=',', header=None)
NP_T7_R2 =pd.read_csv('', sep=',', header=None)
NP_T7_R3 =pd.read_csv('', sep=',', header=None)

#trial 8, robot 1 2 3
NP_T8_R1 =pd.read_csv('', sep=',', header=None)
NP_T8_R2 =pd.read_csv('', sep=',', header=None)
NP_T8_R3 =pd.read_csv('', sep=',', header=None)

#trial 9, robot 1 2 3
NP_T9_R1 =pd.read_csv('', sep=',', header=None)
NP_T9_R2 =pd.read_csv('', sep=',', header=None)
NP_T9_R3 =pd.read_csv('', sep=',', header=None)

#trial 10, robot 1 2 3
NP_T10_R1 =pd.read_csv('', sep=',', header=None)
NP_T10_R2 =pd.read_csv('', sep=',', header=None)
NP_T10_R3 =pd.read_csv('', sep=',', header=None)

# TTH 6 10 
# trial 1, robot 1 2 3 
TTH_6_10_T1_R1 =pd.read_csv('', sep=',', header=None) 
TTH_6_10_T1_R2 =pd.read_csv('', sep=',', header=None) 
TTH_6_10_T1_R3 =pd.read_csv('', sep=',', header=None)

# trial 2, robot 1 2 3
TTH_6_10_T2_R1 =pd.read_csv('', sep=',', header=None)
TTH_6_10_T2_R2 =pd.read_csv('', sep=',', header=None)
TTH_6_10_T2_R3 =pd.read_csv('', sep=',', header=None)

# trial 3, robot 1 2 3
TTH_6_10_T3_R1 =pd.read_csv('', sep=',', header=None)
TTH_6_10_T3_R2 =pd.read_csv('', sep=',', header=None)
TTH_6_10_T3_R3 =pd.read_csv('', sep=',', header=None)

# trial 4, robot 1 2 3
TTH_6_10_T4_R1 =pd.read_csv('', sep=',', header=None)
TTH_6_10_T4_R2 =pd.read_csv('', sep=',', header=None)
TTH_6_10_T4_R3 =pd.read_csv('', sep=',', header=None)

# trial 5, robot 1 2 3
TTH_6_10_T5_R1 =pd.read_csv('', sep=',', header=None)
TTH_6_10_T5_R2 =pd.read_csv('', sep=',', header=None)
TTH_6_10_T5_R3 =pd.read_csv('', sep=',', header=None)

# trial 6, robot 1 2 3
TTH_6_10_T6_R1 =pd.read_csv('', sep=',', header=None)
TTH_6_10_T6_R2 =pd.read_csv('', sep=',', header=None)
TTH_6_10_T6_R3 =pd.read_csv('', sep=',', header=None)

# trial 7, robot 1 2 3
TTH_6_10_T7_R1 =pd.read_csv('', sep=',', header=None)
TTH_6_10_T7_R2 =pd.read_csv('', sep=',', header=None)
TTH_6_10_T7_R3 =pd.read_csv('', sep=',', header=None)

# trial 8, robot 1 2 3
TTH_6_10_T8_R1 =pd.read_csv('', sep=',', header=None)
TTH_6_10_T8_R2 =pd.read_csv('', sep=',', header=None)
TTH_6_10_T8_R3 =pd.read_csv('', sep=',', header=None)

# trial 9, robot 1 2 3
TTH_6_10_T9_R1 =pd.read_csv('', sep=',', header=None)
TTH_6_10_T9_R2 =pd.read_csv('', sep=',', header=None)
TTH_6_10_T9_R3 =pd.read_csv('', sep=',', header=None)

# trial 10, robot 1 2 3
TTH_6_10_T10_R1 =pd.read_csv('', sep=',', header=None)
TTH_6_10_T10_R2 =pd.read_csv('', sep=',', header=None)
TTH_6_10_T10_R3 =pd.read_csv('', sep=',', header=None)

#TTH 100 200
#trial 1, robot 1 2 3
TTH_100_200_T1_R1 =pd.read_csv('', sep=',', header=None)
TTH_100_200_T1_R2 =pd.read_csv('', sep=',', header=None)
TTH_100_200_T1_R3 =pd.read_csv('', sep=',', header=None)

#trial 2, robot 1 2 3
TTH_100_200_T2_R1 =pd.read_csv('', sep=',', header=None)
TTH_100_200_T2_R2 =pd.read_csv('', sep=',', header=None)
TTH_100_200_T2_R3 =pd.read_csv('', sep=',', header=None)

# trial 3, robot 1 2 3
TTH_100_200_T3_R1 =pd.read_csv('', sep=',', header=None)
TTH_100_200_T3_R2 =pd.read_csv('', sep=',', header=None)
TTH_100_200_T3_R3 =pd.read_csv('', sep=',', header=None)

# trial 4, robot 1 2 3
TTH_100_200_T4_R1 =pd.read_csv('', sep=',', header=None)
TTH_100_200_T4_R2 =pd.read_csv('', sep=',', header=None)
TTH_100_200_T4_R3 =pd.read_csv('', sep=',', header=None)

# trial 5, robot 1 2 3
TTH_100_200_T5_R1 =pd.read_csv('', sep=',', header=None)
TTH_100_200_T5_R2 =pd.read_csv('', sep=',', header=None)
TTH_100_200_T5_R3 =pd.read_csv('', sep=',', header=None)

# trial 6, robot 1 2 3
TTH_100_200_T6_R1 =pd.read_csv('', sep=',', header=None)
TTH_100_200_T6_R2 =pd.read_csv('', sep=',', header=None)
TTH_100_200_T6_R3 =pd.read_csv('', sep=',', header=None)

# trial 7, robot 1 2 3
TTH_100_200_T7_R1 =pd.read_csv('', sep=',', header=None)
TTH_100_200_T7_R2 =pd.read_csv('', sep=',', header=None)
TTH_100_200_T7_R3 =pd.read_csv('', sep=',', header=None)

# trial 8, robot 1 2 3
TTH_100_200_T8_R1 =pd.read_csv('', sep=',', header=None)
TTH_100_200_T8_R2 =pd.read_csv('', sep=',', header=None)
TTH_100_200_T8_R3 =pd.read_csv('', sep=',', header=None)

# trial 9, robot 1 2 3
TTH_100_200_T9_R1 =pd.read_csv('', sep=',', header=None)
TTH_100_200_T9_R2 =pd.read_csv('', sep=',', header=None)
TTH_100_200_T9_R3 =pd.read_csv('', sep=',', header=None)

# trial 10, robot 1 2 3
TTH_100_200_T10_R1 =pd.read_csv('', sep=',', header=None)
TTH_100_200_T10_R2 =pd.read_csv('', sep=',', header=None)
TTH_100_200_T10_R3 =pd.read_csv('', sep=',', header=None)

# First job is to label columns
TTH_2_6_T1_R1.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
TTH_2_6_T1_R2.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
TTH_2_6_T1_R3.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']

TTH_2_6_T2_R1.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
TTH_2_6_T2_R2.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
TTH_2_6_T2_R3.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']

TTH_2_6_T3_R1.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
TTH_2_6_T3_R2.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
TTH_2_6_T3_R3.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']

TTH_2_6_T4_R1.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
TTH_2_6_T4_R2.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
TTH_2_6_T4_R3.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']

TTH_2_6_T5_R1.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
TTH_2_6_T5_R2.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
TTH_2_6_T5_R3.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']

TTH_2_6_T6_R1.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
TTH_2_6_T6_R2.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
TTH_2_6_T6_R3.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']

TTH_2_6_T7_R1.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
TTH_2_6_T7_R2.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
TTH_2_6_T7_R3.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']

TTH_2_6_T8_R1.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
TTH_2_6_T8_R2.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
TTH_2_6_T8_R3.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']

TTH_2_6_T9_R1.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
TTH_2_6_T9_R2.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
TTH_2_6_T9_R3.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']

TTH_2_6_T10_R1.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
TTH_2_6_T10_R2.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
TTH_2_6_T10_R3.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']

TTH_6_10_T1_R1.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
TTH_6_10_T1_R2.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
TTH_6_10_T1_R3.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']

TTH_6_10_T2_R1.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
TTH_6_10_T2_R2.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
TTH_6_10_T2_R3.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']

TTH_6_10_T3_R1.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
TTH_6_10_T3_R2.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
TTH_6_10_T3_R3.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']

TTH_6_10_T4_R1.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
TTH_6_10_T4_R2.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
TTH_6_10_T4_R3.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']

TTH_6_10_T5_R1.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
TTH_6_10_T5_R2.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
TTH_6_10_T5_R3.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']

TTH_6_10_T6_R1.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
TTH_6_10_T6_R2.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
TTH_6_10_T6_R3.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']

TTH_6_10_T7_R1.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
TTH_6_10_T7_R2.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
TTH_6_10_T7_R3.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']

TTH_6_10_T8_R1.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
TTH_6_10_T8_R2.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
TTH_6_10_T8_R3.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']

TTH_6_10_T9_R1.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
TTH_6_10_T9_R2.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
TTH_6_10_T9_R3.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']

TTH_6_10_T10_R1.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
TTH_6_10_T10_R2.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
TTH_6_10_T10_R3.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']

TTH_100_200_T1_R1.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
TTH_100_200_T1_R2.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
TTH_100_200_T1_R3.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']

TTH_100_200_T2_R1.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
TTH_100_200_T2_R2.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
TTH_100_200_T2_R3.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']

TTH_100_200_T3_R1.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
TTH_100_200_T3_R2.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
TTH_100_200_T3_R3.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']

TTH_100_200_T4_R1.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
TTH_100_200_T4_R2.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
TTH_100_200_T4_R3.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']

TTH_100_200_T5_R1.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
TTH_100_200_T5_R2.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
TTH_100_200_T5_R3.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']

TTH_100_200_T6_R1.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
TTH_100_200_T6_R2.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
TTH_100_200_T6_R3.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']

TTH_100_200_T7_R1.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
TTH_100_200_T7_R2.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
TTH_100_200_T7_R3.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']

TTH_100_200_T8_R1.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
TTH_100_200_T8_R2.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
TTH_100_200_T8_R3.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']

TTH_100_200_T9_R1.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
TTH_100_200_T9_R2.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
TTH_100_200_T9_R3.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']

TTH_100_200_T10_R1.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
TTH_100_200_T10_R2.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
TTH_100_200_T10_R3.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']

NP_T1_R1.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
NP_T1_R2.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
NP_T1_R3.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']

NP_T2_R1.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
NP_T2_R2.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
NP_T2_R3.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']

NP_T3_R1.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
NP_T3_R2.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
NP_T3_R3.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']

NP_T4_R1.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
NP_T4_R2.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
NP_T4_R3.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']

NP_T5_R1.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
NP_T5_R2.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
NP_T5_R3.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']

NP_T6_R1.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
NP_T6_R2.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
NP_T6_R3.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']

NP_T7_R1.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
NP_T7_R2.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
NP_T7_R3.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']

NP_T8_R1.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
NP_T8_R2.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
NP_T8_R3.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']

NP_T9_R1.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
NP_T9_R2.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
NP_T9_R3.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']

NP_T10_R1.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
NP_T10_R2.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
NP_T10_R3.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']



# Add columns to apply labels to data
# TTH 2 6
TTH_2_6_T1_R2.insert(0, 'condition', 'tth_2_6')
TTH_2_6_T1_R1.insert(0, 'condition', 'tth_2_6')
TTH_2_6_T1_R3.insert(0, 'condition', 'tth_2_6')
TTH_2_6_T1_R2.insert(1, 'trial', '1')
TTH_2_6_T1_R1.insert(1, 'trial', '1')
TTH_2_6_T1_R3.insert(1, 'trial', '1')
TTH_2_6_T1_R1.insert(2, 'robot', '1')
TTH_2_6_T1_R2.insert(2, 'robot', '2')
TTH_2_6_T1_R3.insert(2, 'robot', '3')

TTH_2_6_T2_R2.insert(0, 'condition', 'tth_2_6')
TTH_2_6_T2_R1.insert(0, 'condition', 'tth_2_6')
TTH_2_6_T2_R3.insert(0, 'condition', 'tth_2_6')
TTH_2_6_T2_R2.insert(1, 'trial', '2')
TTH_2_6_T2_R1.insert(1, 'trial', '2')
TTH_2_6_T2_R3.insert(1, 'trial', '2')
TTH_2_6_T2_R1.insert(2, 'robot', '1')
TTH_2_6_T2_R2.insert(2, 'robot', '2')
TTH_2_6_T2_R3.insert(2, 'robot', '3')

TTH_2_6_T3_R2.insert(0, 'condition', 'tth_2_6')
TTH_2_6_T3_R1.insert(0, 'condition', 'tth_2_6')
TTH_2_6_T3_R3.insert(0, 'condition', 'tth_2_6')
TTH_2_6_T3_R2.insert(1, 'trial', '3')
TTH_2_6_T3_R1.insert(1, 'trial', '3')
TTH_2_6_T3_R3.insert(1, 'trial', '3')
TTH_2_6_T3_R1.insert(2, 'robot', '1')
TTH_2_6_T3_R2.insert(2, 'robot', '2')
TTH_2_6_T3_R3.insert(2, 'robot', '3')

TTH_2_6_T4_R2.insert(0, 'condition', 'tth_2_6')
TTH_2_6_T4_R1.insert(0, 'condition', 'tth_2_6')
TTH_2_6_T4_R3.insert(0, 'condition', 'tth_2_6')
TTH_2_6_T4_R2.insert(1, 'trial', '4')
TTH_2_6_T4_R1.insert(1, 'trial', '4')
TTH_2_6_T4_R3.insert(1, 'trial', '4')
TTH_2_6_T4_R1.insert(2, 'robot', '1')
TTH_2_6_T4_R2.insert(2, 'robot', '2')
TTH_2_6_T4_R3.insert(2, 'robot', '3')

TTH_2_6_T5_R2.insert(0, 'condition', 'tth_2_6')
TTH_2_6_T5_R1.insert(0, 'condition', 'tth_2_6')
TTH_2_6_T5_R3.insert(0, 'condition', 'tth_2_6')
TTH_2_6_T5_R2.insert(1, 'trial', '3')
TTH_2_6_T5_R1.insert(1, 'trial', '3')
TTH_2_6_T5_R3.insert(1, 'trial', '3')
TTH_2_6_T5_R1.insert(2, 'robot', '1')
TTH_2_6_T5_R2.insert(2, 'robot', '2')
TTH_2_6_T5_R3.insert(2, 'robot', '3')

TTH_2_6_T6_R2.insert(0, 'condition', 'tth_2_6')
TTH_2_6_T6_R1.insert(0, 'condition', 'tth_2_6')
TTH_2_6_T6_R3.insert(0, 'condition', 'tth_2_6')
TTH_2_6_T6_R2.insert(1, 'trial', '4')
TTH_2_6_T6_R1.insert(1, 'trial', '4')
TTH_2_6_T6_R3.insert(1, 'trial', '4')
TTH_2_6_T6_R1.insert(2, 'robot', '1')
TTH_2_6_T6_R2.insert(2, 'robot', '2')
TTH_2_6_T6_R3.insert(2, 'robot', '3')

TTH_2_6_T7_R2.insert(0, 'condition', 'tth_2_6')
TTH_2_6_T7_R1.insert(0, 'condition', 'tth_2_6')
TTH_2_6_T7_R3.insert(0, 'condition', 'tth_2_6')
TTH_2_6_T7_R2.insert(1, 'trial', '3')
TTH_2_6_T7_R1.insert(1, 'trial', '3')
TTH_2_6_T7_R3.insert(1, 'trial', '3')
TTH_2_6_T7_R1.insert(2, 'robot', '1')
TTH_2_6_T7_R2.insert(2, 'robot', '2')
TTH_2_6_T7_R3.insert(2, 'robot', '3')

TTH_2_6_T8_R2.insert(0, 'condition', 'tth_2_6')
TTH_2_6_T8_R1.insert(0, 'condition', 'tth_2_6')
TTH_2_6_T8_R3.insert(0, 'condition', 'tth_2_6')
TTH_2_6_T8_R2.insert(1, 'trial', '4')
TTH_2_6_T8_R1.insert(1, 'trial', '4')
TTH_2_6_T8_R3.insert(1, 'trial', '4')
TTH_2_6_T8_R1.insert(2, 'robot', '1')
TTH_2_6_T8_R2.insert(2, 'robot', '2')
TTH_2_6_T8_R3.insert(2, 'robot', '3')

TTH_2_6_T9_R2.insert(0, 'condition', 'tth_2_6')
TTH_2_6_T9_R1.insert(0, 'condition', 'tth_2_6')
TTH_2_6_T9_R3.insert(0, 'condition', 'tth_2_6')
TTH_2_6_T9_R2.insert(1, 'trial', '3')
TTH_2_6_T9_R1.insert(1, 'trial', '3')
TTH_2_6_T9_R3.insert(1, 'trial', '3')
TTH_2_6_T9_R1.insert(2, 'robot', '1')
TTH_2_6_T9_R2.insert(2, 'robot', '2')
TTH_2_6_T9_R3.insert(2, 'robot', '3')

TTH_2_6_T10_R2.insert(0, 'condition', 'tth_2_6')
TTH_2_6_T10_R1.insert(0, 'condition', 'tth_2_6')
TTH_2_6_T10_R3.insert(0, 'condition', 'tth_2_6')
TTH_2_6_T10_R2.insert(1, 'trial', '4')
TTH_2_6_T10_R1.insert(1, 'trial', '4')
TTH_2_6_T10_R3.insert(1, 'trial', '4')
TTH_2_6_T10_R1.insert(2, 'robot', '1')
TTH_2_6_T10_R2.insert(2, 'robot', '2')
TTH_2_6_T10_R3.insert(2, 'robot', '3')


# TTH 6 10
TTH_6_10_T1_R2.insert(0, 'condition', 'tth_6_10')
TTH_6_10_T1_R1.insert(0, 'condition', 'tth_6_10')
TTH_6_10_T1_R3.insert(0, 'condition', 'tth_6_10')
TTH_6_10_T1_R2.insert(1, 'trial', '1')
TTH_6_10_T1_R1.insert(1, 'trial', '1')
TTH_6_10_T1_R3.insert(1, 'trial', '1')
TTH_6_10_T1_R1.insert(2, 'robot', '1')
TTH_6_10_T1_R2.insert(2, 'robot', '2')
TTH_6_10_T1_R3.insert(2, 'robot', '3')

TTH_6_10_T2_R2.insert(0, 'condition', 'tth_6_10')
TTH_6_10_T2_R1.insert(0, 'condition', 'tth_6_10')
TTH_6_10_T2_R3.insert(0, 'condition', 'tth_6_10')
TTH_6_10_T2_R2.insert(1, 'trial', '2')
TTH_6_10_T2_R1.insert(1, 'trial', '2')
TTH_6_10_T2_R3.insert(1, 'trial', '2')
TTH_6_10_T2_R1.insert(2, 'robot', '1')
TTH_6_10_T2_R2.insert(2, 'robot', '2')
TTH_6_10_T2_R3.insert(2, 'robot', '3')

TTH_6_10_T3_R2.insert(0, 'condition', 'tth_6_10')
TTH_6_10_T3_R1.insert(0, 'condition', 'tth_6_10')
TTH_6_10_T3_R3.insert(0, 'condition', 'tth_6_10')
TTH_6_10_T3_R2.insert(1, 'trial', '3')
TTH_6_10_T3_R1.insert(1, 'trial', '3')
TTH_6_10_T3_R3.insert(1, 'trial', '3')
TTH_6_10_T3_R1.insert(2, 'robot', '1')
TTH_6_10_T3_R2.insert(2, 'robot', '2')
TTH_6_10_T3_R3.insert(2, 'robot', '3')

TTH_6_10_T4_R2.insert(0, 'condition', 'tth_6_10')
TTH_6_10_T4_R1.insert(0, 'condition', 'tth_6_10')
TTH_6_10_T4_R3.insert(0, 'condition', 'tth_6_10')
TTH_6_10_T4_R2.insert(1, 'trial', '4')
TTH_6_10_T4_R1.insert(1, 'trial', '4')
TTH_6_10_T4_R3.insert(1, 'trial', '4')
TTH_6_10_T4_R1.insert(2, 'robot', '1')
TTH_6_10_T4_R2.insert(2, 'robot', '2')
TTH_6_10_T4_R3.insert(2, 'robot', '3')

TTH_6_10_T5_R2.insert(0, 'condition', 'tth_6_10')
TTH_6_10_T5_R1.insert(0, 'condition', 'tth_6_10')
TTH_6_10_T5_R3.insert(0, 'condition', 'tth_6_10')
TTH_6_10_T5_R2.insert(1, 'trial', '3')
TTH_6_10_T5_R1.insert(1, 'trial', '3')
TTH_6_10_T5_R3.insert(1, 'trial', '3')
TTH_6_10_T5_R1.insert(2, 'robot', '1')
TTH_6_10_T5_R2.insert(2, 'robot', '2')
TTH_6_10_T5_R3.insert(2, 'robot', '3')

TTH_6_10_T6_R2.insert(0, 'condition', 'tth_6_10')
TTH_6_10_T6_R1.insert(0, 'condition', 'tth_6_10')
TTH_6_10_T6_R3.insert(0, 'condition', 'tth_6_10')
TTH_6_10_T6_R2.insert(1, 'trial', '4')
TTH_6_10_T6_R1.insert(1, 'trial', '4')
TTH_6_10_T6_R3.insert(1, 'trial', '4')
TTH_6_10_T6_R1.insert(2, 'robot', '1')
TTH_6_10_T6_R2.insert(2, 'robot', '2')
TTH_6_10_T6_R3.insert(2, 'robot', '3')

TTH_6_10_T7_R2.insert(0, 'condition', 'tth_6_10')
TTH_6_10_T7_R1.insert(0, 'condition', 'tth_6_10')
TTH_6_10_T7_R3.insert(0, 'condition', 'tth_6_10')
TTH_6_10_T7_R2.insert(1, 'trial', '3')
TTH_6_10_T7_R1.insert(1, 'trial', '3')
TTH_6_10_T7_R3.insert(1, 'trial', '3')
TTH_6_10_T7_R1.insert(2, 'robot', '1')
TTH_6_10_T7_R2.insert(2, 'robot', '2')
TTH_6_10_T7_R3.insert(2, 'robot', '3')

TTH_6_10_T8_R2.insert(0, 'condition', 'tth_6_10')
TTH_6_10_T8_R1.insert(0, 'condition', 'tth_6_10')
TTH_6_10_T8_R3.insert(0, 'condition', 'tth_6_10')
TTH_6_10_T8_R2.insert(1, 'trial', '4')
TTH_6_10_T8_R1.insert(1, 'trial', '4')
TTH_6_10_T8_R3.insert(1, 'trial', '4')
TTH_6_10_T8_R1.insert(2, 'robot', '1')
TTH_6_10_T8_R2.insert(2, 'robot', '2')
TTH_6_10_T8_R3.insert(2, 'robot', '3')

TTH_6_10_T9_R2.insert(0, 'condition', 'tth_6_10')
TTH_6_10_T9_R1.insert(0, 'condition', 'tth_6_10')
TTH_6_10_T9_R3.insert(0, 'condition', 'tth_6_10')
TTH_6_10_T9_R2.insert(1, 'trial', '3')
TTH_6_10_T9_R1.insert(1, 'trial', '3')
TTH_6_10_T9_R3.insert(1, 'trial', '3')
TTH_6_10_T9_R1.insert(2, 'robot', '1')
TTH_6_10_T9_R2.insert(2, 'robot', '2')
TTH_6_10_T9_R3.insert(2, 'robot', '3')

TTH_6_10_T10_R2.insert(0, 'condition', 'tth_6_10')
TTH_6_10_T10_R1.insert(0, 'condition', 'tth_6_10')
TTH_6_10_T10_R3.insert(0, 'condition', 'tth_6_10')
TTH_6_10_T10_R2.insert(1, 'trial', '4')
TTH_6_10_T10_R1.insert(1, 'trial', '4')
TTH_6_10_T10_R3.insert(1, 'trial', '4')
TTH_6_10_T10_R1.insert(2, 'robot', '1')
TTH_6_10_T10_R2.insert(2, 'robot', '2')
TTH_6_10_T10_R3.insert(2, 'robot', '3')



# TTH 100 200
TTH_100_200_T1_R2.insert(0, 'condition', 'tth_100_200')
TTH_100_200_T1_R1.insert(0, 'condition', 'tth_100_200')
TTH_100_200_T1_R3.insert(0, 'condition', 'tth_100_200')
TTH_100_200_T1_R2.insert(1, 'trial', '1')
TTH_100_200_T1_R1.insert(1, 'trial', '1')
TTH_100_200_T1_R3.insert(1, 'trial', '1')
TTH_100_200_T1_R1.insert(2, 'robot', '1')
TTH_100_200_T1_R2.insert(2, 'robot', '2')
TTH_100_200_T1_R3.insert(2, 'robot', '3')

TTH_100_200_T2_R2.insert(0, 'condition', 'tth_100_200')
TTH_100_200_T2_R1.insert(0, 'condition', 'tth_100_200')
TTH_100_200_T2_R3.insert(0, 'condition', 'tth_100_200')
TTH_100_200_T2_R2.insert(1, 'trial', '2')
TTH_100_200_T2_R1.insert(1, 'trial', '2')
TTH_100_200_T2_R3.insert(1, 'trial', '2')
TTH_100_200_T2_R1.insert(2, 'robot', '1')
TTH_100_200_T2_R2.insert(2, 'robot', '2')
TTH_100_200_T2_R3.insert(2, 'robot', '3')

TTH_100_200_T3_R2.insert(0, 'condition', 'tth_100_200')
TTH_100_200_T3_R1.insert(0, 'condition', 'tth_100_200')
TTH_100_200_T3_R3.insert(0, 'condition', 'tth_100_200')
TTH_100_200_T3_R2.insert(1, 'trial', '3')
TTH_100_200_T3_R1.insert(1, 'trial', '3')
TTH_100_200_T3_R3.insert(1, 'trial', '3')
TTH_100_200_T3_R1.insert(2, 'robot', '1')
TTH_100_200_T3_R2.insert(2, 'robot', '2')
TTH_100_200_T3_R3.insert(2, 'robot', '3')

TTH_100_200_T4_R2.insert(0, 'condition', 'tth_100_200')
TTH_100_200_T4_R1.insert(0, 'condition', 'tth_100_200')
TTH_100_200_T4_R3.insert(0, 'condition', 'tth_100_200')
TTH_100_200_T4_R2.insert(1, 'trial', '4')
TTH_100_200_T4_R1.insert(1, 'trial', '4')
TTH_100_200_T4_R3.insert(1, 'trial', '4')
TTH_100_200_T4_R1.insert(2, 'robot', '1')
TTH_100_200_T4_R2.insert(2, 'robot', '2')
TTH_100_200_T4_R3.insert(2, 'robot', '3')

TTH_100_200_T5_R2.insert(0, 'condition', 'tth_100_200')
TTH_100_200_T5_R1.insert(0, 'condition', 'tth_100_200')
TTH_100_200_T5_R3.insert(0, 'condition', 'tth_100_200')
TTH_100_200_T5_R2.insert(1, 'trial', '3')
TTH_100_200_T5_R1.insert(1, 'trial', '3')
TTH_100_200_T5_R3.insert(1, 'trial', '3')
TTH_100_200_T5_R1.insert(2, 'robot', '1')
TTH_100_200_T5_R2.insert(2, 'robot', '2')
TTH_100_200_T5_R3.insert(2, 'robot', '3')

TTH_100_200_T6_R2.insert(0, 'condition', 'tth_100_200')
TTH_100_200_T6_R1.insert(0, 'condition', 'tth_100_200')
TTH_100_200_T6_R3.insert(0, 'condition', 'tth_100_200')
TTH_100_200_T6_R2.insert(1, 'trial', '4')
TTH_100_200_T6_R1.insert(1, 'trial', '4')
TTH_100_200_T6_R3.insert(1, 'trial', '4')
TTH_100_200_T6_R1.insert(2, 'robot', '1')
TTH_100_200_T6_R2.insert(2, 'robot', '2')
TTH_100_200_T6_R3.insert(2, 'robot', '3')

TTH_100_200_T7_R2.insert(0, 'condition', 'tth_100_200')
TTH_100_200_T7_R1.insert(0, 'condition', 'tth_100_200')
TTH_100_200_T7_R3.insert(0, 'condition', 'tth_100_200')
TTH_100_200_T7_R2.insert(1, 'trial', '3')
TTH_100_200_T7_R1.insert(1, 'trial', '3')
TTH_100_200_T7_R3.insert(1, 'trial', '3')
TTH_100_200_T7_R1.insert(2, 'robot', '1')
TTH_100_200_T7_R2.insert(2, 'robot', '2')
TTH_100_200_T7_R3.insert(2, 'robot', '3')

TTH_100_200_T8_R2.insert(0, 'condition', 'tth_100_200')
TTH_100_200_T8_R1.insert(0, 'condition', 'tth_100_200')
TTH_100_200_T8_R3.insert(0, 'condition', 'tth_100_200')
TTH_100_200_T8_R2.insert(1, 'trial', '4')
TTH_100_200_T8_R1.insert(1, 'trial', '4')
TTH_100_200_T8_R3.insert(1, 'trial', '4')
TTH_100_200_T8_R1.insert(2, 'robot', '1')
TTH_100_200_T8_R2.insert(2, 'robot', '2')
TTH_100_200_T8_R3.insert(2, 'robot', '3')

TTH_100_200_T9_R2.insert(0, 'condition', 'tth_100_200')
TTH_100_200_T9_R1.insert(0, 'condition', 'tth_100_200')
TTH_100_200_T9_R3.insert(0, 'condition', 'tth_100_200')
TTH_100_200_T9_R2.insert(1, 'trial', '3')
TTH_100_200_T9_R1.insert(1, 'trial', '3')
TTH_100_200_T9_R3.insert(1, 'trial', '3')
TTH_100_200_T9_R1.insert(2, 'robot', '1')
TTH_100_200_T9_R2.insert(2, 'robot', '2')
TTH_100_200_T9_R3.insert(2, 'robot', '3')

TTH_100_200_T10_R2.insert(0, 'condition', 'tth_100_200')
TTH_100_200_T10_R1.insert(0, 'condition', 'tth_100_200')
TTH_100_200_T10_R3.insert(0, 'condition', 'tth_100_200')
TTH_100_200_T10_R2.insert(1, 'trial', '4')
TTH_100_200_T10_R1.insert(1, 'trial', '4')
TTH_100_200_T10_R3.insert(1, 'trial', '4')
TTH_100_200_T10_R1.insert(2, 'robot', '1')
TTH_100_200_T10_R2.insert(2, 'robot', '2')
TTH_100_200_T10_R3.insert(2, 'robot', '3')



# NP
NP_T1_R2.insert(0, 'condition', 'NP')
NP_T1_R1.insert(0, 'condition', 'NP')
NP_T1_R3.insert(0, 'condition', 'NP')
NP_T1_R2.insert(1, 'trial', '1')
NP_T1_R1.insert(1, 'trial', '1')
NP_T1_R3.insert(1, 'trial', '1')
NP_T1_R1.insert(2, 'robot', '1')
NP_T1_R2.insert(2, 'robot', '2')
NP_T1_R3.insert(2, 'robot', '3')

NP_T2_R2.insert(0, 'condition', 'NP')
NP_T2_R1.insert(0, 'condition', 'NP')
NP_T2_R3.insert(0, 'condition', 'NP')
NP_T2_R2.insert(1, 'trial', '2')
NP_T2_R1.insert(1, 'trial', '2')
NP_T2_R3.insert(1, 'trial', '2')
NP_T2_R1.insert(2, 'robot', '1')
NP_T2_R2.insert(2, 'robot', '2')
NP_T2_R3.insert(2, 'robot', '3')

NP_T3_R2.insert(0, 'condition', 'NP')
NP_T3_R1.insert(0, 'condition', 'NP')
NP_T3_R3.insert(0, 'condition', 'NP')
NP_T3_R2.insert(1, 'trial', '3')
NP_T3_R1.insert(1, 'trial', '3')
NP_T3_R3.insert(1, 'trial', '3')
NP_T3_R1.insert(2, 'robot', '1')
NP_T3_R2.insert(2, 'robot', '2')
NP_T3_R3.insert(2, 'robot', '3')

NP_T4_R2.insert(0, 'condition', 'NP')
NP_T4_R1.insert(0, 'condition', 'NP')
NP_T4_R3.insert(0, 'condition', 'NP')
NP_T4_R2.insert(1, 'trial', '4')
NP_T4_R1.insert(1, 'trial', '4')
NP_T4_R3.insert(1, 'trial', '4')
NP_T4_R1.insert(2, 'robot', '1')
NP_T4_R2.insert(2, 'robot', '2')
NP_T4_R3.insert(2, 'robot', '3')

NP_T5_R2.insert(0, 'condition', 'NP')
NP_T5_R1.insert(0, 'condition', 'NP')
NP_T5_R3.insert(0, 'condition', 'NP')
NP_T5_R2.insert(1, 'trial', '3')
NP_T5_R1.insert(1, 'trial', '3')
NP_T5_R3.insert(1, 'trial', '3')
NP_T5_R1.insert(2, 'robot', '1')
NP_T5_R2.insert(2, 'robot', '2')
NP_T5_R3.insert(2, 'robot', '3')

NP_T6_R2.insert(0, 'condition', 'NP')
NP_T6_R1.insert(0, 'condition', 'NP')
NP_T6_R3.insert(0, 'condition', 'NP')
NP_T6_R2.insert(1, 'trial', '4')
NP_T6_R1.insert(1, 'trial', '4')
NP_T6_R3.insert(1, 'trial', '4')
NP_T6_R1.insert(2, 'robot', '1')
NP_T6_R2.insert(2, 'robot', '2')
NP_T6_R3.insert(2, 'robot', '3')

NP_T7_R2.insert(0, 'condition', 'NP')
NP_T7_R1.insert(0, 'condition', 'NP')
NP_T7_R3.insert(0, 'condition', 'NP')
NP_T7_R2.insert(1, 'trial', '3')
NP_T7_R1.insert(1, 'trial', '3')
NP_T7_R3.insert(1, 'trial', '3')
NP_T7_R1.insert(2, 'robot', '1')
NP_T7_R2.insert(2, 'robot', '2')
NP_T7_R3.insert(2, 'robot', '3')

NP_T8_R2.insert(0, 'condition', 'NP')
NP_T8_R1.insert(0, 'condition', 'NP')
NP_T8_R3.insert(0, 'condition', 'NP')
NP_T8_R2.insert(1, 'trial', '4')
NP_T8_R1.insert(1, 'trial', '4')
NP_T8_R3.insert(1, 'trial', '4')
NP_T8_R1.insert(2, 'robot', '1')
NP_T8_R2.insert(2, 'robot', '2')
NP_T8_R3.insert(2, 'robot', '3')

NP_T9_R2.insert(0, 'condition', 'NP')
NP_T9_R1.insert(0, 'condition', 'NP')
NP_T9_R3.insert(0, 'condition', 'NP')
NP_T9_R2.insert(1, 'trial', '3')
NP_T9_R1.insert(1, 'trial', '3')
NP_T9_R3.insert(1, 'trial', '3')
NP_T9_R1.insert(2, 'robot', '1')
NP_T9_R2.insert(2, 'robot', '2')
NP_T9_R3.insert(2, 'robot', '3')

NP_T10_R2.insert(0, 'condition', 'NP')
NP_T10_R1.insert(0, 'condition', 'NP')
NP_T10_R3.insert(0, 'condition', 'NP')
NP_T10_R2.insert(1, 'trial', '4')
NP_T10_R1.insert(1, 'trial', '4')
NP_T10_R3.insert(1, 'trial', '4')
NP_T10_R1.insert(2, 'robot', '1')
NP_T10_R2.insert(2, 'robot', '2')
NP_T10_R3.insert(2, 'robot', '3')


# Stick the individual dataframes in an array
frames = [ TTH_2_6_T1_R1,  TTH_2_6_T1_R2,  TTH_2_6_T1_R3,
           TTH_2_6_T2_R1, TTH_2_6_T2_R2, TTH_2_6_T2_R3, 
            TTH_2_6_T3_R1, TTH_2_6_T3_R2, TTH_2_6_T3_R3, 
            TTH_2_6_T4_R1, TTH_2_6_T4_R2, TTH_2_6_T4_R3, 
            TTH_2_6_T5_R1, TTH_2_6_T5_R2, TTH_2_6_T5_R3, 
            TTH_2_6_T6_R1, TTH_2_6_T6_R2, TTH_2_6_T6_R3, 
            TTH_2_6_T7_R1, TTH_2_6_T7_R2, TTH_2_6_T7_R3, 
            TTH_2_6_T8_R1, TTH_2_6_T8_R2, TTH_2_6_T8_R3, 
            TTH_2_6_T9_R1, TTH_2_6_T9_R2, TTH_2_6_T9_R3, 
            TTH_2_6_T10_R1, TTH_2_6_T10_R2, TTH_2_6_T10_R3, 
            TTH_6_10_T1_R1, TTH_6_10_T1_R2, TTH_6_10_T1_R3, 
            TTH_6_10_T2_R1, TTH_6_10_T2_R2, TTH_6_10_T2_R3, 
            TTH_6_10_T3_R1, TTH_6_10_T3_R2, TTH_6_10_T3_R3, 
            TTH_6_10_T4_R1, TTH_6_10_T4_R2, TTH_6_10_T4_R3, 
            TTH_6_10_T5_R1, TTH_6_10_T5_R2, TTH_6_10_T5_R3, 
            TTH_6_10_T6_R1, TTH_6_10_T6_R2, TTH_6_10_T6_R3, 
            TTH_6_10_T7_R1, TTH_6_10_T7_R2, TTH_6_10_T7_R3, 
            TTH_6_10_T8_R1, TTH_6_10_T8_R2, TTH_6_10_T8_R3, 
            TTH_6_10_T9_R1, TTH_6_10_T9_R2, TTH_6_10_T9_R3, 
            TTH_6_10_T10_R1, TTH_6_10_T10_R2, TTH_6_10_T10_R3, 
            TTH_100_200_T1_R1, TTH_100_200_T1_R2, TTH_100_200_T1_R3, 
            TTH_100_200_T2_R1, TTH_100_200_T2_R2, TTH_100_200_T2_R3, 
            TTH_100_200_T3_R1, TTH_100_200_T3_R2, TTH_100_200_T3_R3, 
            TTH_100_200_T4_R1, TTH_100_200_T4_R2, TTH_100_200_T4_R3, 
            TTH_100_200_T5_R1, TTH_100_200_T5_R2, TTH_100_200_T5_R3, 
            TTH_100_200_T6_R1, TTH_100_200_T6_R2, TTH_100_200_T6_R3, 
            TTH_100_200_T7_R1, TTH_100_200_T7_R2, TTH_100_200_T7_R3, 
            TTH_100_200_T8_R1, TTH_100_200_T8_R2, TTH_100_200_T8_R3, 
            TTH_100_200_T9_R1, TTH_100_200_T9_R2, TTH_100_200_T9_R3, 
            TTH_100_200_T10_R1, TTH_100_200_T10_R2, TTH_100_200_T10_R3, 
            NP_T1_R1, NP_T1_R2, NP_T1_R3, 
            NP_T2_R1, NP_T2_R2, NP_T2_R3, 
            NP_T3_R1, NP_T3_R2, NP_T3_R3, 
            NP_T4_R1, NP_T4_R2, NP_T4_R3, 
            NP_T5_R1, NP_T5_R2, NP_T5_R3, 
            NP_T6_R1, NP_T6_R2, NP_T6_R3, 
            NP_T7_R1, NP_T7_R2, NP_T7_R3, 
            NP_T8_R1, NP_T8_R2, NP_T8_R3, 
            NP_T9_R1, NP_T9_R2, NP_T9_R3, 
            NP_T10_R1, NP_T10_R2, NP_T10_R3]


# Concatenate them together into 1 dataframe
all_df = pd.concat(frames, ignore_index=True)


# Your data has high resolution precision on time,
# which means the x-axis will get indexed with individual
# time markers, rather than collating per second (for example)
# This means that we can't plot a distribution, because every
# row of data for every trial appears unique.
# It look like your data is per second, just with some
# arbitrary offset.  Rounding down (0 decimal places)
# seems to fix this.
all_df['time'] = all_df['time'].round(0)

# Make sure our numeric columns are not strings
all_df["robot"] = pd.to_numeric(all_df["robot"])
all_df["trial"] = pd.to_numeric(all_df["trial"])
all_df["activation"] = pd.to_numeric(all_df["activation"])
all_df["state"] = pd.to_numeric(all_df["state"])
all_df["cumul_tags"] = pd.to_numeric(all_df["cumul_tags"])

# It looks like you have some NaN's?
print( "Oops, number of NaN's: ", all_df.isnull().sum().sum() )


# Exclude data based on our min max time values above
all_df = all_df[ ( all_df['time'] >= min_time ) ]
all_df = all_df[ ( all_df['time'] <= max_time ) ]

# We can peek inside each file to
# check formatting like this
print( all_df )





# Results 2 6
subset = all_df[ ( all_df['condition'] == 'tth_2_6' ) ]
#print( subset )


# Set y-axis limits
y_limits = (0, 110)

# having trouble with hue colours
colours = dict(zip(subset['robot'].unique(), sns.color_palette(n_colors=len(subset['robot'].unique()))))

lplot = sns.relplot(data=subset, x='time', y='activation', kind='line', hue='robot', palette=colours, height=5, aspect=2, errorbar=('ci',95) )
lplot.fig.suptitle('Inspecting how robots compare within TTH 2 6 across all trials', fontsize=16)

# Set y-axis limits
plt.ylim(y_limits)
plt.axhline(y=50, linestyle='--', linewidth=0.8, c='hotpink')

plt.xlabel('Time (s)')
plt.ylabel('Activity Level')

plt.show()




# Results 6 10
subset = all_df[ ( all_df['condition'] == 'tth_6_10' ) ]
#print( subset )


# Set y-axis limits
y_limits = (0, 110)

# having trouble with hue colours
colours = dict(zip(subset['robot'].unique(), sns.color_palette(n_colors=len(subset['robot'].unique()))))

lplot = sns.relplot(data=subset, x='time', y='activation', kind='line', hue='robot', palette=colours, height=5, aspect=2, errorbar=('ci',95) )
lplot.fig.suptitle('Inspecting how robots compare within TTH 6 10 across all trials', fontsize=16)

# Set y-axis limits
plt.ylim(y_limits)
plt.axhline(y=50, linestyle='--', linewidth=0.8, c='hotpink')

plt.xlabel('Time (s)')
plt.ylabel('Activity Level')

plt.show()


# Result 100 200

subset = all_df[ ( all_df['condition'] == 'tth_100_200' ) ]
#print( subset )

# Set y-axis limits
y_limits = (0, 110)

# having trouble with hue colours
colours = dict(zip(subset['robot'].unique(), sns.color_palette(n_colors=len(subset['robot'].unique()))))

lplot = sns.relplot(data=subset, x='time', y='activation', kind='line', hue='robot', palette=colours, height=5, aspect=2, errorbar=('ci',95) )
lplot.fig.suptitle('Inspecting how robots compare within TTH 100 200 across all trials - Sim', fontsize=16)

# Set y-axis limits
plt.ylim(y_limits)
plt.axhline(y=50, linestyle='--', linewidth=0.8, c='hotpink')


plt.xlabel('Time (s)')
plt.ylabel('Activity Level')

plt.show()

# Results all compared 
subset = all_df[ ( all_df['time'] < max_time ) ]
subset = all_df[ ( all_df['condition'] != 'NP' ) ]
#print( subset )



# having trouble with hue colours
colours = dict(zip(subset['condition'].unique(), sns.color_palette(n_colors=len(subset['condition'].unique()))))

lplot = sns.relplot(data=subset, x='time', y='activation', kind='line', hue='condition', palette=colours, height=5, aspect=2, errorbar=('ci',95) )
lplot.fig.suptitle('Comparing TTH 2 6 against TTH 6 10 & TTH 100 200, across all robots & trials', fontsize=16)

plt.axhline(y=50, linestyle='--', linewidth=0.8, c='hotpink')


plt.xlabel('Time (s)')
plt.ylabel('Activity Level')

plt.show()

# total tags all conditions all trials



# Fetch the final tag count for each trial, for each scenario
subset = all_df[ ( all_df['time'] < max_time ) ]
subset = subset[ ( subset['condition'] == 'tth_2_6' ) ]
tth_2_6_tags = subset.groupby(['trial'])['cumul_tags'].max() # from https://stackoverflow.com/a/57595535

subset = all_df[ ( all_df['time'] < max_time ) ]
subset = subset[ ( subset['condition'] == 'tth_6_10' ) ]
tth_6_10_tags = subset.groupby(['trial'])['cumul_tags'].max()

subset = all_df[ ( all_df['time'] < max_time ) ]
subset = subset[ ( subset['condition']== 'tth_100_200' ) ]
tth_100_200_tags = subset.groupby(['trial'])['cumul_tags'].max()

subset = all_df[ ( all_df['time'] < max_time ) ]
subset = subset[ ( subset['condition'] == 'NP' ) ]
np_tags = subset.groupby(['trial'])['cumul_tags'].max()


tags = { 'tth_2_6' : tth_2_6_tags,
        'tth_6_10' : tth_6_10_tags,
        'tth_100_200' : tth_100_200_tags,
         'np' : np_tags,
         }

df = pd.DataFrame( tags )
print(df)

#colours = dict(zip(subset['robot'].unique(), sns.color_palette(n_colors=len(subset['robot'].unique()))))
bplot = sns.boxplot( data=df, width=0.4)
bplot.set_xlabel('Experiment Condition')
bplot.set_ylabel('Final Tag Count')
bplot.set_title('Final Count of Collected Tags Across All Conditions')
plt.show()
