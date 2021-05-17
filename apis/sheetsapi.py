import json
import os.path

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

EQUIPS = 0
EVENTS = 1
CHECKS = 2

class Sheets():

    equips = []
    events = []
    checks = []

    sheetID = ""
    equipsRange = ""
    eventsRange = ""
    checksRange = ""

    service = None

    def __init__(self):
        with open('config.json') as testdict:
            c_json = json.loads(testdict.read())

            configs = c_json['configs']

            self.sheetID = configs['sheetID']
            self.equipsRange = configs['eqRNG']
            self.eventsRange = configs['evRNG']
            self.checksRange = configs['chRNG']

            self.connected = False
    
    #Método para abrir conexão com a Database. Deve ser invocado antes de usar a API
    def Connect(self):
        SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

        creds = None
        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            with open('token.json', 'w') as token:
                token.write(creds.to_json())

        self.service = build('sheets', 'v4', credentials=creds)

        self.connected = True

        self.LoadEquips()
        self.LoadEvents()
        self.LoadChecks()

    #Os métodos a seguir devem solicitar as informações à DB e computar elas de forma
    #que os retornos sejam compatíveis com as interfaces criadas. Estes métodos são os
    #mediadores de recepção
    def LoadEquips(self):
        if self.connected:
            sheet = self.service.spreadsheets()
            result = sheet.values().get(spreadsheetId=self.sheetID,
                                        range=self.equipsRange).execute()
            unformatted = result.get('values', [])
            formatted : list = []

            #Tipos! deve retornar as devidas quantidades, como em_uso e defeito nessa planilha são bool
            for i in unformatted:
                item : dict = {}
                item['l_name'] = i[1]
                item['l_id'] = i[0]
                item['l_qtd_tot'] = i[2]
                item['l_qtd_uso'] = i[2]
                item['l_qtd_disp'] = i[3]
                item['l_obs'] = i[4]
                formatted.append(item)

            self.equips = formatted
    
    def LoadEvents(self):
        if self.connected:
            sheet = self.service.spreadsheets()
            result = sheet.values().get(spreadsheetId=self.sheetID,
                                        range=self.eventsRange).execute()
            unformatted = result.get('values', [])
            formatted : list = []
            for i in unformatted:
                item : dict = {}
                item['l_name'] = i[0]
                item['l_start'] = i[1]
                item['l_end'] = i[2]
                item['l_team'] = i[3]
                item['l_check'] = i[4]
                item['l_obs'] = i[5]
                formatted.append(item)

            self.events = formatted

    def LoadChecks(self):
        if self.connected:
            sheet = self.service.spreadsheets()
            result = sheet.values().get(spreadsheetId=self.sheetID,
                                        range=self.checksRange).execute()
            unformatted = result.get('values', [])
            formatted : list = []
            for i in unformatted:
                item : dict = {}
                item['l_name'] = i[0]
                item['l_items'] = i[1]
                formatted.append(item)

            self.checks = formatted

    #Os métodos abaixo retornam os valores carregados e computados previamente
    def GetEquips(self):
        return self.equips

    def GetEvents(self):
        return self.events

    def GetChecks(self):
        return self.checks

    #Os métodos a seguir irão manusear os dados do banco de dados

    def Add(self):
        pass

    def Remove(self):
        pass

    def GetRange(self):
        pass

    def ReadRange(self, range):
        if self.connected:
            sheet = self.service.spreadsheets()
            result = sheet.values().get(spreadsheetId=self.sheetID,
                                        range=range).execute()
            answer = result.get('values',[])
            return answer
        else:
            return []