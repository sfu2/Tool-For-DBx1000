import re

# FILL 'DIR' WITH YOUR OWN RESULT DIRECTORY !!!
DIR = "Result/"
ALGS = ["WAIT_DIE", "NO_WAIT", "DL_DETECT", "TIMESTAMP", "MVCC","HEKATON", "HSTORE", "OCC", "TICTOC", "SILO"]

# headers
for alg in ALGS:
    print("{: ^8s} ".format(alg[0:8] if len(alg) > 8 else alg), end='')
print('BEST')
# calculate throughput
for thd_cnt in range(1,9):
    max_throughput = 0
    max_alg = ''
    for alg in ALGS:
        run_time = 1
        txn_cnt = 0
        file = open(DIR + alg + "_t" + str(thd_cnt) + ".txt").readlines()
        for line in file:
            if '[summary]' in line:
                txn_cnt = int(re.findall('txn_cnt=\d+', line)[0].split('=')[-1])
                run_time = float(re.findall('run_time=\d+.\d+', line)[0].split('=')[-1])
        throughput = txn_cnt / run_time * thd_cnt
        print("%8.1f " % throughput, sep='\t', end='')
        # get the best algorithm
        if max_throughput < throughput:
            max_throughput = throughput
            max_alg = alg
    print(max_alg)
