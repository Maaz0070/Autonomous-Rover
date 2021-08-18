# Rover

This is a lidar-based self-driving rover which autonomously drives to a specified object.


## User Stories

The following functionality is completed:

- [x] Multiple .world files (simulator environments) can be launched in Husky Gazebo Simulator. 
- [x] Rover can subscribe to node of laser scan values and accurately determine angle to drive at. 
- [x] Rover is able to autonomously navigate to specified object. 

The following **additional** features are implemented:

- [x] Teleop twist Keyboard is implemented (C++ file) to manually take control of Rover in situations.
- [x] Subscribers and Publishers are implemented (Python files) to read data from rover such as laser scan values, distance from object, speed, etc.

##Video Walkthrough of basic features:

- ![Sample Gif](https://i.imgur.com/7T2Aa2a.gif)
- +<img src="/art/sample.gif?raw=true" width="200px">

<img src='https://i.imgur.com/7T2Aa2a.gif' title='Video Walkthriough' width='' alt='Basic features' />

- [x] Here the Rover locates the pillar and autonomously sets the speed and direction to reach the pillar while avoiding obstacles
- [x] Terminal on bottom right is running a ROS node Python file which is reading all the sensor data of the rover in real time

##ROS Master, Publishers, Subscribers overview

Here's a simple diagram showing the general concept of Publishers and Subscribers:
<img src='https://www.researchgate.net/publication/323520311/figure/fig1/AS:599727376695296@1519997557097/Establishing-connections-through-the-ROS-Topic-paradigm-Derivative-of-Establishing-a.png' title='ROS Master' width='' alt='ROS overview' />

Overview:
- [ ] "Node" is the ROS term for an executable that is connected to the ROS network
- [ ] Topics are named buses over which nodes exchange messages
- [ ] A Publisher puts the messages of some standard Message Type to a particular Topic
- [ ] Subscriber subscribes to the Topic so that it receives the messages whenever any message is published to the Topic
