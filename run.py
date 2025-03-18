from flask import Flask, render_template, request
from app.models.FCFS import Process, FCFS

app=Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method=="POST":
        process_list=[]
        Nop=int(request.form["Nop"])#number of processes(Nop)

    for i in range(Nop):
        name=request.form[f"name{i}"]
        arrival_time=int(request.form[f"arrival_time{i}"])    
        burst_time=int(request.form[f"burst_time{i}"])
        process_list.append(Process(name, arrival_time, burst_time))
            