import subprocess
image=input("Enter a name of the image to be deleted: ")
subprocess.call("docker rmi %s"%image, shell=True)

