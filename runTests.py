import os
import subprocess
import sys
import string
import time

f = open("output-MCTSAgent.txt", 'w')

start_time = time.time()
proc = subprocess.Popen(["python pacman.py -p MCTSAgent -l smallClassic -q -n 10 -k 1"], stdout=subprocess.PIPE, shell=True)
(out, err) = proc.communicate()
end_time = time.time()
output= "\nMCTSAgent Small Map 1 Ghost------\n"
out=out.decode("utf-8")
execution_time = end_time - start_time
output+=out
output+="\nExecution time:"+ str(execution_time)+ "seconds"
print(output)
f.write(output)

start_time = time.time()
proc = subprocess.Popen(["python pacman.py -p MCTSAgent -l mediumClassic -q -n 10 -k 1"], stdout=subprocess.PIPE, shell=True)
(out, err) = proc.communicate()
end_time = time.time()
output= "\nMCTSAgent Medium Map 1 Ghost------\n"
out=out.decode("utf-8")
execution_time = end_time - start_time
output+=out
output+="\nExecution time:"+ str(execution_time)+ "seconds"
print(output)
f.write(output)

start_time = time.time()
proc = subprocess.Popen(["python pacman.py -p MCTSAgent -l smallClassic -q -n 10 -k 3"], stdout=subprocess.PIPE, shell=True)
(out, err) = proc.communicate()
end_time = time.time()
output= "\nMCTSAgent Small Map 3 Ghost------\n"
out=out.decode("utf-8")
execution_time = end_time - start_time
output+=out
output+="\nExecution time:"+ str(execution_time)+ "seconds"
print(output)
f.write(output)

start_time = time.time()
proc = subprocess.Popen(["python pacman.py -p MCTSAgent -l mediumClassic -q -n 10 -k 3"], stdout=subprocess.PIPE, shell=True)
(out, err) = proc.communicate()
end_time = time.time()
output= "\nMCTSAgent Medium Map 3 Ghost------\n"
out=out.decode("utf-8")
execution_time = end_time - start_time
output+=out
output+="\nExecution time:"+ str(execution_time)+ "seconds"
print(output)
f.write(output)

start_time = time.time()
proc = subprocess.Popen(["python pacman.py -p AlphaBetaAgent -l smallClassic -q -n 10 -k 1"], stdout=subprocess.PIPE, shell=True)
(out, err) = proc.communicate()
end_time = time.time()
output= "\nAlphaBetaAgent Small Map 1 Ghost------\n"
out=out.decode("utf-8")
execution_time = end_time - start_time
output+=out
output+="\nExecution time:"+ str(execution_time)+ "seconds"
print(output)
f.write(output)

start_time = time.time()
proc = subprocess.Popen(["python pacman.py -p AlphaBetaAgent -l mediumClassic -q -n 10 -k 1"], stdout=subprocess.PIPE, shell=True)
(out, err) = proc.communicate()
end_time = time.time()
output= "\nAlphaBetaAgent Medium Map 1 Ghost------\n"
out=out.decode("utf-8")
execution_time = end_time - start_time
output+=out
output+="\nExecution time:"+ str(execution_time)+ "seconds"
print(output)
f.write(output)

start_time = time.time()
proc = subprocess.Popen(["python pacman.py -p AlphaBetaAgent -l smallClassic -q -n 10 -k 3"], stdout=subprocess.PIPE, shell=True)
(out, err) = proc.communicate()
end_time = time.time()
output= "\nAlphaBetaAgent Small Map 3 Ghost------\n"
out=out.decode("utf-8")
execution_time = end_time - start_time
output+=out
output+="\nExecution time:"+ str(execution_time)+ "seconds"
print(output)
f.write(output)

start_time = time.time()
proc = subprocess.Popen(["python pacman.py -p AlphaBetaAgent -l mediumClassic -q -n 10 -k 3"], stdout=subprocess.PIPE, shell=True)
(out, err) = proc.communicate()
end_time = time.time()
output= "\nAlphaBetaAgent Medium Map 3 Ghost------\n"
out=out.decode("utf-8")
execution_time = end_time - start_time
output+=out
output+="\nExecution time:"+ str(execution_time)+ "seconds"
print(output)
f.write(output)

start_time = time.time()
proc = subprocess.Popen(["python pacman.py -p ExpectimaxAgent -l smallClassic -q -n 10 -k 1"], stdout=subprocess.PIPE, shell=True)
(out, err) = proc.communicate()
end_time = time.time()
output= "\nExpectimaxAgent Small Map 1 Ghost------\n"
out=out.decode("utf-8")
execution_time = end_time - start_time
output+=out
output+="\nExecution time:"+ str(execution_time)+ "seconds"
print(output)
f.write(output)

start_time = time.time()
proc = subprocess.Popen(["python pacman.py -p ExpectimaxAgent -l mediumClassic -q -n 10 -k 1"], stdout=subprocess.PIPE, shell=True)
(out, err) = proc.communicate()
end_time = time.time()
output= "\nExpectimaxAgent Medium Map 1 Ghost------\n"
out=out.decode("utf-8")
execution_time = end_time - start_time
output+=out
output+="\nExecution time:"+ str(execution_time)+ "seconds"
print(output)
f.write(output)

start_time = time.time()
proc = subprocess.Popen(["python pacman.py -p ExpectimaxAgent -l smallClassic -q -n 10 -k 3"], stdout=subprocess.PIPE, shell=True)
(out, err) = proc.communicate()
end_time = time.time()
output= "\nExpectimaxAgent Small Map 3 Ghost------\n"
out=out.decode("utf-8")
execution_time = end_time - start_time
output+=out
output+="\nExecution time:"+ str(execution_time)+ "seconds"
print(output)
f.write(output)

start_time = time.time()
proc = subprocess.Popen(["python pacman.py -p ExpectimaxAgent -l mediumClassic -q -n 10 -k 3"], stdout=subprocess.PIPE, shell=True)
(out, err) = proc.communicate()
end_time = time.time()
output= "\nExpectimaxAgent Medium Map 3 Ghost------\n"
out=out.decode("utf-8")
execution_time = end_time - start_time
output+=out
output+="\nExecution time:"+ str(execution_time)+ "seconds"
print(output)
f.write(output)

f.close()