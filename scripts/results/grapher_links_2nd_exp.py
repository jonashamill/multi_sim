
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

#NP
#trial 1, robot 1 2 3
NP_T1_R1 =pd.read_csv('src/multi_sim/logs/2nd_exp/robot1/NP/trial_1/metrics/20240229000118_robot1_NP_trial_1_metricspog.csv', sep=',', header=None)
NP_T1_R2 =pd.read_csv('src/multi_sim/logs/2nd_exp/robot2/NP/trial_1/metrics/20240229000119_robot2_NP_trial_1_metricspog.csv', sep=',', header=None)
NP_T1_R3 =pd.read_csv('src/multi_sim/logs/2nd_exp/robot3/NP/trial_1/metrics/20240229000119_robot3_NP_trial_1_metricspog.csv', sep=',', header=None)

#trial 2, robot 1 2 3
NP_T2_R1 =pd.read_csv('src/multi_sim/logs/2nd_exp/robot1/NP/trial_2/metrics/20240229002149_robot1_NP_trial_2_metricspog.csv', sep=',', header=None)
NP_T2_R2 =pd.read_csv('src/multi_sim/logs/2nd_exp/robot2/NP/trial_2/metrics/20240229002149_robot2_NP_trial_2_metricspog.csv', sep=',', header=None)
NP_T2_R3 =pd.read_csv('src/multi_sim/logs/2nd_exp/robot3/NP/trial_2/metrics/20240229002149_robot3_NP_trial_2_metricspog.csv', sep=',', header=None)

#trial 3, robot 1 2 3
NP_T3_R1 =pd.read_csv('src/multi_sim/logs/2nd_exp/robot1/NP/trial_3/metrics/20240229004219_robot1_NP_trial_3_metricspog.csv', sep=',', header=None)
NP_T3_R2 =pd.read_csv('src/multi_sim/logs/2nd_exp/robot2/NP/trial_3/metrics/20240229004219_robot2_NP_trial_3_metricspog.csv', sep=',', header=None)
NP_T3_R3 =pd.read_csv('src/multi_sim/logs/2nd_exp/robot3/NP/trial_3/metrics/20240229004219_robot3_NP_trial_3_metricspog.csv', sep=',', header=None)

#trial 4, robot 1 2 3
NP_T4_R1 =pd.read_csv('src/multi_sim/logs/2nd_exp/robot1/NP/trial_4/metrics/20240229010249_robot1_NP_trial_4_metricspog.csv', sep=',', header=None)
NP_T4_R2 =pd.read_csv('src/multi_sim/logs/2nd_exp/robot2/NP/trial_4/metrics/20240229010249_robot2_NP_trial_4_metricspog.csv', sep=',', header=None)
NP_T4_R3 =pd.read_csv('src/multi_sim/logs/2nd_exp/robot3/NP/trial_4/metrics/20240229010249_robot3_NP_trial_4_metricspog.csv', sep=',', header=None)

#trial 5, robot 1 2 3
NP_T5_R1 =pd.read_csv('src/multi_sim/logs/2nd_exp/robot1/NP/trial_5/metrics/20240229012319_robot1_NP_trial_5_metricspog.csv', sep=',', header=None)
NP_T5_R2 =pd.read_csv('src/multi_sim/logs/2nd_exp/robot2/NP/trial_5/metrics/20240229012320_robot2_NP_trial_5_metricspog.csv', sep=',', header=None)
NP_T5_R3 =pd.read_csv('src/multi_sim/logs/2nd_exp/robot3/NP/trial_5/metrics/20240229012320_robot3_NP_trial_5_metricspog.csv', sep=',', header=None)

#trial 6, robot 1 2 3
NP_T6_R1 =pd.read_csv('src/multi_sim/logs/2nd_exp/robot1/NP/trial_6/metrics/20240229014350_robot1_NP_trial_6_metricspog.csv', sep=',', header=None)
NP_T6_R2 =pd.read_csv('src/multi_sim/logs/2nd_exp/robot2/NP/trial_6/metrics/20240229014350_robot2_NP_trial_6_metricspog.csv', sep=',', header=None)
NP_T6_R3 =pd.read_csv('src/multi_sim/logs/2nd_exp/robot3/NP/trial_6/metrics/20240229014350_robot3_NP_trial_6_metricspog.csv', sep=',', header=None)

#trial 7, robot 1 2 3
NP_T7_R1 =pd.read_csv('src/multi_sim/logs/2nd_exp/robot1/NP/trial_7/metrics/20240229020420_robot1_NP_trial_7_metricspog.csv', sep=',', header=None)
NP_T7_R2 =pd.read_csv('src/multi_sim/logs/2nd_exp/robot2/NP/trial_7/metrics/20240229020420_robot2_NP_trial_7_metricspog.csv', sep=',', header=None)
NP_T7_R3 =pd.read_csv('src/multi_sim/logs/2nd_exp/robot3/NP/trial_7/metrics/20240229020420_robot3_NP_trial_7_metricspog.csv', sep=',', header=None)

#trial 8, robot 1 2 3
NP_T8_R1 =pd.read_csv('src/multi_sim/logs/2nd_exp/robot1/NP/trial_8/metrics/20240229022450_robot1_NP_trial_8_metricspog.csv', sep=',', header=None)
NP_T8_R2 =pd.read_csv('src/multi_sim/logs/2nd_exp/robot2/NP/trial_8/metrics/20240229022450_robot2_NP_trial_8_metricspog.csv', sep=',', header=None)
NP_T8_R3 =pd.read_csv('src/multi_sim/logs/2nd_exp/robot3/NP/trial_8/metrics/20240229022450_robot3_NP_trial_8_metricspog.csv', sep=',', header=None)

#trial 9, robot 1 2 3
NP_T9_R1 =pd.read_csv('src/multi_sim/logs/2nd_exp/robot1/NP/trial_9/metrics/20240229024520_robot1_NP_trial_9_metricspog.csv', sep=',', header=None)
NP_T9_R2 =pd.read_csv('src/multi_sim/logs/2nd_exp/robot2/NP/trial_9/metrics/20240229024520_robot2_NP_trial_9_metricspog.csv', sep=',', header=None)
NP_T9_R3 =pd.read_csv('src/multi_sim/logs/2nd_exp/robot3/NP/trial_9/metrics/20240229024521_robot3_NP_trial_9_metricspog.csv', sep=',', header=None)

