from coapthon.client.helperclient import HelperClient

client = HelperClient(server=('192.168.137.157', 5683))
response = client.get('/temperature')
print(	response.payload)
client.stop()

