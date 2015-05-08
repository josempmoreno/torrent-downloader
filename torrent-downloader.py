import os
import urllib
import glob
import shutil


dirTmp='tmp'
dirOut='torrents'
end=80000
j=0

def checkDirectories():
	if not os.path.exists(dirTmp):
		os.mkdir(dirTmp) 

	if not os.path.exists(dirOut):
		os.mkdir(dirOut) 

def downloadFile(i):
	#get file from url
	urllib.urlretrieve("http://tumejorjuego.com/download/index.php?link=descargar-torrent/0"+str(i)+"_torrent.torrent", filename=dirTmp+"/index.php?link=descargar-torrent%2F0"+str(i)+"_torrent.torrent")
	#generate name
	namefile = '/index.php?link=descargar-torrent%2F0'+str(i)+'_torrent.torrent' 
	return namefile   

def getStartNumber():
	if len(os.listdir(dirOut)) > 0:
		newest = max(glob.iglob(dirOut+'/*.torrent'), key=os.path.getctime)		
		numberstart = newest[newest.find('/')+1:newest.find('-')]
	else:
		numberstart = 50000
	return numberstart

def getNameFromFile(dirTmp,namefile):
	f = open(dirTmp+namefile)		
	data=f.read()
	initialPositionName = data.find('name')
	finalPositionName= data.find('12:piece')
	name=data[initialPositionName+7:finalPositionName]
	name=str(i)+"-"+name
	return name

checkDirectories()
start = getStartNumber()

for i in range(int(start),end):    
	try:
		namefile = downloadFile(i)
		name = getNameFromFile(dirTmp,namefile)
		
		if len(name) > 150:			
			#is a html file
			os.remove(dirTmp+namefile)
			j+=1
			if j == 50:	
				shutil.rmtree(dirTmp)			
				break
		else:
			j=0
			print name
			#rename and move file to dirOut
			os.rename(dirTmp+namefile,dirOut+"/"+name+'.torrent')
			
	except OSError:
		print "Oops!  This file is not a torrent"
		break
	except IOError:
		print "Oops!  This file not exist, check your connection"
		break

		