#trial 10, robot 1 2 3
NP_T10_R1 =pd.read_csv('src/multi_sim/logs/2nd_exp/robot1/NP/trial_10/metrics/20240229030550_robot1_NP_trial_10_metricspog.csv', sep=',', header=None)
NP_T10_R2 =pd.read_csv('src/multi_sim/logs/2nd_exp/robot2/NP/trial_10/metrics/20240229030551_robot2_NP_trial_10_metricspog.csv', sep=',', header=None)
NP_T10_R3 =pd.read_csv('src/multi_sim/logs/2nd_exp/robot3/NP/trial_10/metrics/20240229030551_robot3_NP_trial_10_metricspog.csv', sep=',', header=None)

#TTH 2 6
#trial 1, robot 1 2 3
TTH_2_6_T1_R1= pd.read_csv('src/multi_sim/logs/2nd_exp/robot1/TTH_2_6/trial_1/metrics/20240229032621_robot1_TTH_2_6_trial_1_metricspog.csv', sep=',', header=None)
TTH_2_6_T1_R2 =pd.read_csv('src/multi_sim/logs/2nd_exp/robot2/TTH_2_6/trial_1/metrics/20240229032621_robot2_TTH_2_6_trial_1_metricspog.csv', sep=',', header=None)
TTH_2_6_T1_R3 =pd.read_csv('src/multi_sim/logs/2nd_exp/robot3/TTH_2_6/trial_1/metrics/20240229032621_robot3_TTH_2_6_trial_1_metricspog.csv', sep=',', header=None)

#trial 2, robot 1 2 3
TTH_2_6_T2_R1= pd.read_csv('src/multi_sim/logs/2nd_exp/robot1/TTH_2_6/trial_2/metrics/20240229034651_robot1_TTH_2_6_trial_2_metricspog.csv', sep=',', header=None)
TTH_2_6_T2_R2 =pd.read_csv('src/multi_sim/logs/2nd_exp/robot2/TTH_2_6/trial_2/metrics/20240229034651_robot2_TTH_2_6_trial_2_metricspog.csv', sep=',', header=None)
TTH_2_6_T2_R3= pd.read_csv('src/multi_sim/logs/2nd_exp/robot3/TTH_2_6/trial_2/metrics/20240229034651_robot3_TTH_2_6_trial_2_metricspog.csv', sep=',', header=None)

#trial 3, robot 1 2 3
TTH_2_6_T3_R1= pd.read_csv('src/multi_sim/logs/2nd_exp/robot1/TTH_2_6/trial_3/metrics/20240229040721_robot1_TTH_2_6_trial_3_metricspog.csv', sep=',', header=None)
TTH_2_6_T3_R2 =pd.read_csv('src/multi_sim/logs/2nd_exp/robot2/TTH_2_6/trial_3/metrics/20240229040721_robot2_TTH_2_6_trial_3_metricspog.csv', sep=',', header=None)
TTH_2_6_T3_R3 =pd.read_csv('src/multi_sim/logs/2nd_exp/robot3/TTH_2_6/trial_3/metrics/20240229040722_robot3_TTH_2_6_trial_3_metricspog.csv', sep=',', header=None)

#trial 4, robot 1 2 3
TTH_2_6_T4_R1= pd.read_csv('src/multi_sim/logs/2nd_exp/robot1/TTH_2_6/trial_4/metrics/20240229042752_robot1_TTH_2_6_trial_4_metricspog.csv', sep=',', header=None)
TTH_2_6_T4_R2 =pd.read_csv('src/multi_sim/logs/2nd_exp/robot2/TTH_2_6/trial_4/metrics/20240229042752_robot2_TTH_2_6_trial_4_metricspog.csv', sep=',', header=None)
TTH_2_6_T4_R3 =pd.read_csv('src/multi_sim/logs/2nd_exp/robot3/TTH_2_6/trial_4/metrics/20240229042752_robot3_TTH_2_6_trial_4_metricspog.csv', sep=',', header=None)

#trial 5, robot 1 2 3
TTH_2_6_T5_R1= pd.read_csv('src/multi_sim/logs/2nd_exp/robot1/TTH_2_6/trial_5/metrics/20240229044822_robot1_TTH_2_6_trial_5_metricspog.csv', sep=',', header=None)
TTH_2_6_T5_R2 =pd.read_csv('src/multi_sim/logs/2nd_exp/robot2/TTH_2_6/trial_5/metrics/20240229044822_robot2_TTH_2_6_trial_5_metricspog.csv', sep=',', header=None)
TTH_2_6_T5_R3 =pd.read_csv('src/multi_sim/logs/2nd_exp/robot3/TTH_2_6/trial_5/metrics/20240229044822_robot3_TTH_2_6_trial_5_metricspog.csv', sep=',', header=None)

#trial 6, robot 1 2 3
TTH_2_6_T6_R1= pd.read_csv('src/multi_sim/logs/2nd_exp/robot1/TTH_2_6/trial_6/metrics/20240229050852_robot1_TTH_2_6_trial_6_metricspog.csv', sep=',', header=None)
TTH_2_6_T6_R2 =pd.read_csv('src/multi_sim/logs/2nd_exp/robot2/TTH_2_6/trial_6/metrics/20240229050852_robot2_TTH_2_6_trial_6_metricspog.csv', sep=',', header=None)
TTH_2_6_T6_R3 =pd.read_csv('src/multi_sim/logs/2nd_exp/robot3/TTH_2_6/trial_6/metrics/20240229050852_robot3_TTH_2_6_trial_6_metricspog.csv', sep=',', header=None)

#trial 7, robot 1 2 3
TTH_2_6_T7_R1= pd.read_csv('src/multi_sim/logs/2nd_exp/robot1/TTH_2_6/trial_7/metrics/20240229052922_robot1_TTH_2_6_trial_7_metricspog.csv', sep=',', header=None)
TTH_2_6_T7_R2 =pd.read_csv('src/multi_sim/logs/2nd_exp/robot2/TTH_2_6/trial_7/metrics/20240229052922_robot2_TTH_2_6_trial_7_metricspog.csv', sep=',', header=None)
TTH_2_6_T7_R3= pd.read_csv('src/multi_sim/logs/2nd_exp/robot3/TTH_2_6/trial_7/metrics/20240229052922_robot3_TTH_2_6_trial_7_metricspog.csv', sep=',', header=None)

