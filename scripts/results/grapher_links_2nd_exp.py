
# We will use the following Python libraries:
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
import os


# Path to where the results are hosted online
# This loads the data into a Pandas dataframe
# You have seperate files for all trials and all
# robots, so these have to be loaded in individually

min_time = 0
max_time = 1200

conditions = ['NP', 'TTH_2_6', 'TTH_6_10', 'TTH_100_200']
trials = 10
robots = 3


# Set these to the experiment params
experiment = '2nd_exp'
# "3rd_exp_decrease_at_600"
title_extension = "- Increase at 600(s)- Sim"

graph_path = f'src/multi_sim/scripts/results/graphs/{experiment}'


if not os.path.exists(f"{graph_path}/pngs"):
    os.makedirs(f"{graph_path}/pngs")

if not os.path.exists(f"{graph_path}/pdfs"):
    os.makedirs(f"{graph_path}/pdfs")


# Here we loop through the paths to find the csv containing the results
data = {}
for cond in conditions:
    data[cond] = {}
    for t in range(1, trials+1):
        data[cond][f"T{t}"] = {}
        for r in range(1, robots+1):
            path = f'src/multi_sim/logs/{experiment}/robot{r}/{cond}/trial_{t}/metrics/'
            csv_files = os.listdir(path)
            csv_file = [f for f in csv_files if f.endswith('metricspog.csv')][0]
            df = pd.read_csv(os.path.join(path, csv_file), header=None)
            data[cond][f"T{t}"][f"R{r}"] = df


# Here we create variables for each trial/robot/condition
for cond in conditions:
  for t in range(1, trials+1):
    for r in range(1, robots+1):
      
      # Construct variable name  
      var_name = f"{cond}_T{t}_R{r}"
      
      # Get DataFrame
      df = data[cond][f"T{t}"][f"R{r}"]
      
      # Assign to variable
      exec(f"{var_name} = df") 

