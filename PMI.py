import subprocess
n=int(input("Enter the number of images to be downloaded: "))
i=1
while i<=n:
    image=input("Enter a name of the image: ")
    subprocess.call("docker pull %s"%image, shell=True)
    i=i+1
