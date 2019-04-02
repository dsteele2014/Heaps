import csv
import math

class dataSorter():
	def __init__(self):
			self.latList = []
			self.longList = []
			self.newLatList = []
			self.newLongList = []

	def csvReader(self):
			with open('cs455_project3_Sliger_Steele.csv') as csvfile:
				reader = csv.DictReader(csvfile)
				for row in reader:
						self.latList.append(row['latitude'])
						self.longList.append(row['longitude'])

	def csvWriter(self):
			with open('temp.csv','w') as csvfile:
				writera = csv.writer(csvfile,
                            quotechar='|', quoting=csv.QUOTE_MINIMAL,lineterminator='\n')

				for i in self.newLongList:
						writera.writerow([i])

	def generalizeLat(self):
			for i in self.latList:
					if float(i) < 40.63000:
						self.newLatList.append("<40.63000")
					elif float(i) > 40.76000:
						self.newLatList.append(">40.76000")
					else:
						self.newLatList.append("40.63000...40.76000")

	def generalizeLong(self):
			for i in self.longList:
					if float(i) < -74.07000:
						self.newLongList.append("<-74.07000")
					elif float(i) > -73.89000:
						self.newLongList.append(">-73.89000")						
					else:
						self.newLongList.append("-74.07000...-73.89000")
		
dataSorter = dataSorter()
dataSorter.csvReader()
dataSorter.generalizeLong()
dataSorter.csvWriter()
