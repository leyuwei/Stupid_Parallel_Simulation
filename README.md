# Stupid_Parallel_Simulation
An easy script to help simulate your code in parallel mode. It will save you much time!

## Who am I?
Have you ever run into such situation during your research work?
```
  for i in range(8):
    for j in range(5):
      a long process to simulate something...
```
The above code will take up 40 loops to finish, which is so fxxking annoying, isn't it?

Now, with Stupid Parallel Simulation to help you, you just need to do this:

1. copy your simulation project into the directory where I am.
2. tell me which script to begin with.
3. modify the specific code to (notice that the indentation should also be modified slightly):
```
  i=#p.1#
  j=#p.2#
  a long process to simulate something...
```
4. tell me what is #p.1# and #p.2#. (type in 0,1,2,3,4,5,6,7 for #p.1#)
5. tell me how much parallel simulations you want to run at the same time.
6. start and hand over to me. (I'll handle everything for you then!)

## How to use me?
RUN `run.py` and just follow the guide! It's just that simple!

## Update Log
0421 UPDATE
- Added configuration file, which is a txt document, to simplify your work
- Fixed the number control issue when runnning parallel simulations
- Modified some expressions in the guide

## Extra Info
Version.20190421

Current version only supports Python projects and cannot help you with data collection.

Any ideas about how to improve this project are welcomed in the repo issues!!
