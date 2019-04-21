# -*- encoding:utf-8 -*-

import os,re
import shutil
import queue
import threading
import time

def main():
	print("Welcome to Stupid Parallel Simulation!")
	print("This guide will help you run your stupid code in parallel mode!")
	print("Exciting, isn't it? The principle is simple:")
	print("For each set of simulation parameter, we help you start a new instance to run it.")
	print("Though stupid, we still coded this script to help you finish your work before deadline!")
	print("We still hope that you make some modifications to your stupid code to fully utilize your multi-core CPU!")
	print("This script can only support WINDOWS environment and PYTHON projects for the current version!")
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

	is_config_exist = True
	if not dir_name == "":
		config_name = "config_" + dir_name + ".txt"
		if os.path.exists(config_name):
			paras = dict()
			max_paras = 0
			judger = [False]*3
			with open(config_name,'r',encoding='UTF-8') as f:
				for line in f.readlines():
					if line.__contains__('='):
						sets = line.replace('\r','').replace('\n','').split('=')
						k = sets[0].strip(' ')
						v = sets[1].strip(' ')
						if k == 'name':
							script_name = v.replace('.py','').replace('.m','')
							judger[0] = True
						if k == 'max_num':
							max_num = int(v)
							judger[1] = True
						if k.strip('#').split('.')[0] == 'p':
							judger[2] = True
							paras[int(k.strip('#').split('.')[1])] = v.split(',')
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
		script_name = input("main script name please (without .py suffix):").strip(" ").replace(".py","")

		print()
		sep()
		print("STEP 4 : Open the main script and delete the loops for testing different parameters")
		sep()
		input("PRESS ANY KEY when you finish...")

		print()
		sep()
		print("STEP 5 : Replace all the original in-loop parameters to our required expressions:")
		print("e.g. A=a(i), i is the original loop index => A=#p.1#")
		print("e.g. B=b(j), j is the original loop index => B=#p.2#")
		print("If the set of simulation parameter contains 3 parameters, you'd have to modify them sequentially to #p.1#, #p.2#, and #p.3#")
		print("Please make sure your indentation is correct and #p.x# is written in lowercase!")
		print("After you finish, the Python scripts will not be formatted correctly!")
		sep()
		input("PRESS ANY KEY when you finish...")

		print()
		print("Reading the number of simulation parameters...")
		r = re.compile(r'#p.[0-9]*#')
		with open(dir_name + "\\" + script_name + ".py", 'r', encoding="UTF-8") as f:
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
			pl = input("Give your value sets for para.%d : " % (n+1))
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
	print("STEP FINAL : Please wait for us to run your stupid codes, will you?")
	sep()
	print("Settings for your simulation:")
	print("project name: %s and main script name: %s" % (dir_name,script_name))
	print("script has %d simulation parameters, which are:" % max_paras)
	c = 1
	for p in para_list:
		print("parameter %d = %s" % (c,','.join(p)))
		c = c + 1
	print("max number of parallel simulations: %d" % max_num)
	input("PRESS ANY KEY when you're ready to start the `parallel` simulation...")

	print("Creating temporary directories for parallel simulations...")
	plist_tmp = lists_combination(para_list, code=',')
	plist = list()
	for p in plist_tmp:
		plist.append(p.split(','))
	shutil.rmtree(dir_name + '_sim', ignore_errors=True)
	time.sleep(3.0)
	while os.path.exists(dir_name + '_sim'):
		pass
	full_target_queue = queue.Queue()
	for name in plist:
		new_dir_name = dir_name + '_sim' + '\\' + dir_name + '_' + '_'.join(name)
		full_target_queue.put(new_dir_name)
		shutil.copytree(dir_name, new_dir_name)
		with open(new_dir_name + '\\' + script_name + '.py', 'r', encoding="UTF-8") as f:
			script = '**'.join(f.readlines())
			for ind in range(max_paras):
				rep_target = "#p." + str(ind+1) + "#"
				script = script.replace(rep_target, name[ind])
			script = script.split('**')
		with open(new_dir_name + '\\' + script_name + '.py', 'w', encoding="UTF-8") as f:
			f.writelines(script)
	print("Created successfully...")

	print("Starting simulations...")
	threadpool = dict()
	for i in range(max_num):
		threadpool[str(i)] = None
	while True:
		# Check Thread Status & Pop dead threads
		threadpool = clear_threadpool(threadpool)
		# Check Termination Condition
		if len_threadpool(threadpool) == 0 and full_target_queue.empty():
			break
		# Add New Threads & Start
		while len_threadpool(threadpool) < max_num and not full_target_queue.empty():
			if not full_target_queue.empty():
				pp = full_target_queue.get()
				t = threading.Thread(target=run_proc, args=(str(pp).replace('\\','/'),script_name + '.py'))
				t.start()
				threadpool = fill_threadpool(str(pp), t, threadpool)
				print("Added simulation: %s ..." % pp)
		time.sleep(5.0)
	print("Simulations are all complete...")
	print("Thanks for using Stupid Parallel Simulation !!!")
	input("Press any key to close me...")


def run_proc(dirname,filename):
	os.system("cd %s & start /wait cmd /c python %s" % (dirname, filename))
	#"cd CNVChain_sim\CNVChain_0.1_3 & start /wait cmd /c python main_bran_implementation_blocktime.py"

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

def clear_threadpool(tp):
	for (k, v) in tp.items():
		if not v == None and (not v[1].is_alive() or not v[1].isAlive()):
			tp[k] = None
			print("Simulation complete: %s ..." % v[0])
	return tp

def len_threadpool(tp):
	len = 0
	for (k, v) in tp.items():
		if not v == None:
			len = len + 1
	return len

def lists_combination(lists, code=''):
	#输入多个列表组成的列表, 输出其中每个列表所有元素可能的所有排列组合code用于分隔每个元素
	try:
		import reduce
	except:
		from functools import reduce
	def myfunc(list1, list2):
		return [str(i) + code + str(j) for i in list1 for j in list2]
	return reduce(myfunc, lists)

if __name__ == "__main__":
	main()