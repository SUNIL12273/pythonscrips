import subprocess

subprocess.call("docker rm -f $(docker ps -aq)", shell=True)

