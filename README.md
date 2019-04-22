# Stupid Parallel Simulation
An easy script to help simulate your code in parallel mode.

**Added Matlab Support !!**

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

## Who am I? (for Matlab projects)
For Matlab projects, the configuration procedures are almost the same as the previous section. Some few differences are listed as follows.

Please change:
```
  for i = [1,2,3]
    for j = 2:4
      a long process to simulate something...
    end
  end
```
To:
```
  i = #p.1#
  j = #p.2#
  a long process to simulate something...
```
Please tell me that #p.1# is 1,2,3, and #p.2# is 2,3,4.

**In addition**, PLEASE add a new command: `exit;` to the end of the Matlab script !!! Otherwise this script will not function properly !!!

## What is a Configuration File?
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
RUN `run.py` and just follow the guide! Or you can create a configuration file to skip the process! It's just that simple!

Requirement: Python Version 3.6+

## 中文简介

**本项目解决什么问题？**

假设一段耗时的代码，用到仿真参数i和j，i和j各长3，总共需要仿真9段循环，极其耗时！一般情况下，我们会复制该工程9次，分别修改下面的运行脚本为对应的i和j的组合，再分别打开运行，可以节省一些时间。但是！当代码一旦修改，复制9次的操作又将再来一遍！本项目就是为了帮助你自动完成这一伪并行化仿真的操作！

**怎么用？**

两种模式：

[A] 按照脚本`run.py`的指引来！请仔细看指引里的提示语句，虽然很多，但必须按照它来操作！ 

[B] 自己在把工程文件夹复制到脚本目录后，创建一个配置文件，工程叫`张三`，那么配置文件就叫`config_张三.txt`，按照上上节的介绍去写！运行run.py后先把工程名给它，配置文件就会自动读入，也就略过了指引步骤！

**有什么注意事项？**

1. 所有仿真项目都需要先拷贝到本项目所在的文件夹下，必须是整个文件夹拷，别零零散散的拷贝过来！
2. 所有仿真都会有仿真入口脚本，请在入口脚本里面把仿真里嵌套循环去掉！然后把循环变量写成`i=#p.X#`的形式，请参考前文！
3. 如果你是Matlab工程，请务必在入口脚本最后添加一行`exit;`语句，保证仿真结束窗口的自动关闭，否则这个工具就失效了，根本无法工作！
4. 如果你是Matlab工程，可以先试一试能不能用！如果不能用，说明你需要添加matlab的系统变量，请参考：[这个链接](https://blog.csdn.net/qq_16019107/article/details/77882017)
5. 请酌情设定MAX NUMBER，也即同时跑多少个仿真的控制参数，设置太大计算机会崩坏的！
6. 项目支持仿真结果的自动收集，这在配置文件和指引里都可以设置！前提是，你要保证仿真代码最后会把结果输出到下属文件夹中！如果最后输出结果和入口脚本在同一级目录，这个工具没法帮你！因为要提前指定结果文件夹的！
7. 不看上面的注意事项你会后悔的，甚至可能运行出一堆错误！

## Update Log
0422 UPDATE
- **Added support for Matlab projects**
- Added a new function for data collection (see above for its usage)
- Fixed a crash problem for repeated running on a certain project
- Fixed a crash problem when Python project has `**` expressions

0421 UPDATE
- Added configuration file, which is a txt document, to simplify your work
- Fixed the number control issue when runnning parallel simulations
- Modified some expressions in the guide

## Extra Info
Version.20190422

Current version only supports Python projects. ~~and cannot help you with data collection.~~(0422 update added this function)

Any ideas about how to improve this project are welcomed in the repo issues!!
