# Stupid Parallel Simulation
An easy script to help simulate your code in parallel mode.

## Who am I? (for Python projects)
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
6. ask me to collect the output data for you automatically, if your codes have some output results.
7. start and hand it over to me. (I'll handle everything for you then!)

## What is Configuration File?
If your project directory is `test`, the configuration file should exist in the same directory where you run this script.

It should be named to `config_test.txt` and looks like this:

```
  name = test.py
  p.1 = 1,2,3
  p.2 = 3,4,5
  max_num = 2
  output_folder = re
```

It tells me you want to run `test\test.py`, while parameter 1 should iterate through 1 to 3 and parameter 2 from 3 to 5. You want 2 simulations to run at the same time and you want me to collect your output results under folder `test\re` to a fixed directory named `output_results`.

`output_folder` is not a required field, while others are all required for a fully functional configuration file!

## How to use me?
RUN `run.py` and just follow the guide! It's just that simple!

## Update Log
0422 UPDATE
- Added a new function for data collection (see above for its usage)
- Fixed a crash problem for repeated running on a certain project

0421 UPDATE
- Added configuration file, which is a txt document, to simplify your work
- Fixed the number control issue when runnning parallel simulations
- Modified some expressions in the guide

## Extra Info
Version.20190422

Current version only supports Python projects. ~~and cannot help you with data collection.~~(0422 update added this function)

Any ideas about how to improve this project are welcomed in the repo issues!!
