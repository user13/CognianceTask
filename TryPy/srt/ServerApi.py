import json
import requests

class ServerApi:
    #showAll
    def showAll(self):
        r = requests.get('http://qainterview.cogniance.com/candidates')
        return r

    #showById
    def showById(self, idt):
        r = requests.get('http://qainterview.cogniance.com/candidates/' + str(idt))
        return r
    
    #addById
    def add(self, name, position):
        headers = {'content-type': 'application/json', }
        payload = {'name' : str(name), 'position' : str(position)}
        r = requests.post('http://qainterview.cogniance.com/candidates', data=json.dumps(payload), headers=headers)
        return r

    #delete
    def delete(self, idt):
        r = requests.delete('http://qainterview.cogniance.com/candidates/' + str(idt))
        return r  
            