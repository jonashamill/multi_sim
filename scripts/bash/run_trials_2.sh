#!/bin/bash

trialDuration=2400
noTrials=10
experiment="10th_exp_changing_env"


for i in $(seq 1 $noTrials);
do

    echo $i


    roslaunch multi_sim 1cs_sim.launch &
    
    pid=$!

    sleep 10

    rosparam set use_plasticity false 
    rosparam set trialNumber $i
    rosparam set neo_threshold_init 0


    sleep $trialDuration

    kill $pid

    sleep 20

done

for i in $(seq 1 $noTrials);
do

    echo $i


    roslaunch multi_sim 1cs_sim.launch &
    
    pid=$!

    sleep 10

    rosparam set use_plasticity false 
    rosparam set trialNumber $i
    rosparam set neo_threshold_init 100

    sleep $trialDuration

    kill $pid

    sleep 20

done


for i in $(seq 1 $noTrials);
do

    echo $i


    roslaunch multi_sim 1cs_sim.launch &
    
    pid=$!

    sleep 10

    rosparam set use_plasticity true 
    rosparam set trialNumber $i
    rosparam set neo_threshold_init 50


    sleep $trialDuration

    kill $pid

    sleep 20

done


# for i in $(seq 1 $noTrials);
# do

#     echo $i


#     roslaunch multi_sim 1cs_sim.launch &
    
#     pid=$!

#     sleep 10

#     rosparam set usePlasticity true 
#     rosparam set trialNumber $i
#     rosparam set timeThresholdLow 6
#     rosparam set timeThresholdHigh 10


#     sleep $trialDuration

#     kill $pid

#     sleep 20

# done

# for i in $(seq 1 $noTrials);
# do

#     echo $i


#     roslaunch multi_sim 1cs_sim.launch &
    
#     pid=$!

#     sleep 10

#     rosparam set usePlasticity true 
#     rosparam set trialNumber $i
#     rosparam set timeThresholdLow 1
#     rosparam set timeThresholdHigh 1


#     sleep $trialDuration

#     kill $pid

#     sleep 20

# done


mkdir -p ../logs_n_results/logs/$experiment

mv ../../logs/robot1 ../../../logs_n_results/logs/$experiment

mv ../../logs/robot2 ../../../logs_n_results/logs/$experiment

mv ../../logs/robot3 ../../../logs_n_results/logs/$experiment

cd ../../../logs_n_results

git add *

git commit -m "adding logs from $experiment trials"

git push


# for i in $(seq 1 $noTrials);
# do

#     echo $i


#     roslaunch multi_sim 1cs_sim.launch &
    
#     pid=$!

#     sleep 10

#     rosparam set usePlasticity true 
#     rosparam set trialNumber $i
#     rosparam set timeThresholdLow: 5
#     rosparam set timeThresholdHigh: 6


#     sleep $trialDuration

#     kill $pid

#     sleep 20

# done