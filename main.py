import subprocess

i = 1
    
args = ['sbatch', '-J', "sleep"+str(i), 'sleepy.sbatch']

print("submitting job:", i, flush=True)
jid1 = subprocess.check_output(args)
jid1 = str(jid1).split(" ")[3][:-3]
i+=1
print(jid1)

print("submitting job:", i, flush=True)
dep_args = [args[0], args[1], "sleep"+str(i), '--dependency=afterok:'+jid1, args[3]]
jid2 = subprocess.check_output(dep_args)
jid2 = str(jid2).split(" ")[3][:-3]
i+=1
print(dep_args)
print(jid2)

print("submitting job:", i, flush=True)
dep_args = [args[0], args[1], "sleep"+str(i), '--dependency=afterok:'+jid2, args[3]]
jid3 = subprocess.check_output(dep_args)
jid3 = str(jid3).split(" ")[3][:-3]
i+=1
print(dep_args)
print(jid3)

print("submitting job:", i, flush=True)
dep_args = [args[0], args[1], "sleep"+str(i), '--dependency=afterok:'+jid3, args[3]]
jid4 = subprocess.check_output(dep_args)
jid4 = str(jid4).split(" ")[3][:-3]
print(dep_args)
print(jid4)
    





