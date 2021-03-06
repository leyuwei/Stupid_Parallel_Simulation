# -*- encoding:utf-8 -*-

import os,re
import shutil
import queue
import threading
import time
import random

def main():
	print("Welcome to Stupid Parallel Simulation!")
	print("This guide will help you run your stupid code in parallel mode!")
	print("Exciting, isn't it? The principle is simple:")
	print("For each set of simulation parameter, we help you start a new instance to run it.")
	print("Though stupid, we still coded this script to help you finish your work before deadline!")
	print("We still hope that you make some modifications to your stupid code to fully utilize your multi-core CPU!")
	print("This script supports WINDOWS environment and Python/Matlab projects!")
	input("PRESS ANY KEY when ready...")

	print()
	sep()
	print("First let me ask you a question: do you have a config file in the current directory?")
	print("It means you have both directory `hello` and text file `config_hello.txt` in the current directory.")
	print("The config file will be read to configure your simulation automatically!")
	print("If you don't know how to write a config file, please refer to the example `config_test` for project `test`!")
	print("However, I still recommend you to go through the whole guide when you first use this tool!!")
	print("Just type your project name (e.g. `hello`,`test`) to let me know you have configured a config file.")
	print("If not, please leave the following input field blank and just input an ENTER!")
	sep()
	dir_name = input("project name please:").strip()

	is_python = True # Default: python project
	file_suffix = '.py'

	is_config_exist = True
	if not dir_name == "":
		config_name = "config_" + dir_name + ".txt"
		if os.path.exists(config_name):
			paras = dict()
			max_paras = 0
			judger = [False]*3
			output_folder = ''
			with open(config_name,'r',encoding='UTF-8') as f:
				for line in f.readlines():
					if line.__contains__('='):
						sets = line.replace('\r','').replace('\n','').split('=')
						k = sets[0].strip(' ')
						v = sets[1].strip(' ')
						if k == 'name':
							if v.__contains__('.m'):
								is_python = False
								file_suffix = '.m'
							script_name = v.replace('.py','').replace('.m','')
							judger[0] = True
						if k == 'max_num':
							max_num = int(v)
							judger[1] = True
						if k == 'output_folder':
							output_folder = str(v).strip(' ')
						if k.strip('#').strip(' ').split('.')[0] == 'p':
							judger[2] = True
							paras[int(k.strip('#').strip(' ').split('.')[1])] = v.replace(' ','').split('#')[0].split(',')
							max_paras = max_paras + 1
			para_list = sorted_dict_values(paras)
			for j in judger:
				if not j:
					is_config_exist = False
					print("\n%s is not properly formatted and cannot be read!" % config_name)
					break
		else:
			is_config_exist = False
			print("\n%s does not exist! You liar!" % config_name)

	if dir_name == "" or not is_config_exist:
		print("\nOK then, I'm happy to guide you through the configuration process. BE PATIENT !!!")

		print()
		sep()
		print("STEP 1 : Move your codes to the same directory where you run this script")
		sep()
		input("PRESS ANY KEY when you finish...")

		print()
		sep()
		print("STEP 2 : Tell us the name you given to your simulation directory")
		sep()
		dir_name = input("name please:").strip(" ")

		print()
		sep()
		print("STEP 3 : Tell us the entrance script name that will start your simulation")
		sep()
		script_name = input("main script name please (WITH suffix .py or .m):").strip(" ")
		if script_name.__contains__('.m'):
			is_python = False
			file_suffix = '.m'
		script_name = script_name.replace('.py','').replace('.m','')

		print()
		sep()
		print("STEP 4 : Open the main script and delete the loops for testing different parameters")
		print("If you're using Matlab, please add `exit;` to the end of the script, otherwise it won't be functional!!")
		sep()
		input("PRESS ANY KEY when you finish...")

		print()
		sep()
		print("STEP 5 : Replace all the original in-loop parameters to our required expressions:")
		print("e.g. A=a(i), i is the original loop index => A=#p.1#")
		print("e.g. B=b(j), j is the original loop index => B=#p.2#")
		print("If the set of simulation parameter contains 3 parameters, you'd have to modify them sequentially to #p.1#, #p.2#, and #p.3#")
		print("If you're using Python, please make sure your indentation is correct and #p.x# is written in lowercase!")
		print("After you finish, the Python or Matlab scripts will be tested several error syntax!")
		sep()
		input("PRESS ANY KEY when you finish...")

		print()
		print("Reading the number of simulation parameters...")
		r = re.compile(r'#p.[0-9]*#')
		with open(dir_name + "\\" + script_name + file_suffix, 'r', encoding="UTF-8") as f:
			lines = f.readlines()
			placeholders = r.findall(','.join(lines))
			max_paras = 0
			for ph in placeholders:
				if get_para_num(ph) > max_paras:
					max_paras = get_para_num(ph)
		sep()
		print("STEP 6 : Please give the value sets of %d parameters in your code." % max_paras)
		print("For example: 0,1,2,3,4,5 for original i=range(6)")
		print("Please make sure you separate each parameter with comma!")
		sep()
		para_list = list()
		for n in range(max_paras):
			pl = input("Give your value sets for para.%d : " % (n+1)).strip(' ')
			pl = pl.split(',')
			para_list.append(pl)

		print()
		sep()
		print("STEP 7 : Tell us how many simulations would you prefer to run at the same time?")
		print("(If you don't want to see your device burning or running into some annonying blue screens)")
		sep()
		max_num = int(input("a MAX number please:").strip(" "))

		print()
		sep()
		print("STEP 8 : If you want me to help you collect the simulation output files, please tell me where?")
		print("For example, if your result file is in test/re, you should give me `re` and I will collect the results for you!")
		print("The names of output files should contain the simulation parameters, otherwise the files will be overwritten by me!")
		sep()
		output_folder = input("output folder name please:").strip(" ")

	print()
	sep()
	print("FINAL STEP : Please wait for me to run your stupid codes, will you?")
	sep()
	print("Settings for your simulation:")
	if is_python:
		print("You've planned a parallel simulation for a Python project!")
	else:
		print("You've planned a parallel simulation for a Matlab project!")
		with open(dir_name + "\\" + script_name + file_suffix, 'r', encoding="UTF-8") as f:
			if not ','.join(f.readlines()).__contains__('exit'):
				print("The last line of your script has not been added the command: `exit;` !!! PLEASE DO IT NOW !!!")
	print("project name: %s , main script name: %s" % (dir_name,script_name))
	print("script has %d simulation parameters, which are:" % max_paras)
	c = 1
	for p in para_list:
		print("parameter %d = %s" % (c,','.join(p)))
		c = c + 1
	print("max number of parallel simulations: %d" % max_num)
	print("output folder: %s" % output_folder)
	input("PRESS ANY KEY when you're ready to start the `parallel` simulation...")

	# START Simulation !
	print("Creating temporary directories for parallel simulations...")
	plist_tmp = lists_combination(para_list, code=',')
	plist = list()
	for p in plist_tmp:
		plist.append(p.split(','))
	shutil.rmtree(dir_name + '_sim', ignore_errors=True)
	while os.path.exists(dir_name + '_sim'):
		time.sleep(2.0)
		pass
	full_target_queue = queue.Queue()
	sepper = '***'
	for name in plist:
		new_dir_name = dir_name + '_sim' + '\\' + dir_name + '_' + '_'.join(name)
		full_target_queue.put(new_dir_name)
		shutil.copytree(dir_name, new_dir_name)
		with open(new_dir_name + '\\' + script_name + file_suffix, 'r', encoding="UTF-8") as f:
			script = sepper.join(f.readlines())
			for ind in range(max_paras):
				rep_target = "#p." + str(ind+1) + "#"
				script = script.replace(rep_target, name[ind])
			script = script.split(sepper)
		with open(new_dir_name + '\\' + script_name + file_suffix, 'w', encoding="UTF-8") as f:
			f.writelines(script)
	print("Created successfully...")

	print("Starting simulations...")
	threadpool = dict()
	for i in range(max_num):
		threadpool[str(i)] = None
	task_count = 0
	while True:
		# Check Thread Status & Pop dead threads
		threadpool = clear_threadpool(threadpool, output_folder, dir_name)
		# Check Termination Condition
		if len_threadpool(threadpool) == 0 and full_target_queue.empty():
			break
		# Add New Threads & Start
		while len_threadpool(threadpool) < max_num and not full_target_queue.empty():
			if not full_target_queue.empty():
				pp = full_target_queue.get()
				t = threading.Thread(target=run_proc, args=(str(pp).replace('\\','/'),script_name + file_suffix))
				t.start()
				threadpool = fill_threadpool(str(pp), t, threadpool)
				task_count = task_count + 1
				print("[ %d / %d ] Added simulation: %s ..." % (task_count,len(plist_tmp),pp))
		time.sleep(5.0)
	print("Simulations are all complete...")
	print("Thanks for using Stupid Parallel Simulation !!!")
	input("Press any key to close me...")


