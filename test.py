import subprocess

hostname = "172.16.1.1"

response = subprocess.run('ping '+hostname, stdout=subprocess.DEVNULL) 


if response.returncode == 0:
  print(hostname, 'is up!')
else:
  print(hostname, 'is down!')
