# import the necessary packages
from colordescriptor import ColorDescriptor
from searcher import Searcher
import argparse
import cv2
import os

def generateResult(index, queryPath, resultPath, savePath):
	 
	# initialize the image descriptor
	cd = ColorDescriptor((8, 12, 3))
	# load the query image and describe it
	query = cv2.imread(queryPath)
	features = cd.describe(query)
	 
	# perform the search
	searcher = Searcher(index)
	results = searcher.search(features)
	 
	# display the query
	cv2.imwrite(savePath+"/Query.jpg", query)
	
	i=1 
	f = open(savePath + "/data.txt", 'w')
	# loop over the results
	for (score, resultID) in results:
		# load the result image and display it
		#print(resultID,score)
		f.write(str(resultID) + " : " + str(score)+"\n")

		result = cv2.imread(resultPath + "/" + resultID)
		cv2.imwrite(savePath+"/Result"+str(i)+".jpg", result)
		i=i+1
	f.close()
i=1
for file in os.listdir("query12"):
	directory = "testResult/catalog12/result"+str(i)
	if not os.path.exists(directory):
	    os.makedirs(directory)
	generateResult("testIndex12.csv", "query12/"+file, "cataloges/catalog12", directory)
	i=i+1
