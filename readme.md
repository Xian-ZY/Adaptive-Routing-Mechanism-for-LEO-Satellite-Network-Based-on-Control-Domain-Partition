# Adaptive-Routing-Mechanism-for-LEO-Satellite-Network-Based-on-Control-Domain-Partition



## /DQN_routing
​		Running DNQ-based dynamic routing algorithms on randomly generated networks.

​		Throughout one episode of the simulation, edges are randomly chosen to disappear and be restored at each time step. In addition, edge weights fluctuate in a sinusoidal manner throughout the episode. At the beginning of each episode, a number of packets (the network load) is generated on the network, each with a random start and destination node. Every time a packet is delivered, a new one is initialized some number of time steps later. Once a set number of packets have been generated and delivered on the network, the episode ends. Average packet delivery time and various measures of network congestion are then calculated.


### Requirements:
- NetworkX
- FFmpeg (for animating)
- Matplotlib
- OpenAI Gym
- PyTorch

### File Descriptions
- DQN.py
    - Specifies hidden layer and activation functions
- neural_network.py
    - Create instance of neural networks which contains DQN instances, specify memory size, policy and target networks, and optimizer.
- replay_memory.py
    - contain methods for creating reply_memory instance, pushing and pulling experiences.
- Setting.json
    - contain all the settings for network, parameters for deep Q-learning, agent and setup for simulation.
- DeepQSimulation.py
    -Teaches an agent based on the max in a list of network loads for a fixed number of episodes. Then routes using deep Q-learning algorithms. Outputs measures of delivery time and congestion. Contains options for comparing to Shortest Path.

### Usage
- Open Setting.json and specify desired settings
- Open DeepQSimulation.py and run the program in python 3





## /StarPerf

​		Building geometric scenarios for satellite networks, including satellite constellation creation, addition of inter satellite links and transceivers, access analysis, and orbit analysis, to provide physical parameters for subsequent simulations.

### Requirements:

- MATLAB 2019
- STK v12.2

### File Descriptions

- constellation_data: TLE file information for constellations, used to import STK to create constellations
- countries_json: Location information of ground stations
- matlab_code:
  - build_constellation: Main function, creating constellation and calling other functions to generate inter satellite link information.
  - Create_delay: Calculate delay between LEOs and facilities.
  - Create_Fac: Create ground facilities
  - Create_LEO: Create LEOs in STK.
  - Create_location
  - Lla2Cbf

