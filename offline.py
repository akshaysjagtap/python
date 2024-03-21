import os, sys

print("Offline downloading packages for "+sys.argv[1]+"...\n")
os.system("apt-rdepends "+sys.argv[1]+" -v 2> /dev/null > list.txt")

if os.path.exists("list.txt") == True:
	filePkgList = open("list.txt", "r")
	setPkgs = set()
	
	for line in filePkgList:
		line=line.strip()
		
		if line.startswith("node: "): 
			setPkgs.add(line.split("\"")[1])
		elif line.startswith("edge: "):
			setPkgs.add(line.split("\"")[3])
	
	setPkgs=sorted(setPkgs)
	
	for pkg in setPkgs:
		print("Downloading package: "+pkg+"...")
		os.system("apt download " + pkg + " 2> /dev/null")
		print()
		
	os.system("mkdir -p debpkgs")
	os.system("mv *.deb debpkgs")	
