# Simulation for multi-robot system in gazebo using leo rovers

Depends on the leo_common package available from leorover's github
[master]: https://github.com/LeoRover/leo_common/tree/master



Start sim by launching 1cs_sim.launch

You can then launch the experiment by launching start_exp.launch

This will send the robots on a patrol route using move_base with an FSM

You can change the routes of the individual robots in patparms.yaml


If you want additional robots, add them in launch_gazebo.launch, making sure to set unique init positions, robot_ns and model name for each. 

You must also update start_exp.launch and patparams.yaml in the same manner 