#trial 8, robot 1 2 3
TTH_2_6_T8_R1= pd.read_csv('src/multi_sim/logs/2nd_exp/robot1/TTH_2_6/trial_8/metrics/20240229054952_robot1_TTH_2_6_trial_8_metricspog.csv', sep=',', header=None)
TTH_2_6_T8_R2 =pd.read_csv('src/multi_sim/logs/2nd_exp/robot2/TTH_2_6/trial_8/metrics/20240229054952_robot2_TTH_2_6_trial_8_metricspog.csv', sep=',', header=None)
TTH_2_6_T8_R3 =pd.read_csv('src/multi_sim/logs/2nd_exp/robot3/TTH_2_6/trial_8/metrics/20240229054953_robot3_TTH_2_6_trial_8_metricspog.csv', sep=',', header=None)

#trial 9, robot 1 2 3
TTH_2_6_T9_R1= pd.read_csv('src/multi_sim/logs/2nd_exp/robot1/TTH_2_6/trial_9/metrics/20240229061023_robot1_TTH_2_6_trial_9_metricspog.csv', sep=',', header=None)
TTH_2_6_T9_R2 =pd.read_csv('src/multi_sim/logs/2nd_exp/robot2/TTH_2_6/trial_9/metrics/20240229061023_robot2_TTH_2_6_trial_9_metricspog.csv', sep=',', header=None)
TTH_2_6_T9_R3 =pd.read_csv('src/multi_sim/logs/2nd_exp/robot3/TTH_2_6/trial_9/metrics/20240229061023_robot3_TTH_2_6_trial_9_metricspog.csv', sep=',', header=None)

#trial 10, robot 1 2 3
TTH_2_6_T10_R1= pd.read_csv('src/multi_sim/logs/2nd_exp/robot1/TTH_2_6/trial_10/metrics/20240229063053_robot1_TTH_2_6_trial_10_metricspog.csv', sep=',', header=None)
TTH_2_6_T10_R2 =pd.read_csv('src/multi_sim/logs/2nd_exp/robot2/TTH_2_6/trial_10/metrics/20240229063053_robot2_TTH_2_6_trial_10_metricspog.csv', sep=',', header=None)
TTH_2_6_T10_R3 =pd.read_csv('src/multi_sim/logs/2nd_exp/robot3/TTH_2_6/trial_10/metrics/20240229063053_robot3_TTH_2_6_trial_10_metricspog.csv', sep=',', header=None)

# TTH 6 10 
# trial 1, robot 1 2 3 
TTH_6_10_T1_R1 =pd.read_csv('src/multi_sim/logs/2nd_exp/robot1/TTH_6_10/trial_1/metrics/20240229101625_robot1_TTH_6_10_trial_1_metricspog.csv', sep=',', header=None) 
TTH_6_10_T1_R2 =pd.read_csv('src/multi_sim/logs/2nd_exp/robot2/TTH_6_10/trial_1/metrics/20240229101626_robot2_TTH_6_10_trial_1_metricspog.csv', sep=',', header=None) 
TTH_6_10_T1_R3 =pd.read_csv('src/multi_sim/logs/2nd_exp/robot3/TTH_6_10/trial_1/metrics/20240229101626_robot3_TTH_6_10_trial_1_metricspog.csv', sep=',', header=None)

# trial 2, robot 1 2 3
TTH_6_10_T2_R1 =pd.read_csv('src/multi_sim/logs/2nd_exp/robot1/TTH_6_10/trial_2/metrics/20240229103655_robot1_TTH_6_10_trial_2_metricspog.csv', sep=',', header=None)
TTH_6_10_T2_R2 =pd.read_csv('src/multi_sim/logs/2nd_exp/robot2/TTH_6_10/trial_2/metrics/20240229103656_robot2_TTH_6_10_trial_2_metricspog.csv', sep=',', header=None)
TTH_6_10_T2_R3 =pd.read_csv('src/multi_sim/logs/2nd_exp/robot3/TTH_6_10/trial_2/metrics/20240229103656_robot3_TTH_6_10_trial_2_metricspog.csv', sep=',', header=None)

# trial 3, robot 1 2 3
TTH_6_10_T3_R1 =pd.read_csv('src/multi_sim/logs/2nd_exp/robot1/TTH_6_10/trial_3/metrics/20240229105726_robot1_TTH_6_10_trial_3_metricspog.csv', sep=',', header=None)
TTH_6_10_T3_R2 =pd.read_csv('src/multi_sim/logs/2nd_exp/robot2/TTH_6_10/trial_3/metrics/20240229105726_robot2_TTH_6_10_trial_3_metricspog.csv', sep=',', header=None)
TTH_6_10_T3_R3 =pd.read_csv('src/multi_sim/logs/2nd_exp/robot3/TTH_6_10/trial_3/metrics/20240229105726_robot3_TTH_6_10_trial_3_metricspog.csv', sep=',', header=None)

# trial 4, robot 1 2 3
TTH_6_10_T4_R1 =pd.read_csv('src/multi_sim/logs/2nd_exp/robot1/TTH_6_10/trial_4/metrics/20240229111756_robot1_TTH_6_10_trial_4_metricspog.csv', sep=',', header=None)
TTH_6_10_T4_R2 =pd.read_csv('src/multi_sim/logs/2nd_exp/robot2/TTH_6_10/trial_4/metrics/20240229111756_robot2_TTH_6_10_trial_4_metricspog.csv', sep=',', header=None)
TTH_6_10_T4_R3 =pd.read_csv('src/multi_sim/logs/2nd_exp/robot3/TTH_6_10/trial_4/metrics/20240229111756_robot3_TTH_6_10_trial_4_metricspog.csv', sep=',', header=None)

