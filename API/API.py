import requests

class API(object):
	def __init__(self):
		super(API, self).__init__()
		self.headers = {"Authorization": "coegsekali", "Content-Type": "application/json"}
		self.host = "http://localhost:3456"

	def postImage(self, filename, kerapatan, arusInjeksi, algoritma, dataVolt):
		data = '{"nama":"'+filename+'","data": "'+dataVolt+'","algoritma":"'+algoritma+'","kerapatan":"'+str(kerapatan)+'","arus_injeksi":"'+str(arusInjeksi)+'"}'
		url = self.host+'/image'
		response = requests.post(url, data, headers=self.headers)
		print(response.text)

	def postData():
		url = self.host+'/data'
		