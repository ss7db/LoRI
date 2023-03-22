import time
import SInf
import numpy
# import SInf
# import Game
# import subprocess
# # from sys import stdout
# import tempfile
# # from sys import stdout
# cmd = ['python', '--version']
# print(subprocess.Popen(cmd, stdout))
# output = subprocess.Popen(cmd, stdout =subprocess.PIPE).communicate()[0]
# print(output)
# from subprocess import run
# output = run("python --version", capture_output=True).stdout
# subprocess.Po
# with tempfile.TemporaryFile() as tempf:
#     proc = subprocess.Popen(cmd, stdout=tempf)
#     proc.wait()
#     tempf.seek(0)
#     print(tempf.read())
# t = int(time.time())

# t = [19.850864197530864, 19.850864197530864, 19.850864197530864, 19.850864197530864, 19.850864197530864]
# # s = [23.003703703703703, 23.0, 23.0]
# x = sum(t)
# # y = sum(s)
# print(x/len(t))

lt = []
for i in numpy.arange(0,1,0.1):
    lt.append(SInf.activeInactive(i))
    print(lt)