import json
import os.path

import src.constants as const

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

class Sheets():

    equips = []
    events = []
    checks = []

    sheetID = ""
    equipsRange = ""
    eventsRange = ""
    checksRange = ""

    currentRange = ""

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
        creds = None
        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', const.SCOPES)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', const.SCOPES)
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

    def Write(self, range, values):
        value_list: list = values
        data = [
            {
                'range':range,
                'values':value_list
            }
        ]
        body = {
            'valueInputOption': "USER_ENTERED",
            'data': data
        }
        result = self.service.spreadsheets().values().batchUpdate(
            spreadsheetId=self.sheetID, body=body
        ).execute()

        print(str(json.loads(result)))

    def Remove(self):
        pass

    def Read(self, range):
        self.currentRange = range
        if self.connected:
            sheet = self.service.spreadsheets()
            result = sheet.values().get(spreadsheetId=self.sheetID,
                                        range=range).execute()
            answer = result.get('values',[])
            return answer
        else:
            return []