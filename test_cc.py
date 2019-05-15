import os, sys, re, os.path
import platform
import subprocess, datetime, time, signal

def replace(filename, pattern, replacement):
	f = open(filename)
	s = f.read()
	f.close()
	s = re.sub(pattern,replacement,s)
	f = open(filename,'w')
	f.write(s)
	f.close()

jobs = {}
dbms_cfg = ["config-std.h", "config.h"]
algs = ["WAIT_DIE", "NO_WAIT", "DL_DETECT", "TIMESTAMP", "MVCC","HEKATON", "HSTORE", "OCC", "VLL", "TICTOC", "SILO"]

def insert_job(alg):
	jobs[alg] = {
		"CC_ALG"			: alg,
		"WORKLOAD"			: "TPCC",
		"MAX_TXN_PER_PART"	: 1000000
	}

def test_compile(job):
	os.system("cp "+ dbms_cfg[0] +' ' + dbms_cfg[1])
	for (param, value) in job.iteritems():
		pattern = r"\#define\s*" + re.escape(param) + r'.*'
		replacement = "#define " + param + ' ' + str(value)
		replace(dbms_cfg[1], pattern, replacement)
	os.system("sed -n 19p config.h")
	os.system("sed -n 42p config.h")
	os.system("sed -n 112p config.h")
	os.system("make clean > temp.out 2>&1")
	ret = os.system("make -j > temp.out 2>&1")
	if ret != 0:
		print "ERROR in compiling job="
		print job
		exit(0)
	print "PASS Compile\t\talg=%s,\tworkload=%s" % (job['CC_ALG'], job['WORKLOAD'])
	for i in range(8):
		os.system("./rundb -n1 -p1 -t"+str(i+1)+" > ./Result/"+job['CC_ALG']+"_t"+str(i+1)+".txt")	
		print "PASS Run\t\talg=%s,\tthread=%d" % (job['CC_ALG'], i+1)

# run TPCC tests
jobs = {}
os.system("mkdir -p Result")
for alg in algs: 
	insert_job(alg)
for (jobname, job) in jobs.iteritems():
	test_compile(job)
os.system('cp config-std.h config.h')
os.system('make clean > temp.out 2>&1')
os.system('rm temp.out')
