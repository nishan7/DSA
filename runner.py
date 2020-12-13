import subprocess
import os

path = 'D:\\Projects\\DSA\\'



# os.system(' start "" "cmd \k "start server.url && set FLASK_ENV=development && python app.py""')

p = subprocess.Popen('start '+path+'server.url', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
p = subprocess.Popen('set FLASK_ENV=development', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
p = subprocess.Popen('python '+path+'app.py', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
p.wait()
input()
p.terminate()