import json

import kivy
from kivy.config import Config
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.recycleview import RecycleView, RecycleViewBehavior
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.properties import BooleanProperty, StringProperty
from apis.sheetsapi import Sheets
import src.constants as const

kivy.require('2.0.0')

Config.set('graphics', 'width', '300')
Config.set('graphics', 'height', '600')
Config.set('graphics', 'resizable', False)

class ScreenWrapper(Screen):
    def __init__(self, **kwargs):
        super(ScreenWrapper,self).__init__(**kwargs)
        self.widget: Widget
        self.items: list

    def set_widget(self, widget):
        self.clear_widgets()
        self.widget = widget
        self.add_widget(widget)

class Lista(RecycleView):
    pass

#List items

class EquipItem(RecycleViewBehavior, GridLayout):
    touchable = BooleanProperty(True)

    l_name = StringProperty("")
    l_id = StringProperty("")
    l_qtd_tot = StringProperty("")
    l_qtd_uso = StringProperty("")
    l_qtd_def = StringProperty("")
    l_qtd_disp = StringProperty("")
    l_obs = StringProperty("")

    def __init__(self, **kwargs):
        super(EquipItem, self).__init__(**kwargs)
        self.app = App.get_running_app()
        self.equip = Equipamento()

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.equip.ids.i_item_id.text = self.l_id
            self.equip.ids.i_item_name.text = self.l_name
            self.equip.ids.i_item_qttot.text = self.l_qtd_tot
            self.equip.ids.i_item_qtuso.text = self.l_qtd_uso
            self.equip.ids.i_item_qtdef.text = self.l_qtd_def
            self.equip.ids.i_item_qtdis.text = self.l_qtd_disp
            self.equip.ids.i_item_obs.text = self.l_obs

            self.equip.ids.back_from_item.bind(on_press = self.PressBack)

            root = self.app.wrapper2
            root.clear_widgets()
            root.add_widget(self.equip)

    def PressBack(self, instance):
        root = self.app.wrapper2
        root.clear_widgets()
        root.add_widget(root.widget)
        self.equip.ids.i_item_id.text = ""
        self.equip.ids.i_item_name.text = ""
        self.equip.ids.i_item_qttot.text = ""
        self.equip.ids.i_item_qtuso.text = ""
        self.equip.ids.i_item_qtdef.text = ""
        self.equip.ids.i_item_qtdis.text = ""
        self.equip.ids.i_item_obs.text = ""

class CheckItem(RecycleViewBehavior, GridLayout):
    touchable = BooleanProperty(True)

    l_name = StringProperty("")
    l_items = StringProperty("")

    def __init__(self, **kwargs):
        super(CheckItem, self).__init__(**kwargs)
        self.app = App.get_running_app()
        self.check = Checklist()

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.check.ids.i_check_name.text = self.l_name
            self.check.ids.i_check_items.text = self.l_items #l_items IDS must be stringed afterwards

            self.check.ids.back_from_item.bind(on_press = self.PressBack)

            root = self.app.wrapper4
            root.clear_widgets()
            root.add_widget(self.check)

    def PressBack(self, instance):
        root = self.app.wrapper4
        root.clear_widgets()
        root.add_widget(root.widget)
        self.check.ids.i_check_name.text = ""
        self.check.ids.i_check_items.text = ""

class EventItem(RecycleViewBehavior, GridLayout):
    touchable = BooleanProperty(True)

    #interface items
    l_name = StringProperty("")
    l_start = StringProperty("")
    l_end = StringProperty("")

    #detail items
    l_team = StringProperty("")
    l_check = StringProperty("")
    l_obs = StringProperty("")

    def __init__(self, **kwargs):
        super(EventItem, self).__init__(**kwargs)
        self.app = App.get_running_app()
        self.event = Evento()

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.event.ids.i_event_name.text = self.l_name
            self.event.ids.i_event_start.text = self.l_start
            self.event.ids.i_event_end.text = self.l_end
            self.event.ids.i_event_team.text = self.l_team
            self.event.ids.i_event_check.text = self.l_check
            self.event.ids.i_event_obs.text = self.l_obs

            self.event.ids.back_from_item.bind(on_press = self.PressBack)

            root = self.app.wrapper3
            root.clear_widgets()
            root.add_widget(self.event)

    def PressBack(self, instance):
        root = self.app.wrapper3
        root.clear_widgets()
        root.add_widget(root.widget)
        self.event.ids.i_event_name.text = ""
        self.event.ids.i_event_start.text = ""
        self.event.ids.i_event_end.text = ""
        self.event.ids.i_event_team.text = ""
        self.event.ids.i_event_check.text = ""
        self.event.ids.i_event_obs.text = ""