# trial 5, robot 1 2 3
TTH_6_10_T5_R1 =pd.read_csv('src/multi_sim/logs/2nd_exp/robot1/TTH_6_10/trial_5/metrics/20240229113826_robot1_TTH_6_10_trial_5_metricspog.csv', sep=',', header=None)
TTH_6_10_T5_R2 =pd.read_csv('src/multi_sim/logs/2nd_exp/robot2/TTH_6_10/trial_5/metrics/20240229113827_robot2_TTH_6_10_trial_5_metricspog.csv', sep=',', header=None)
TTH_6_10_T5_R3 =pd.read_csv('src/multi_sim/logs/2nd_exp/robot3/TTH_6_10/trial_5/metrics/20240229113827_robot3_TTH_6_10_trial_5_metricspog.csv', sep=',', header=None)

# trial 6, robot 1 2 3
TTH_6_10_T6_R1 =pd.read_csv('src/multi_sim/logs/2nd_exp/robot1/TTH_6_10/trial_6/metrics/20240229115857_robot1_TTH_6_10_trial_6_metricspog.csv', sep=',', header=None)
TTH_6_10_T6_R2 =pd.read_csv('src/multi_sim/logs/2nd_exp/robot2/TTH_6_10/trial_6/metrics/20240229115857_robot2_TTH_6_10_trial_6_metricspog.csv', sep=',', header=None)
TTH_6_10_T6_R3 =pd.read_csv('src/multi_sim/logs/2nd_exp/robot3/TTH_6_10/trial_6/metrics/20240229115857_robot3_TTH_6_10_trial_6_metricspog.csv', sep=',', header=None)

# trial 7, robot 1 2 3
TTH_6_10_T7_R1 =pd.read_csv('src/multi_sim/logs/2nd_exp/robot1/TTH_6_10/trial_7/metrics/20240229121927_robot1_TTH_6_10_trial_7_metricspog.csv', sep=',', header=None)
TTH_6_10_T7_R2 =pd.read_csv('src/multi_sim/logs/2nd_exp/robot2/TTH_6_10/trial_7/metrics/20240229121927_robot2_TTH_6_10_trial_7_metricspog.csv', sep=',', header=None)
TTH_6_10_T7_R3 =pd.read_csv('src/multi_sim/logs/2nd_exp/robot3/TTH_6_10/trial_7/metrics/20240229121927_robot3_TTH_6_10_trial_7_metricspog.csv', sep=',', header=None)

# trial 8, robot 1 2 3
TTH_6_10_T8_R1 =pd.read_csv('src/multi_sim/logs/2nd_exp/robot1/TTH_6_10/trial_8/metrics/20240229123957_robot1_TTH_6_10_trial_8_metricspog.csv', sep=',', header=None)
TTH_6_10_T8_R2 =pd.read_csv('src/multi_sim/logs/2nd_exp/robot2/TTH_6_10/trial_8/metrics/20240229123957_robot2_TTH_6_10_trial_8_metricspog.csv', sep=',', header=None)
TTH_6_10_T8_R3 =pd.read_csv('src/multi_sim/logs/2nd_exp/robot3/TTH_6_10/trial_8/metrics/20240229123957_robot3_TTH_6_10_trial_8_metricspog.csv', sep=',', header=None)

# trial 9, robot 1 2 3
TTH_6_10_T9_R1 =pd.read_csv('src/multi_sim/logs/2nd_exp/robot1/TTH_6_10/trial_9/metrics/20240229130027_robot1_TTH_6_10_trial_9_metricspog.csv', sep=',', header=None)
TTH_6_10_T9_R2 =pd.read_csv('src/multi_sim/logs/2nd_exp/robot2/TTH_6_10/trial_9/metrics/20240229130027_robot2_TTH_6_10_trial_9_metricspog.csv', sep=',', header=None)
TTH_6_10_T9_R3 =pd.read_csv('src/multi_sim/logs/2nd_exp/robot3/TTH_6_10/trial_9/metrics/20240229130028_robot3_TTH_6_10_trial_9_metricspog.csv', sep=',', header=None)

# trial 10, robot 1 2 3
TTH_6_10_T10_R1 =pd.read_csv('src/multi_sim/logs/2nd_exp/robot1/TTH_6_10/trial_10/metrics/20240229132057_robot1_TTH_6_10_trial_10_metricspog.csv', sep=',', header=None)
TTH_6_10_T10_R2 =pd.read_csv('src/multi_sim/logs/2nd_exp/robot2/TTH_6_10/trial_10/metrics/20240229132058_robot2_TTH_6_10_trial_10_metricspog.csv', sep=',', header=None)
TTH_6_10_T10_R3 =pd.read_csv('src/multi_sim/logs/2nd_exp/robot3/TTH_6_10/trial_10/metrics/20240229132058_robot3_TTH_6_10_trial_10_metricspog.csv', sep=',', header=None)

#TTH 100 200
#trial 1, robot 1 2 3
TTH_100_200_T1_R1 =pd.read_csv('src/multi_sim/logs/2nd_exp/robot1/TTH_100_200/trial_1/metrics/20240229065123_robot1_TTH_100_200_trial_1_metricspog.csv', sep=',', header=None)
TTH_100_200_T1_R2 =pd.read_csv('src/multi_sim/logs/2nd_exp/robot2/TTH_100_200/trial_1/metrics/20240229065123_robot2_TTH_100_200_trial_1_metricspog.csv', sep=',', header=None)
TTH_100_200_T1_R3 =pd.read_csv('src/multi_sim/logs/2nd_exp/robot3/TTH_100_200/trial_1/metrics/20240229065123_robot3_TTH_100_200_trial_1_metricspog.csv', sep=',', header=None)

#trial 2, robot 1 2 3
TTH_100_200_T2_R1 =pd.read_csv('src/multi_sim/logs/2nd_exp/robot1/TTH_100_200/trial_2/metrics/20240229071153_robot1_TTH_100_200_trial_2_metricspog.csv', sep=',', header=None)
TTH_100_200_T2_R2 =pd.read_csv('src/multi_sim/logs/2nd_exp/robot2/TTH_100_200/trial_2/metrics/20240229071153_robot2_TTH_100_200_trial_2_metricspog.csv', sep=',', header=None)
TTH_100_200_T2_R3 =pd.read_csv('src/multi_sim/logs/2nd_exp/robot3/TTH_100_200/trial_2/metrics/20240229071154_robot3_TTH_100_200_trial_2_metricspog.csv', sep=',', header=None)

