#!/bin/bash

trialDuration=1200
noTrials=10
experiment="6th_exp_1_tag_buffer_high_tags"


for i in $(seq 1 $noTrials);
do

    echo $i


    roslaunch multi_sim 1cs_sim.launch &
    
    pid=$!

    sleep 10

    rosparam set usePlasticity false 
    rosparam set trialNumber $i
    rosparam set timeThresholdLow 1
    rosparam set timeThresholdHigh 1


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

    rosparam set usePlasticity true 
    rosparam set trialNumber $i 
    rosparam set timeThresholdLow 2
    rosparam set timeThresholdHigh 6

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

    rosparam set usePlasticity true 
    rosparam set trialNumber $i
    rosparam set timeThresholdLow 100
    rosparam set timeThresholdHigh 200


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

    rosparam set usePlasticity true 
    rosparam set trialNumber $i
    rosparam set timeThresholdLow 6
    rosparam set timeThresholdHigh 10


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

    rosparam set usePlasticity true 
    rosparam set trialNumber $i
    rosparam set timeThresholdLow 1
    rosparam set timeThresholdHigh 1


    sleep $trialDuration

    kill $pid

    sleep 20

done


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