#Screens
class StartScr(GridLayout):
    pass

class EquipScr(GridLayout):
    def __init__(self, **kwargs):
        super(EquipScr,self).__init__(**kwargs)
        self.pesquisar = ""
        self.items = []


class EventScr(GridLayout):
    pass

class CheckScr(GridLayout):
    pass

class AdminScr(GridLayout):
    configs : dict = {}

    def __init__(self, **kwargs):
        super(AdminScr, self).__init__(**kwargs)
        with open('config.json','r')as config_file:
            filestr = json.loads(config_file.read())
            self.configs = filestr['configs']

        self.ids.a_id.text = self.configs['sheetID']
        self.ids.a_eqrng.text = self.configs['eqRNG']
        self.ids.a_evrng.text = self.configs['evRNG']
        self.ids.a_chrng.text = self.configs['chRNG']

        self.ids.b_ok.bind(on_touch_down = self.PressOk)

    def Ok_check(self):
        check : bool = False

        if self.ids.a_id.text and self.ids.a_eqrng.text and self.ids.a_evrng.text and self.ids.a_chrng.text:
            check = True
        else:
            check = False

        return check

    def PressOk(self, instance, args):
        app = App.get_running_app()

        if self.Ok_check():
            to_write = self.configs
            to_write['sheetID'] = self.ids.a_id.text
            to_write['eqRNG'] = self.ids.a_eqrng.text
            to_write['evRNG'] = self.ids.a_evrng.text
            to_write['chRNG'] = self.ids.a_chrng.text
            to_write['init'] = "1"

            writeable = {}
            writeable['configs'] = to_write

            with open('config.json','w') as config_file:
                config_file.write(json.dumps(writeable))

        else:
            print("Sem todos os dados")

        with open('config.json','r') as config_file:
            filestr = json.loads(config_file.read())
            app.configs = filestr['configs']


class Equipamento(GridLayout):
    pass

class Evento(GridLayout):
    pass

class Checklist(GridLayout):
    pass