# trial 3, robot 1 2 3
TTH_100_200_T3_R1 =pd.read_csv('src/multi_sim/logs/2nd_exp/robot1/TTH_100_200/trial_3/metrics/20240229073224_robot1_TTH_100_200_trial_3_metricspog.csv', sep=',', header=None)
TTH_100_200_T3_R2 =pd.read_csv('src/multi_sim/logs/2nd_exp/robot2/TTH_100_200/trial_3/metrics/20240229073224_robot2_TTH_100_200_trial_3_metricspog.csv', sep=',', header=None)
TTH_100_200_T3_R3 =pd.read_csv('src/multi_sim/logs/2nd_exp/robot3/TTH_100_200/trial_3/metrics/20240229073224_robot3_TTH_100_200_trial_3_metricspog.csv', sep=',', header=None)

# trial 4, robot 1 2 3
TTH_100_200_T4_R1 =pd.read_csv('src/multi_sim/logs/2nd_exp/robot1/TTH_100_200/trial_4/metrics/20240229075254_robot1_TTH_100_200_trial_4_metricspog.csv', sep=',', header=None)
TTH_100_200_T4_R2 =pd.read_csv('src/multi_sim/logs/2nd_exp/robot2/TTH_100_200/trial_4/metrics/20240229075254_robot2_TTH_100_200_trial_4_metricspog.csv', sep=',', header=None)
TTH_100_200_T4_R3 =pd.read_csv('src/multi_sim/logs/2nd_exp/robot3/TTH_100_200/trial_4/metrics/20240229075254_robot3_TTH_100_200_trial_4_metricspog.csv', sep=',', header=None)

# trial 5, robot 1 2 3
TTH_100_200_T5_R1 =pd.read_csv('src/multi_sim/logs/2nd_exp/robot1/TTH_100_200/trial_5/metrics/20240229081324_robot1_TTH_100_200_trial_5_metricspog.csv', sep=',', header=None)
TTH_100_200_T5_R2 =pd.read_csv('src/multi_sim/logs/2nd_exp/robot2/TTH_100_200/trial_5/metrics/20240229081324_robot2_TTH_100_200_trial_5_metricspog.csv', sep=',', header=None)
TTH_100_200_T5_R3 =pd.read_csv('src/multi_sim/logs/2nd_exp/robot3/TTH_100_200/trial_5/metrics/20240229081324_robot3_TTH_100_200_trial_5_metricspog.csv', sep=',', header=None)

# trial 6, robot 1 2 3
TTH_100_200_T6_R1 =pd.read_csv('src/multi_sim/logs/2nd_exp/robot1/TTH_100_200/trial_6/metrics/20240229083354_robot1_TTH_100_200_trial_6_metricspog.csv', sep=',', header=None)
TTH_100_200_T6_R2 =pd.read_csv('src/multi_sim/logs/2nd_exp/robot2/TTH_100_200/trial_6/metrics/20240229083354_robot2_TTH_100_200_trial_6_metricspog.csv', sep=',', header=None)
TTH_100_200_T6_R3 =pd.read_csv('src/multi_sim/logs/2nd_exp/robot3/TTH_100_200/trial_6/metrics/20240229083354_robot3_TTH_100_200_trial_6_metricspog.csv', sep=',', header=None)

# trial 7, robot 1 2 3
TTH_100_200_T7_R1 =pd.read_csv('src/multi_sim/logs/2nd_exp/robot1/TTH_100_200/trial_7/metrics/20240229085424_robot1_TTH_100_200_trial_7_metricspog.csv', sep=',', header=None)
TTH_100_200_T7_R2 =pd.read_csv('src/multi_sim/logs/2nd_exp/robot2/TTH_100_200/trial_7/metrics/20240229085425_robot2_TTH_100_200_trial_7_metricspog.csv', sep=',', header=None)
TTH_100_200_T7_R3 =pd.read_csv('src/multi_sim/logs/2nd_exp/robot3/TTH_100_200/trial_7/metrics/20240229085425_robot3_TTH_100_200_trial_7_metricspog.csv', sep=',', header=None)

# trial 8, robot 1 2 3
TTH_100_200_T8_R1 =pd.read_csv('src/multi_sim/logs/2nd_exp/robot1/TTH_100_200/trial_8/metrics/20240229091455_robot1_TTH_100_200_trial_8_metricspog.csv', sep=',', header=None)
TTH_100_200_T8_R2 =pd.read_csv('src/multi_sim/logs/2nd_exp/robot2/TTH_100_200/trial_8/metrics/20240229091455_robot2_TTH_100_200_trial_8_metricspog.csv', sep=',', header=None)
TTH_100_200_T8_R3 =pd.read_csv('src/multi_sim/logs/2nd_exp/robot3/TTH_100_200/trial_8/metrics/20240229091455_robot3_TTH_100_200_trial_8_metricspog.csv', sep=',', header=None)

# trial 9, robot 1 2 3
TTH_100_200_T9_R1 =pd.read_csv('src/multi_sim/logs/2nd_exp/robot1/TTH_100_200/trial_9/metrics/20240229093525_robot1_TTH_100_200_trial_9_metricspog.csv', sep=',', header=None)
TTH_100_200_T9_R2 =pd.read_csv('src/multi_sim/logs/2nd_exp/robot2/TTH_100_200/trial_9/metrics/20240229093525_robot2_TTH_100_200_trial_9_metricspog.csv', sep=',', header=None)
TTH_100_200_T9_R3 =pd.read_csv('src/multi_sim/logs/2nd_exp/robot3/TTH_100_200/trial_9/metrics/20240229093525_robot3_TTH_100_200_trial_9_metricspog.csv', sep=',', header=None)

# trial 10, robot 1 2 3
TTH_100_200_T10_R1 =pd.read_csv('src/multi_sim/logs/2nd_exp/robot1/TTH_100_200/trial_10/metrics/20240229095555_robot1_TTH_100_200_trial_10_metricspog.csv', sep=',', header=None)
TTH_100_200_T10_R2 =pd.read_csv('src/multi_sim/logs/2nd_exp/robot2/TTH_100_200/trial_10/metrics/20240229095555_robot2_TTH_100_200_trial_10_metricspog.csv', sep=',', header=None)
TTH_100_200_T10_R3 =pd.read_csv('src/multi_sim/logs/2nd_exp/robot3/TTH_100_200/trial_10/metrics/20240229095555_robot3_TTH_100_200_trial_10_metricspog.csv', sep=',', header=None)

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