# Set column names       
columns = ['time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
for cond in conditions:
  for t in range(1, trials+1):
    for r in range(1, robots+1):
        
      df = data[cond][f"T{t}"][f"R{r}"]  
      df.columns = columns





# # First job is to label columns
# TTH_2_6_T1_R1.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
# TTH_2_6_T1_R2.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
# TTH_2_6_T1_R3.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']

# TTH_2_6_T2_R1.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
# TTH_2_6_T2_R2.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
# TTH_2_6_T2_R3.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']

# TTH_2_6_T3_R1.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
# TTH_2_6_T3_R2.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
# TTH_2_6_T3_R3.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']

# TTH_2_6_T4_R1.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
# TTH_2_6_T4_R2.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
# TTH_2_6_T4_R3.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']

# TTH_2_6_T5_R1.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
# TTH_2_6_T5_R2.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
# TTH_2_6_T5_R3.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']

# TTH_2_6_T6_R1.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
# TTH_2_6_T6_R2.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
# TTH_2_6_T6_R3.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']

# TTH_2_6_T7_R1.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
# TTH_2_6_T7_R2.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
# TTH_2_6_T7_R3.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']

# TTH_2_6_T8_R1.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
# TTH_2_6_T8_R2.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
# TTH_2_6_T8_R3.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']

# TTH_2_6_T9_R1.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
# TTH_2_6_T9_R2.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
# TTH_2_6_T9_R3.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']

# TTH_2_6_T10_R1.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
# TTH_2_6_T10_R2.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
# TTH_2_6_T10_R3.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']

# TTH_6_10_T1_R1.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
# TTH_6_10_T1_R2.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
# TTH_6_10_T1_R3.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']

# TTH_6_10_T2_R1.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
# TTH_6_10_T2_R2.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
# TTH_6_10_T2_R3.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']

# TTH_6_10_T3_R1.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
# TTH_6_10_T3_R2.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
# TTH_6_10_T3_R3.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']

# TTH_6_10_T4_R1.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
# TTH_6_10_T4_R2.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
# TTH_6_10_T4_R3.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']

# TTH_6_10_T5_R1.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
# TTH_6_10_T5_R2.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
# TTH_6_10_T5_R3.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']

# TTH_6_10_T6_R1.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
# TTH_6_10_T6_R2.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
# TTH_6_10_T6_R3.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']

# TTH_6_10_T7_R1.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
# TTH_6_10_T7_R2.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
# TTH_6_10_T7_R3.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']

# TTH_6_10_T8_R1.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
# TTH_6_10_T8_R2.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
# TTH_6_10_T8_R3.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']

# TTH_6_10_T9_R1.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
# TTH_6_10_T9_R2.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
# TTH_6_10_T9_R3.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']

# TTH_6_10_T10_R1.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
# TTH_6_10_T10_R2.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
# TTH_6_10_T10_R3.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']

# TTH_100_200_T1_R1.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
# TTH_100_200_T1_R2.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
# TTH_100_200_T1_R3.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']

# TTH_100_200_T2_R1.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
# TTH_100_200_T2_R2.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
# TTH_100_200_T2_R3.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']

# TTH_100_200_T3_R1.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
# TTH_100_200_T3_R2.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
# TTH_100_200_T3_R3.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']

# TTH_100_200_T4_R1.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
# TTH_100_200_T4_R2.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
# TTH_100_200_T4_R3.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']

# TTH_100_200_T5_R1.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
# TTH_100_200_T5_R2.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
# TTH_100_200_T5_R3.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']

# TTH_100_200_T6_R1.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
# TTH_100_200_T6_R2.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
# TTH_100_200_T6_R3.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']

# TTH_100_200_T7_R1.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
# TTH_100_200_T7_R2.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
# TTH_100_200_T7_R3.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']

# TTH_100_200_T8_R1.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
# TTH_100_200_T8_R2.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
# TTH_100_200_T8_R3.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']

# TTH_100_200_T9_R1.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
# TTH_100_200_T9_R2.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
# TTH_100_200_T9_R3.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']

# TTH_100_200_T10_R1.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
# TTH_100_200_T10_R2.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
# TTH_100_200_T10_R3.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']

# NP_T1_R1.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
# NP_T1_R2.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
# NP_T1_R3.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']

# NP_T2_R1.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
# NP_T2_R2.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
# NP_T2_R3.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']

# NP_T3_R1.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
# NP_T3_R2.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
# NP_T3_R3.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']

# NP_T4_R1.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
# NP_T4_R2.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
# NP_T4_R3.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']

# NP_T5_R1.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
# NP_T5_R2.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
# NP_T5_R3.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']

# NP_T6_R1.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
# NP_T6_R2.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
# NP_T6_R3.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']

# NP_T7_R1.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
# NP_T7_R2.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
# NP_T7_R3.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']

# NP_T8_R1.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
# NP_T8_R2.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
# NP_T8_R3.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']

# NP_T9_R1.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
# NP_T9_R2.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
# NP_T9_R3.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']

# NP_T10_R1.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
# NP_T10_R2.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']
# NP_T10_R3.columns = [ 'time', 'state', 'u_rand_num', 'activation', 'cumul_tags']



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
# print( "Oops, number of NaN's: ", all_df.isnull().sum().sum() )


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
lplot.fig.suptitle(f'Activity Level {conditions[2]} {title_extension}', fontsize=16)

# Set y-axis limits
plt.ylim(y_limits)
plt.axhline(y=50, linestyle='--', linewidth=0.8, c='hotpink')

plt.xlabel('Time (s)')
plt.ylabel('Activity Level')


plt.savefig(f'{graph_path}/pngs/{conditions[1]}_AL.png')
plt.savefig(f'{graph_path}/pdfs/{conditions[1]}_AL.pdf')
plt.close()




# Results 6 10
subset = all_df[ ( all_df['condition'] == 'tth_6_10' ) ]
#print( subset )


# Set y-axis limits
y_limits = (0, 110)

# having trouble with hue colours
colours = dict(zip(subset['robot'].unique(), sns.color_palette(n_colors=len(subset['robot'].unique()))))

lplot = sns.relplot(data=subset, x='time', y='activation', kind='line', hue='robot', palette=colours, height=5, aspect=2, errorbar=('ci',95) )
lplot.fig.suptitle('Activity Level {conditions[1]} {title_extension}', fontsize=16)

# Set y-axis limits
plt.ylim(y_limits)
plt.axhline(y=50, linestyle='--', linewidth=0.8, c='hotpink')

plt.xlabel('Time (s)')
plt.ylabel('Activity Level')

plt.savefig(f'{graph_path}/pngs/{conditions[2]}_AL.png')
plt.savefig(f'{graph_path}/pdfs/{conditions[2]}_AL.pdf')
plt.close()


# Result 100 200

subset = all_df[ ( all_df['condition'] == 'tth_100_200' ) ]
#print( subset )

# Set y-axis limits
y_limits = (0, 110)

# having trouble with hue colours
colours = dict(zip(subset['robot'].unique(), sns.color_palette(n_colors=len(subset['robot'].unique()))))

lplot = sns.relplot(data=subset, x='time', y='activation', kind='line', hue='robot', palette=colours, height=5, aspect=2, errorbar=('ci',95) )
lplot.fig.suptitle(f'Activity Level {conditions[3]} {title_extension}', fontsize=16)

# Set y-axis limits
plt.ylim(y_limits)
plt.axhline(y=50, linestyle='--', linewidth=0.8, c='hotpink')


plt.xlabel('Time (s)')
plt.ylabel('Activity Level')

plt.savefig(f'{graph_path}/pngs/{conditions[3]}_AL.png')
plt.savefig(f'{graph_path}/pdfs/{conditions[3]}_AL.pdf')
plt.close()


# Results all compared 
subset = all_df[ ( all_df['time'] < max_time ) ]
subset = all_df[ ( all_df['condition'] != 'NP' ) ]
#print( subset )



# having trouble with hue colours
colours = dict(zip(subset['condition'].unique(), sns.color_palette(n_colors=len(subset['condition'].unique()))))

lplot = sns.relplot(data=subset, x='time', y='activation', kind='line', hue='condition', palette=colours, height=5, aspect=2, errorbar=('ci',95) )
lplot.fig.suptitle(f'Activity Level Over Time {title_extension}', fontsize=16)

plt.axhline(y=50, linestyle='--', linewidth=0.8, c='hotpink')


plt.xlabel('Time (s)')
plt.ylabel('Activity Level')

plt.savefig(f'{graph_path}/pngs/TTH_ALL_AL.png')
plt.savefig(f'{graph_path}/pdfs/TTH_ALL._AL.pdf')
plt.close()

# total tags all conditions all trials



# Fetch the final tag count for each trial, for each scenario
subset = all_df[ ( all_df['time'] < max_time ) ]
subset = subset[ ( subset['condition'] == 'tth_2_6' ) ]
tth_2_6_tags = subset.groupby(['trial'])['cumul_tags'].max()

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
bplot.set_title(f'Final Tag Count {title_extension}')

plt.savefig(f'{graph_path}/pngs/Tags_over_time.png')
plt.savefig(f'{graph_path}/pdfs/Tags_over_time.pdf')
plt.close()
