import re

# FILL 'DIR' WITH YOUR OWN RESULT DIRECTORY !!!
DIR = "Result/"
ALGS = ["WAIT_DIE", "NO_WAIT", "DL_DETECT", "TIMESTAMP", "MVCC","HEKATON", "HSTORE", "OCC", "TICTOC", "SILO"]

# headers
for alg in ALGS:
    print(alg[0:7] if len(alg) > 7 else alg, end='\t')
print('BEST')
# calculate throughput
for i in range(1,9):
    max_throughput = 0
    max_alg = ''
    for alg in ALGS:
        sim_time = 1
        txn_cnt = 0
        file = open(DIR + alg + "_t" + str(i) + ".txt").readlines()
        for line in file:
            if 'SimTime' in line:
                sim_time = int(line.split("= ")[-1])
            if '[summary]' in line:
                txn_cnt = int(re.findall('txn_cnt=\d+', line)[0].split('=')[-1])
        throughput = 10000 * txn_cnt / sim_time
        print("%.5f " % throughput, sep='\t', end='')
        # get the best algorithm
        if max_throughput < throughput:
            max_throughput = throughput
            max_alg = alg
    print(max_alg)