# Fixing Trials 5 to 10 for condition 'tth_2_6'
TTH_2_6_T5_R2.insert(0, 'condition', 'tth_2_6')
TTH_2_6_T5_R1.insert(0, 'condition', 'tth_2_6')
TTH_2_6_T5_R3.insert(0, 'condition', 'tth_2_6')
TTH_2_6_T5_R2.insert(1, 'trial', '5')
TTH_2_6_T5_R1.insert(1, 'trial', '5')
TTH_2_6_T5_R3.insert(1, 'trial', '5')
TTH_2_6_T5_R1.insert(2, 'robot', '1')
TTH_2_6_T5_R2.insert(2, 'robot', '2')
TTH_2_6_T5_R3.insert(2, 'robot', '3')

TTH_2_6_T6_R2.insert(0, 'condition', 'tth_2_6')
TTH_2_6_T6_R1.insert(0, 'condition', 'tth_2_6')
TTH_2_6_T6_R3.insert(0, 'condition', 'tth_2_6')
TTH_2_6_T6_R2.insert(1, 'trial', '6')
TTH_2_6_T6_R1.insert(1, 'trial', '6')
TTH_2_6_T6_R3.insert(1, 'trial', '6')
TTH_2_6_T6_R1.insert(2, 'robot', '1')
TTH_2_6_T6_R2.insert(2, 'robot', '2')
TTH_2_6_T6_R3.insert(2, 'robot', '3')

TTH_2_6_T7_R2.insert(0, 'condition', 'tth_2_6')
TTH_2_6_T7_R1.insert(0, 'condition', 'tth_2_6')
TTH_2_6_T7_R3.insert(0, 'condition', 'tth_2_6')
TTH_2_6_T7_R2.insert(1, 'trial', '7')
TTH_2_6_T7_R1.insert(1, 'trial', '7')
TTH_2_6_T7_R3.insert(1, 'trial', '7')
TTH_2_6_T7_R1.insert(2, 'robot', '1')
TTH_2_6_T7_R2.insert(2, 'robot', '2')
TTH_2_6_T7_R3.insert(2, 'robot', '3')

TTH_2_6_T8_R2.insert(0, 'condition', 'tth_2_6')
TTH_2_6_T8_R1.insert(0, 'condition', 'tth_2_6')
TTH_2_6_T8_R3.insert(0, 'condition', 'tth_2_6')
TTH_2_6_T8_R2.insert(1, 'trial', '8')
TTH_2_6_T8_R1.insert(1, 'trial', '8')
TTH_2_6_T8_R3.insert(1, 'trial', '8')
TTH_2_6_T8_R1.insert(2, 'robot', '1')
TTH_2_6_T8_R2.insert(2, 'robot', '2')
TTH_2_6_T8_R3.insert(2, 'robot', '3')

TTH_2_6_T9_R2.insert(0, 'condition', 'tth_2_6')
TTH_2_6_T9_R1.insert(0, 'condition', 'tth_2_6')
TTH_2_6_T9_R3.insert(0, 'condition', 'tth_2_6')
TTH_2_6_T9_R2.insert(1, 'trial', '9')
TTH_2_6_T9_R1.insert(1, 'trial', '9')
TTH_2_6_T9_R3.insert(1, 'trial', '9')
TTH_2_6_T9_R1.insert(2, 'robot', '1')
TTH_2_6_T9_R2.insert(2, 'robot', '2')
TTH_2_6_T9_R3.insert(2, 'robot', '3')

TTH_2_6_T10_R2.insert(0, 'condition', 'tth_2_6')
TTH_2_6_T10_R1.insert(0, 'condition', 'tth_2_6')
TTH_2_6_T10_R3.insert(0, 'condition', 'tth_2_6')
TTH_2_6_T10_R2.insert(1, 'trial', '10')
TTH_2_6_T10_R1.insert(1, 'trial', '10')
TTH_2_6_T10_R3.insert(1, 'trial', '10')
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

# Fixing Trials 5 to 10 for condition 'tth_6_10'
TTH_6_10_T5_R2.insert(0, 'condition', 'tth_6_10')
TTH_6_10_T5_R1.insert(0, 'condition', 'tth_6_10')
TTH_6_10_T5_R3.insert(0, 'condition', 'tth_6_10')
TTH_6_10_T5_R2.insert(1, 'trial', '5')
TTH_6_10_T5_R1.insert(1, 'trial', '5')
TTH_6_10_T5_R3.insert(1, 'trial', '5')
TTH_6_10_T5_R1.insert(2, 'robot', '1')
TTH_6_10_T5_R2.insert(2, 'robot', '2')
TTH_6_10_T5_R3.insert(2, 'robot', '3')

TTH_6_10_T6_R2.insert(0, 'condition', 'tth_6_10')
TTH_6_10_T6_R1.insert(0, 'condition', 'tth_6_10')
TTH_6_10_T6_R3.insert(0, 'condition', 'tth_6_10')
TTH_6_10_T6_R2.insert(1, 'trial', '6')
TTH_6_10_T6_R1.insert(1, 'trial', '6')
TTH_6_10_T6_R3.insert(1, 'trial', '6')
TTH_6_10_T6_R1.insert(2, 'robot', '1')
TTH_6_10_T6_R2.insert(2, 'robot', '2')
TTH_6_10_T6_R3.insert(2, 'robot', '3')

TTH_6_10_T7_R2.insert(0, 'condition', 'tth_6_10')
TTH_6_10_T7_R1.insert(0, 'condition', 'tth_6_10')
TTH_6_10_T7_R3.insert(0, 'condition', 'tth_6_10')
TTH_6_10_T7_R2.insert(1, 'trial', '7')
TTH_6_10_T7_R1.insert(1, 'trial', '7')
TTH_6_10_T7_R3.insert(1, 'trial', '7')
TTH_6_10_T7_R1.insert(2, 'robot', '1')
TTH_6_10_T7_R2.insert(2, 'robot', '2')
TTH_6_10_T7_R3.insert(2, 'robot', '3')

