import subprocess
n=int(input("Enter the number of containers to be run: "))
i=1
while i<=n:
    image=input("Enter a name of the image to be run as a container: ")
    subprocess.call("docker run -it -d %s"%image, shell=True)
    i=i+1

