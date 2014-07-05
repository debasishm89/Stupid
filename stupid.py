'''
This software is licenced under a Beerware licence. 
/*
 * ----------------------------------------------------------------------------
 * "THE BEER-WARE LICENSE" (Revision 42):
 * <debasishm89@gmail.com> wrote this file. As long as you retain this notice you
 * can do whatever you want with this stuff. If we meet some day, and you think
 * this stuff is worth it, you can buy me a beer in return Debasish Mandal.
 * ----------------------------------------------------------------------------
 */
'''
try:
	from pydbg import *
	from pydbg.defines import *
except ImportError:
    raise ImportError('[Error] Pydbg is not installed. Which is required to run this fuzzer. Install Pydbg First')
import random
import math
import thread
import time
import shutil
from datetime import datetime
import gc
import utils
import os
from os.path import join
import time

######################   Fuzzer Configuration(Change These parameters Based on your requirement) ##############

timeout = 1										# Run target application for 1 seconds and look for Access violation.
temp_dir = 'c:\\temp\\'							# Temporary Directory
basefile_dir = 'c:\\bases'						# This directory will contain all base files
programname = "c:\\Windows\\notepad.exe"		# Full target application binary path
command_line_arg = ""							# Command line arguments (if any required for programname)
fuzzratio = float(0.09)							# percentage of file size bytes to fuzz

###############################################################################################################
def printBanner():
	print '''
	  ____  _               _     _ 
	 / ___|| |_ _   _ _ __ (_) __| |
	 \___ \| __| | | | '_ \| |/ _` |
	  ___) | |_| |_| | |_) | | (_| |
	 |____/ \__|\__,_| .__/|_|\__,_|
                         |_|            
   The dumbest file format Fuzzer in the whole world!!
	   Author : Debasish Mandal \n\n'''
crash_binning = utils.crash_binning.crash_binning()
def int2binary(n, cnt=24):
    return "".join([str((n >> y) & 1) for y in range(cnt-1, -1, -1)])

def mutate(data):
	b = list(data)
	data_to_be_fuzzed = random.randrange(math.ceil((float(len(data))) * fuzzratio))+1		#Number of bytes to fuzz
	case = random.randint(0,1)
	if case == 0:
		# Replace random offsets with random chars
		for j in range(data_to_be_fuzzed):		#Iterate all bytes
			randbyte = random.randrange(256)	#Random character
			ran = random.randrange(len(data))	#Random offset
			b[ran] = '%c'%(randbyte)			#Replace
		mutated =''.join(b)						#Append
	if case == 1:
		# Bit flip randomly chosen bytes
		for j in range(data_to_be_fuzzed):		#Iterate
			ran = random.randrange(len(data))	#Random offset
			bits = int2binary(ord(b[ran]),8)	#Int to Binary
			flipped = bits[::-1]				#Bit-flip
			b[ran] = chr(int(flipped,2))		#Replace
		mutated =''.join(b)						#Append
	return mutated
def AccessViolationHandler (dbg):
	print '[+] BOOM!! Target Crashed'
	global crash_binn
	crash_binn = utils.crash_binning.crash_binning()
	crash_binn.record_crash(dbg)
	currtime = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
	crashfilename = 'crash_'+programname.split('\\',programname.count('\\'))[-1]+'_'+'_'+ currtime +'.html'
	synfilename = 'crashes\\crash_'+programname.split('\\',programname.count('\\'))[-1]+'_'+'_'+ currtime +'.txt'
	shutil.copyfile(temp_file_path + fuzzfilename,'crashes\\'+crashfilename)
	print '[+] Crash file Copied',crashfilename
	syn = open(synfilename,'w')
	syn.write(crash_binn.last_crash_synopsis())
	syn.close()
	if dbg.debugger_active:
		dbg.terminate_process()
	return DBG_CONTINUE
def StillRunning(dbg):
	time.sleep(timeout)
	if dbg.debugger_active:
		dbg.terminate_process()

def startfuzzer():
	printBanner()
	raw_input('[+] Press Enter to Continue...')
	c = 1
	if len(basefilelist) == 0:
		print '[+] No base files @ ',basefile_dir
		exit()
	print basefilelist
	print '[+] Starting Fuzzing..'
	while 1:
		global basefilename,ext,fuzzfilename
		basefilename = random.choice(basefilelist)
		ext = basefilename.split('.',1)[1]
		fuzzfilename = 'fuzz_' +  basefilename.split('\\',basefilename.count('\\'))[-1:][0]
		fi = open(basefilename,'rb')
		file_data = fi.read()
		fi.close()
		if c%100 == 0:
			collected = gc.collect()
			print '[+] '+str(c)+'th Testcase'
			print "[+] Garbage collector triggered: collected %d objects." % (collected)
		mutated = mutate(file_data)
		try:
			fo = open(temp_dir + fuzzfilename,'wb')
			fo.write(mutated)
			fo.close()
		except Exception, e:
			print '[+] Unable to write new file skipping..'
		dbg = pydbg()
		dbg.set_callback(EXCEPTION_ACCESS_VIOLATION, AccessViolationHandler)
		thread.start_new_thread(StillRunning, (dbg, ))
		args = command_line_arg + " " + temp_dir + fuzzfilename
		dbg.load(programname,args , show_window=True)
		dbg.run()
		c = c + 1
if __name__ == "__main__":
	basefilelist = []
	bases = list()
	for (dirpath, dirname, filenames) in os.walk(basefile_dir):
		for name in filenames:
			a, b = os.path.splitext(join(dirpath,name))
			bases.append((a, b))
	for i in bases:
		basefilelist.append(i[0]+i[1])
	startfuzzer()