TTH_6_10_T8_R2.insert(0, 'condition', 'tth_6_10')
TTH_6_10_T8_R1.insert(0, 'condition', 'tth_6_10')
TTH_6_10_T8_R3.insert(0, 'condition', 'tth_6_10')
TTH_6_10_T8_R2.insert(1, 'trial', '8')
TTH_6_10_T8_R1.insert(1, 'trial', '8')
TTH_6_10_T8_R3.insert(1, 'trial', '8')
TTH_6_10_T8_R1.insert(2, 'robot', '1')
TTH_6_10_T8_R2.insert(2, 'robot', '2')
TTH_6_10_T8_R3.insert(2, 'robot', '3')

TTH_6_10_T9_R2.insert(0, 'condition', 'tth_6_10')
TTH_6_10_T9_R1.insert(0, 'condition', 'tth_6_10')
TTH_6_10_T9_R3.insert(0, 'condition', 'tth_6_10')
TTH_6_10_T9_R2.insert(1, 'trial', '9')
TTH_6_10_T9_R1.insert(1, 'trial', '9')
TTH_6_10_T9_R3.insert(1, 'trial', '9')
TTH_6_10_T9_R1.insert(2, 'robot', '1')
TTH_6_10_T9_R2.insert(2, 'robot', '2')
TTH_6_10_T9_R3.insert(2, 'robot', '3')

TTH_6_10_T10_R2.insert(0, 'condition', 'tth_6_10')
TTH_6_10_T10_R1.insert(0, 'condition', 'tth_6_10')
TTH_6_10_T10_R3.insert(0, 'condition', 'tth_6_10')
TTH_6_10_T10_R2.insert(1, 'trial', '10')
TTH_6_10_T10_R1.insert(1, 'trial', '10')
TTH_6_10_T10_R3.insert(1, 'trial', '10')
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

# Fixing Trials 5 to 10 for condition 'tth_100_200'
TTH_100_200_T5_R2.insert(0, 'condition', 'tth_100_200')
TTH_100_200_T5_R1.insert(0, 'condition', 'tth_100_200')
TTH_100_200_T5_R3.insert(0, 'condition', 'tth_100_200')
TTH_100_200_T5_R2.insert(1, 'trial', '5')
TTH_100_200_T5_R1.insert(1, 'trial', '5')
TTH_100_200_T5_R3.insert(1, 'trial', '5')
TTH_100_200_T5_R1.insert(2, 'robot', '1')
TTH_100_200_T5_R2.insert(2, 'robot', '2')
TTH_100_200_T5_R3.insert(2, 'robot', '3')

TTH_100_200_T6_R2.insert(0, 'condition', 'tth_100_200')
TTH_100_200_T6_R1.insert(0, 'condition', 'tth_100_200')
TTH_100_200_T6_R3.insert(0, 'condition', 'tth_100_200')
TTH_100_200_T6_R2.insert(1, 'trial', '6')
TTH_100_200_T6_R1.insert(1, 'trial', '6')
TTH_100_200_T6_R3.insert(1, 'trial', '6')
TTH_100_200_T6_R1.insert(2, 'robot', '1')
TTH_100_200_T6_R2.insert(2, 'robot', '2')
TTH_100_200_T6_R3.insert(2, 'robot', '3')

TTH_100_200_T7_R2.insert(0, 'condition', 'tth_100_200')
TTH_100_200_T7_R1.insert(0, 'condition', 'tth_100_200')
TTH_100_200_T7_R3.insert(0, 'condition', 'tth_100_200')
TTH_100_200_T7_R2.insert(1, 'trial', '7')
TTH_100_200_T7_R1.insert(1, 'trial', '7')
TTH_100_200_T7_R3.insert(1, 'trial', '7')
TTH_100_200_T7_R1.insert(2, 'robot', '1')
TTH_100_200_T7_R2.insert(2, 'robot', '2')
TTH_100_200_T7_R3.insert(2, 'robot', '3')

TTH_100_200_T8_R2.insert(0, 'condition', 'tth_100_200')
TTH_100_200_T8_R1.insert(0, 'condition', 'tth_100_200')
TTH_100_200_T8_R3.insert(0, 'condition', 'tth_100_200')
TTH_100_200_T8_R2.insert(1, 'trial', '8')
TTH_100_200_T8_R1.insert(1, 'trial', '8')
TTH_100_200_T8_R3.insert(1, 'trial', '8')
TTH_100_200_T8_R1.insert(2, 'robot', '1')
TTH_100_200_T8_R2.insert(2, 'robot', '2')
TTH_100_200_T8_R3.insert(2, 'robot', '3')

TTH_100_200_T9_R2.insert(0, 'condition', 'tth_100_200')
TTH_100_200_T9_R1.insert(0, 'condition', 'tth_100_200')
TTH_100_200_T9_R3.insert(0, 'condition', 'tth_100_200')
TTH_100_200_T9_R2.insert(1, 'trial', '9')
TTH_100_200_T9_R1.insert(1, 'trial', '9')
TTH_100_200_T9_R3.insert(1, 'trial', '9')
TTH_100_200_T9_R1.insert(2, 'robot', '1')
TTH_100_200_T9_R2.insert(2, 'robot', '2')
TTH_100_200_T9_R3.insert(2, 'robot', '3')

TTH_100_200_T10_R2.insert(0, 'condition', 'tth_100_200')
TTH_100_200_T10_R1.insert(0, 'condition', 'tth_100_200')
TTH_100_200_T10_R3.insert(0, 'condition', 'tth_100_200')
TTH_100_200_T10_R2.insert(1, 'trial', '10')
TTH_100_200_T10_R1.insert(1, 'trial', '10')
TTH_100_200_T10_R3.insert(1, 'trial', '10')
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

# Fixing Trials 5 to 10 for condition 'NP'
NP_T5_R2.insert(0, 'condition', 'NP')
NP_T5_R1.insert(0, 'condition', 'NP')
NP_T5_R3.insert(0, 'condition', 'NP')
NP_T5_R2.insert(1, 'trial', '5')
NP_T5_R1.insert(1, 'trial', '5')
NP_T5_R3.insert(1, 'trial', '5')
NP_T5_R1.insert(2, 'robot', '1')
NP_T5_R2.insert(2, 'robot', '2')
NP_T5_R3.insert(2, 'robot', '3')

