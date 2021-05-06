import json

class Sheets():

    equips = []
    events = []
    checks = []

    def __init__(self):
        with open('config.json') as testdict:
            testjson = json.loads(testdict.read())
            teststrings = testjson['teste']
            self.equips = teststrings['equips']
            self.events = teststrings['events']
            self.checks = teststrings['checks']

    #Os métodos a seguir devem solicitar as informações à DB e computar elas de forma
    #que os retornos sejam compatíveis com as interfaces criadas. Estes métodos são os
    #mediadores de recepção
    def GetEquips(self):
        return self.equips
    
    def GetEvents(self):
        return self.events

    def GetChecks(self):
        return self.checks