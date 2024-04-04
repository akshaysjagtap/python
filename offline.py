import os, sys

setMainPkg=set()
print("\nOffline downloading packages for "+sys.argv[1]+"...\n")

def rdepends():
	setPkgs = set()
	
	os.system("apt-rdepends "+sys.argv[1]+" -v 2> /dev/null > list.txt")
	
	if os.path.exists("list.txt") == True:
		filePkgList = open("list.txt", "r")
		
		for line in filePkgList:
			line=line.strip()
			
			if line.startswith("node: "): 
				setPkgs.add(line.split("\"")[1])
			elif line.startswith("edge: "):
				setPkgs.add(line.split("\"")[3])
				
		filePkgList.close()
	
	return setPkgs
		
def funcPkgList(pkgName):
	os.system("apt-cache depends "+pkgName+" > list.txt")
	
	setPkgs = set()
	
	if os.path.exists("list.txt") == True:
		filePkgList = open("list.txt", "r")
		
		for line in filePkgList:
			line=line.strip()
			
			if line.startswith("Depends: "):
				pos = line.find(" ") 
				if pos > -1:
					line=line[pos+1:]
					if line[0] != "<":
						setPkgs.add(line)
		
		filePkgList.close()
	
	return setPkgs

setTemp=set()
setTemp=setMainPkg=funcPkgList(sys.argv[1])
	
while True:
	setDummy=set()

	for setMem in setTemp:
		setDummy.update(funcPkgList(setMem))
	
	if (len(setDummy) == 0) or (setTemp == setDummy):
		break
	else:
		setMainPkg.update(setDummy)
		setTemp = setDummy

setMainPkg.update(rdepends())

for pkg in setMainPkg:
	print("Downloading package: "+pkg+"...")
	os.system("apt download " + pkg + " 2> /dev/null")		