NP_T6_R2.insert(0, 'condition', 'NP')
NP_T6_R1.insert(0, 'condition', 'NP')
NP_T6_R3.insert(0, 'condition', 'NP')
NP_T6_R2.insert(1, 'trial', '6')
NP_T6_R1.insert(1, 'trial', '6')
NP_T6_R3.insert(1, 'trial', '6')
NP_T6_R1.insert(2, 'robot', '1')
NP_T6_R2.insert(2, 'robot', '2')
NP_T6_R3.insert(2, 'robot', '3')

NP_T7_R2.insert(0, 'condition', 'NP')
NP_T7_R1.insert(0, 'condition', 'NP')
NP_T7_R3.insert(0, 'condition', 'NP')
NP_T7_R2.insert(1, 'trial', '7')
NP_T7_R1.insert(1, 'trial', '7')
NP_T7_R3.insert(1, 'trial', '7')
NP_T7_R1.insert(2, 'robot', '1')
NP_T7_R2.insert(2, 'robot', '2')
NP_T7_R3.insert(2, 'robot', '3')

NP_T8_R2.insert(0, 'condition', 'NP')
NP_T8_R1.insert(0, 'condition', 'NP')
NP_T8_R3.insert(0, 'condition', 'NP')
NP_T8_R2.insert(1, 'trial', '8')
NP_T8_R1.insert(1, 'trial', '8')
NP_T8_R3.insert(1, 'trial', '8')
NP_T8_R1.insert(2, 'robot', '1')
NP_T8_R2.insert(2, 'robot', '2')
NP_T8_R3.insert(2, 'robot', '3')

NP_T9_R2.insert(0, 'condition', 'NP')
NP_T9_R1.insert(0, 'condition', 'NP')
NP_T9_R3.insert(0, 'condition', 'NP')
NP_T9_R2.insert(1, 'trial', '9')
NP_T9_R1.insert(1, 'trial', '9')
NP_T9_R3.insert(1, 'trial', '9')
NP_T9_R1.insert(2, 'robot', '1')
NP_T9_R2.insert(2, 'robot', '2')
NP_T9_R3.insert(2, 'robot', '3')

NP_T10_R2.insert(0, 'condition', 'NP')
NP_T10_R1.insert(0, 'condition', 'NP')
NP_T10_R3.insert(0, 'condition', 'NP')
NP_T10_R2.insert(1, 'trial', '10')
NP_T10_R1.insert(1, 'trial', '10')
NP_T10_R3.insert(1, 'trial', '10')
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
lplot.fig.suptitle('Activity Level 6 / 10 - Increase at 600(s)', fontsize=16)

# Set y-axis limits
plt.ylim(y_limits)
plt.axhline(y=50, linestyle='--', linewidth=0.8, c='hotpink')

plt.xlabel('Time (s)')
plt.ylabel('Activity Level')


plt.savefig('src/multi_sim/scripts/results/graphs/TTH2_6_ALL.png')
plt.savefig('src/multi_sim/scripts/results/graphs/TTH2_6_ALL.pdf')
plt.show()




# Results 6 10
subset = all_df[ ( all_df['condition'] == 'tth_6_10' ) ]
#print( subset )


# Set y-axis limits
y_limits = (0, 110)

# having trouble with hue colours
colours = dict(zip(subset['robot'].unique(), sns.color_palette(n_colors=len(subset['robot'].unique()))))

lplot = sns.relplot(data=subset, x='time', y='activation', kind='line', hue='robot', palette=colours, height=5, aspect=2, errorbar=('ci',95) )
lplot.fig.suptitle('Activity Level 6 / 10 - Increase at 600(s)', fontsize=16)

# Set y-axis limits
plt.ylim(y_limits)
plt.axhline(y=50, linestyle='--', linewidth=0.8, c='hotpink')

plt.xlabel('Time (s)')
plt.ylabel('Activity Level')

plt.savefig('src/multi_sim/scripts/results/graphs/TTH6_10_ALL.png')
plt.savefig('src/multi_sim/scripts/results/graphs/TTH6_10_ALL.pdf')
plt.show()


# Result 100 200

subset = all_df[ ( all_df['condition'] == 'tth_100_200' ) ]
#print( subset )

# Set y-axis limits
y_limits = (0, 110)

# having trouble with hue colours
colours = dict(zip(subset['robot'].unique(), sns.color_palette(n_colors=len(subset['robot'].unique()))))

lplot = sns.relplot(data=subset, x='time', y='activation', kind='line', hue='robot', palette=colours, height=5, aspect=2, errorbar=('ci',95) )
lplot.fig.suptitle('Activity Level 100 / 200 - Increase at 600(s)', fontsize=16)

# Set y-axis limits
plt.ylim(y_limits)
plt.axhline(y=50, linestyle='--', linewidth=0.8, c='hotpink')


plt.xlabel('Time (s)')
plt.ylabel('Activity Level')

plt.savefig('src/multi_sim/scripts/results/graphs/TTH100_200_ALL.png')
plt.savefig('src/multi_sim/scripts/results/graphs/TTH100_200_ALL.pdf')
plt.show()


# Results all compared 
subset = all_df[ ( all_df['time'] < max_time ) ]
subset = all_df[ ( all_df['condition'] != 'NP' ) ]
#print( subset )



# having trouble with hue colours
colours = dict(zip(subset['condition'].unique(), sns.color_palette(n_colors=len(subset['condition'].unique()))))

lplot = sns.relplot(data=subset, x='time', y='activation', kind='line', hue='condition', palette=colours, height=5, aspect=2, errorbar=('ci',95) )
lplot.fig.suptitle('Activity Level Over Time - Increase at 600(s)', fontsize=16)

plt.axhline(y=50, linestyle='--', linewidth=0.8, c='hotpink')


plt.xlabel('Time (s)')
plt.ylabel('Activity Level')

plt.savefig('src/multi_sim/scripts/results/graphs/TTH_ALL.png')

plt.savefig('src/multi_sim/scripts/results/graphs/TTH_ALL.pdf')
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
bplot.set_title('Final Tag Count - Increase at 600(s)')


plt.savefig('src/multi_sim/scripts/results/graphs/Total_tags.pdf')
plt.savefig('src/multi_sim/scripts/results/graphs/Total_tags.png')
plt.show()
