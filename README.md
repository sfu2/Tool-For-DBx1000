# Tool For DBx1000
## 介绍
[DBx1000](https://github.com/yxymit/DBx1000)是一个单节点OLTP数据库管理系统(DBMS)。DBx1000的目标是使DBMS在未来的1000核处理器上可伸缩。DBx1000目前实现了所有7种经典的并发控制方案。它们在不同的工作负载下显示不同的可伸缩性属性。

本repo旨在为DBx1000编写自动化测试程序。

```test_cc.py```
测试DBx1000提供的所有并发控制算法。具体测试参数为：
- 仓库数量：1
- 分区数量：1
- 线程数量：1-8
- 工作负载：TPCC

各项测试结果默认重定向至DBx1000/Result/目录下，文件名为"算法名_t线程数量.txt"。例：WAIT_DIE_t1.txt即为DBx1000在WAIT_DIE并发控制算法下使用1个线程的测试结果。

## 用法
1. 切换至DBx1000的目录下
```
cd /path/to/DBx1000
```
2. 运行自动测试程序
```
python test_cc.py
```
预期输出：
```
#define WORKLOAD TPCC
#define CC_ALG HEKATON
#define MAX_TXN_PER_PART 1000000
PASS Compile		alg=HEKATON,	workload=TPCC
PASS Run		alg=HEKATON,	thread=1
PASS Run		alg=HEKATON,	thread=2
PASS Run		alg=HEKATON,	thread=3
PASS Run		alg=HEKATON,	thread=4
PASS Run		alg=HEKATON,	thread=5
PASS Run		alg=HEKATON,	thread=6
PASS Run		alg=HEKATON,	thread=7
PASS Run		alg=HEKATON,	thread=8
#define WORKLOAD TPCC
#define CC_ALG WAIT_DIE
#define MAX_TXN_PER_PART 1000000
PASS Compile		alg=WAIT_DIE,	workload=TPCC
PASS Run		alg=WAIT_DIE,	thread=1
PASS Run		alg=WAIT_DIE,	thread=2
...
```

## FAQ
1. 测试程序终止又不希望从头开始执行所有算法

可在```test_cc.py```第16行左右的```algs```列表中手动删去已测试过的算法
```python
algs = ["WAIT_DIE", "NO_WAIT", "DL_DETECT", "TIMESTAMP", "MVCC","HEKATON", "HSTORE", "OCC", "VLL", "TICTOC", "SILO"]
```
