
import pandas as pd
import json
import urllib2


def download_nordpool(limit, output_file):
	'''
	The method downloads the nordpool available data from www.energidataservice.dk and saves it in a csv file

	limit: Int, the number of maximum rows of data to download 
	output_file: Str, the name of the output file
	'''

	url = 'https://api.energidataservice.dk/datastore_search?resource_id=8bd7a37f-1098-4643-865a-01eb55c62d21&limit=' + str(limit)
	print("downloading nordpool data ...")
	fileobj = urllib2.urlopen(url)
	data = json.loads(fileobj.read())
	nordpool_df = pd.DataFrame.from_dict(data['result']['records']) # the data is stored inside two dictionaries
	nordpool_df.to_csv(output_file)
	print("nordpool data has been downloaded and saved")


def download_dayforward(limit, output_file):
	'''
	The method downloads the available day ahead spotprices in DK and neighboring countries data 
	from www.energidataservice.dk and saves it in a csv file

	limit: Int, the number of maximum rows of data to download 
	output_file: Str, the name of the output file
	'''

	url = 'https://api.energidataservice.dk/datastore_search?resource_id=c86859d2-942e-4029-aec1-32d56f1a2e5d&limit=' + str(limit)
	print("downloading day forward data ...")
	fileobj = urllib2.urlopen(url)
	data = json.loads(fileobj.read())
	nordpool_df = pd.DataFrame.from_dict(data['result']['records']) # the data is stored inside two dictionaries
	nordpool_df.to_csv(output_file)
	print("day forward data has been downloaded and saved")


if __name__ == '__main__':
	print("connecting with the API")
	download_nordpool(10000000, 'nordpool_data.csv')
	download_dayforward(10000000, 'dayforward_data.csv')