#Main method
class Main(App):
    mng = ScreenManager()

    wrapper1 = ScreenWrapper(name = 'Main')
    wrapper2 = ScreenWrapper(name = 'Equipamentos')
    wrapper3 = ScreenWrapper(name = 'Eventos')
    wrapper4 = ScreenWrapper(name = 'Checklists')
    wrapper5 = ScreenWrapper(name = 'Admin')

    configs : dict = {}
    init = const.init_test

    #for debug purposes
    #path = os.path.dirname(os.path.abspath(__file__))
    #print(path)

    #Inicializa????o das p??ginas no Screen Manager
    def build(self):

        #O software ir?? criar um arquivo de configura????o para o usu??rio, caso ele n??o exista
        try:
            open('config.json','x')
            with open('config.json','w')as config_file:
                config_file.write(json.dumps(self.init))
                filestr = json.loads(config_file.read())
                self.configs = filestr['configs']
        except:
            print("Arquivo j?? existe")
            with open('config.json','r') as config_file:
                filestr = json.loads(config_file.read())
                self.configs = filestr['configs']
        
        self.db = Sheets()

        start = StartScr()
        
        #Atrelando fun????es aos bot??es do menu principal
        #Checa-se primeiro se o arquivo de configura????o possui as vari??veis de usu??rio necess??rias
        if(self.configs['init'] == "0"):
            #Caso contr??rio, apenas o bot??o 'Admin' ser?? ativado para que o usu??rio inclua as vari??veis
            start.ids.b4.bind(on_press = self.PressAdmin)
        else:
            self.db.Connect()

            start.ids.b1.bind(on_press = self.PressEquips)
            start.ids.b2.bind(on_press = self.PressEvents)
            start.ids.b3.bind(on_press = self.PressChecks)
            start.ids.b4.bind(on_press = self.PressAdmin)

        #Adicionando a tela do menu principal ao Screen Manager
        self.wrapper1.add_widget(start)

        #Adicionando as outras p??ginas (em branco) ao Screen Manager
        self.mng.add_widget(self.wrapper1)
        self.mng.add_widget(self.wrapper2)
        self.mng.add_widget(self.wrapper3)
        self.mng.add_widget(self.wrapper4)
        self.mng.add_widget(self.wrapper5)

        return self.mng

    #Bot??es do menu principal

    def PressEquips(self, instance):
        items = self.db.GetEquips()

        #Adquire o widget atualizado pela fun????o
        eq = self.PopulateEquip(items)
        self.wrapper2.items = items

        #Adiciona do widget atualizado ?? p??gina em branco
        self.wrapper2.set_widget(eq)

        #Modifica a visualiza????o do usu??rio para a devida p??gina
        self.mng.current = self.wrapper2.name

    def PressEvents(self, instance):
        items = self.db.GetEvents()

        #Adquire o widget atualizado pela fun????o
        event = self.PopulateEvents(items)

        #Adiciona o widget atualizado ?? p??gina em branco
        self.wrapper3.set_widget(event)

        #Modifica a visualiza????o do usu??rio para a devida p??gina
        self.mng.current = self.wrapper3.name

    def PressChecks(self, instance):
        items = self.db.GetChecks()
        
        #Adquire o widget atualizado pela fun????o
        check = self.PopulateCheck(items)

        #Adiciona o widget atualizado ?? p??gina em branco
        self.wrapper4.set_widget(check)

        #Modifica a visualiza????o do usu??rio para a devida p??gina
        self.mng.current = self.wrapper4.name

    def PressAdmin(self, instance):
        #Remove widgets desatualizados, se houver
        self.wrapper5.clear_widgets()
        admin = AdminScr()
        admin.ids.back.bind(on_press = self.PressBack)
        self.wrapper5.add_widget(admin)
        self.mng.current = self.wrapper5.name

    def PressBack(self, instance):
        self.mng.current = self.wrapper1.name

    #popular listas

    def PopulateEquip(self, itens):

        itensteste = itens

        equip = EquipScr()
        equip.ids.back.bind(on_press = self.PressBack)

        eq_ls = Lista()
        eq_ls.viewclass = EquipItem
        eq_ls.data = itensteste

        equip.ids.e_container.add_widget(eq_ls)
        equip.ids.b_pesquisar.bind(on_press = self.PressEqSearch)

        return equip

    def PopulateEvents(self, itens):

        event = EventScr()
        event.ids.back.bind(on_press = self.PressBack)

        ev_ls = Lista()
        ev_ls.viewclass = EventItem
        ev_ls.data = itens

        event.ids.v_container.add_widget(ev_ls)

        return event

    def PopulateCheck(self, itens):

        check = CheckScr()
        check.ids.back.bind(on_press = self.PressBack)

        ch_ls = Lista()
        ch_ls.viewclass = CheckItem
        ch_ls.data = itens

        check.ids.c_container.add_widget(ch_ls)

        return check

    #fun????es de outros bot??es
    def PressEqSearch(self, instance):
        equip: EquipScr
        scr = self.mng.current_screen
        equip = scr.widget

        equip.pesquisar = equip.ids.i_pesquisado.text

        items = self.PressSearch(equip.pesquisar, scr.items)

        new_equip = self.PopulateEquip(items)

        self.wrapper2.set_widget(new_equip)

    #fun????es em geral
    def PressSearch(self, term, items):
        term: str
        items: list = items

        result = []

        for i in items:
            if i['l_name'].find(term) != -1 or i['l_id'].find(term) != -1:
                result.append(i)

        print(result)

        if len(result) > 0:
            return result
        else:
            return items


if __name__ == '__main__':
    Main().run()
