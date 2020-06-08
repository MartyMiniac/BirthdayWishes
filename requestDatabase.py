import requests
import json

class requestDatabase:
    f = open("token.txt", "r")
    token=f.read()
    def getAll(self):
        url = "https://birthday-bba6.restdb.io/rest/bdaywishes"

        headers = {
            'content-type': "application/json",
            'x-apikey': requestDatabase.token,
            'cache-control': "no-cache"
            }

        response = requests.request("GET", url, headers=headers)

        return json.loads(response.text)
    
    def get(self, id):
        url = "https://birthday-bba6.restdb.io/rest/bdaywishes"+str(id)

        headers = {
            'content-type': "application/json",
            'x-apikey': requestDatabase.token,
            'cache-control': "no-cache"
            }

        response = requests.request("GET", url, headers=headers)
        if response.text == '[]':
            return None
        return json.loads(response.text)
    
    def add(self, name, message):
        url = "https://birthday-bba6.restdb.io/rest/bdaywishes"

        payload = json.dumps( {"name": name,"message": message} )
        headers = {
            'content-type': "application/json",
            'x-apikey': requestDatabase.token,
            'cache-control': "no-cache"
            }

        response = requests.request("POST", url, data=payload, headers=headers)
        rt=json.loads(response.text)
        return rt["_id"]

        response = requests.request("PUT", url, data=payload, headers=headers)
        rt=json.loads(response.text)
        return rt['_id']

    def delete(self, id):
        url = "https://birthday-bba6.restdb.io/rest/bdaywishes/"+id

        headers = {
            'content-type': "application/json",
            'x-apikey': "9d0aa297cf5c817088e69f2c9b13b214ba4a4",
            'cache-control': "no-cache"
            }

        response = requests.request("DELETE", url, headers=headers)
        return response.text

    def getAllId(self):
        js=self.getAll()
        d = []
        for t in js:
            d.append(t['_id'])
        return d

    def len(self):
        c=0;
        js=self.getAll()
        for t in js:
            c=c+1
        return c
