class Process:
    #This stores the attributes of each process
    def __init__(self, name, arrival_time, burst_time):
        self.name = name
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.waiting_time = 0
        self.turnaround_time = 0
        self.completion_time = 0

processes=[]#to store object processes of class Process

n=int(input("Enter the number of processes: "))
for i in range(n):
    name=input(f"Enter the name of Process {i+1}: ")
    arrival_time=int(input("Enter the arrival time of the process: "))
    burst_time=int(input("Enter the burst time of the process: "))
    
    P_info=Process(name, arrival_time, burst_time)
    processes.append(P_info)

    
#sorting the processes according to arrival time
processes.sort(key=lambda p: p.arrival_time)
for p in processes:
    # This is to check if the processes are in the order of their arrival time
    print(f"Process: {p.name}, Arrival Time: {p.arrival_time}, Burst Time: {p.burst_time}")

