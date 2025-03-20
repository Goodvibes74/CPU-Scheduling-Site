# app/models/__init__.py

from .process import Process
from .FCFS import fcfs_scheduling
from .SJF import sjf_scheduling
from .SJF_preemptive import sjf_preemptive_scheduling
from .Round_Robin import round_robin_scheduling
from .Priority_scheduling import priority_scheduling
from .Priority_scheduling_preemptive import priority_preemptive_scheduling
