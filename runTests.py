import os
import subprocess
import sys
import string

f = open("output4.txt", 'w')

proc = subprocess.Popen(["python pacman.py -p MCTSAgent -l smallClassic -q -n 5"], stdout=subprocess.PIPE, shell=True)
(out, err) = proc.communicate()
output= "MCTSAgent Small Map------\n"
out=out.decode("utf-8")
output+=out
print(output)
f.write(output)

proc = subprocess.Popen(["python pacman.py -p MCTSAgent -l mediumClassic -q -n 5"], stdout=subprocess.PIPE, shell=True)
(out, err) = proc.communicate()
output= "\nMCTSAgent Medium Map------\n"
out=out.decode("utf-8")
output+=out
print(output)
f.write(output)

proc = subprocess.Popen(["python pacman.py -p MCTSAgent -l originalClassic -q -n 2"], stdout=subprocess.PIPE, shell=True)
(out, err) = proc.communicate()
output= "\nMCTSAgent Original Map------\n"
out=out.decode("utf-8")
output+=out
print(output)
f.write(output)

proc = subprocess.Popen(["python pacman.py -p ImprovedMCTSAgent -l smallClassic -q -n 5"], stdout=subprocess.PIPE, shell=True)
(out, err) = proc.communicate()
output= "ImprovedMCTSAgent Small Map------\n"
out=out.decode("utf-8")
output+=out
print(output)
f.write(output)

proc = subprocess.Popen(["python pacman.py -p ImprovedMCTSAgent -l mediumClassic -q -n 5"], stdout=subprocess.PIPE, shell=True)
(out, err) = proc.communicate()
output= "\nImprovedMCTSAgent Medium Map------\n"
out=out.decode("utf-8")
output+=out
print(output)
f.write(output)

proc = subprocess.Popen(["python pacman.py -p ImprovedMCTSAgent -l originalClassic -q -n 2"], stdout=subprocess.PIPE, shell=True)
(out, err) = proc.communicate()
output= "\nImprovedMCTSAgent Original Map------\n"
out=out.decode("utf-8")
output+=out
print(output)
f.write(output)

proc = subprocess.Popen(["python pacman.py -p AlphaBetaAgent -l smallClassic -q -n 20"], stdout=subprocess.PIPE, shell=True)
(out, err) = proc.communicate()
output= "\nAlphaBetaAgent Small Map------\n"
out=out.decode("utf-8")
output+=out
print(output)
f.write(output)

proc = subprocess.Popen(["python pacman.py -p AlphaBetaAgent -l mediumClassic -q -n 15"], stdout=subprocess.PIPE, shell=True)
(out, err) = proc.communicate()
output= "\nAlphaBetaAgent Medium Map------\n"
out=out.decode("utf-8")
output+=out
print(output)
f.write(output)

proc = subprocess.Popen(["python pacman.py -p AlphaBetaAgent -l originalClassic -q -n 5"], stdout=subprocess.PIPE, shell=True)
(out, err) = proc.communicate()
output= "\nAlphaBetaAgent Original Map------\n"
out=out.decode("utf-8")
output+=out
print(output)
f.write(output)

proc = subprocess.Popen(["python pacman.py -p ExpectimaxAgent -l smallClassic -q -n 20"], stdout=subprocess.PIPE, shell=True)
(out, err) = proc.communicate()
output= "\nExpectimaxAgent Small Map------\n"
out=out.decode("utf-8")
output+=out
print(output)
f.write(output)

proc = subprocess.Popen(["python pacman.py -p ExpectimaxAgent -l mediumClassic -q -n 15"], stdout=subprocess.PIPE, shell=True)
(out, err) = proc.communicate()
output= "\nExpectimaxAgent Medium Map------\n"
out=out.decode("utf-8")
output+=out
print(output)
f.write(output)

proc = subprocess.Popen(["python pacman.py -p ExpectimaxAgent -l originalClassic -q -n 5"], stdout=subprocess.PIPE, shell=True)
(out, err) = proc.communicate()
output= "\nExpectimaxAgent Original Map------\n"
out=out.decode("utf-8")
output+=out
print(output)
f.write(output)
f.close()
