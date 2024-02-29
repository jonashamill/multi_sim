#!/bin/bash

trialDuration=1200
noTrials=10

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

mkdir ../../logs/2nd_exp

mv ../../logs/robot1 ../../logs/2nd_exp

mv ../../logs/robot2 .../../logs/2nd_exp

mv ../../logs/robot2 .../../logs/2nd_exp

git add ../../logs/2nd_exp/*

git commit -m "adding logs from trials"

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