# Other functions

def run_proc(dirname,filename):
	if str(filename).strip(' ').endswith('.py'):
		os.system("cd %s & start /wait cmd /c python %s" % (dirname, filename))
		#"cd CNVChain_sim\CNVChain_0.1_3 & start /wait cmd /c python main_bran_implementation_blocktime.py"
	else:
		os.system("cd %s & start /wait cmd /c matlab -nosplash -nodesktop -wait -r %s" % (dirname, str(filename).replace('.m','')))

def sep():
	print("====================================")

def get_para_num(para):
	return int(para.replace('#','').split('.')[1])

def sorted_dict_values(di):
	return [di[k] for k in sorted(di.keys())]

def fill_threadpool(name,t,tp):
	for (k, v) in tp.items():
		if v == None:
			tp[k] = [name,t]
			break
	return tp

def clear_threadpool(tp, output_folder, dir_name):
	for (k, v) in tp.items():
		if not v == None and (not v[1].is_alive() or not v[1].isAlive()):
			tp[k] = None
			print("Simulation complete: %s ..." % v[0])
			collect_output_data(v[0], output_folder, dir_name)
	return tp

def collect_output_data(instance_name, output_folder, dir_name):
	if not os.path.exists(instance_name + '/' + output_folder):
		return
	if not os.path.exists(dir_name + '_sim' + '\\output_results'):
		os.makedirs(dir_name + '_sim' + '\\output_results')
	try:
		copy_tree(instance_name + '\\' + output_folder, dir_name + '_sim' + '\\output_results')
		print("Collected data for %s ..." % instance_name)
	except:
		print("Error when collecting data for %s ..." % instance_name)

def len_threadpool(tp):
	len = 0
	for (k, v) in tp.items():
		if not v == None:
			len = len + 1
	return len

def copy_tree(path, out):
	for files in os.listdir(path):
		name = os.path.join(path, files)
		back_name = os.path.join(out, files)
		if os.path.isfile(name):
			if os.path.isfile(back_name):
				if not os.path.exists(back_name):
					shutil.copy(name,back_name)
				else:
					new_name = str(back_name).split('.')
					if len(new_name) > 1:
						new_name = new_name[0] + '_' + str(random.randint(0,65535)) + '.' + new_name[1]
					else:
						new_name = back_name + str(random.randint(0,65535))
					shutil.copy(name, new_name)
			else:
				shutil.copy(name, back_name)
		else:
			if not os.path.isdir(back_name):
				os.makedirs(back_name)
			copy_tree(name, back_name)

def lists_combination(lists, code=''):
	try:
		import reduce
	except:
		from functools import reduce
	def myfunc(list1, list2):
		return [str(i) + code + str(j) for i in list1 for j in list2]
	return reduce(myfunc, lists)

if __name__ == "__main__":
	main()