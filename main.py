import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.recycleview import RecycleView, RecycleViewBehavior
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.properties import BooleanProperty, StringProperty

kivy.require('2.0.0')

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
    pass

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
    pass

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

    #Inicialização das páginas no Screen Manager
    def build(self):
        start = StartScr()
        
        #Atrelando funções aos botões do menu principal
        start.ids.b1.bind(on_press = self.PressEquips)
        start.ids.b2.bind(on_press = self.PressEvents)
        start.ids.b3.bind(on_press = self.PressChecks)
        start.ids.b4.bind(on_press = self.PressAdmin)

        #Adicionando a tela do menu principal ao Screen Manager
        self.wrapper1.add_widget(start)

        #Adicionando as outras páginas (em branco) ao Screen Manager
        self.mng.add_widget(self.wrapper1)
        self.mng.add_widget(self.wrapper2)
        self.mng.add_widget(self.wrapper3)
        self.mng.add_widget(self.wrapper4)
        self.mng.add_widget(self.wrapper5)

        return self.mng

    #Botões do menu principal

    def PressEquips(self, instance):
        items = [
            {'l_name':"Vuze", 'l_id':"SW1", 'l_qtd_tot':"1", 'l_qtd_uso':"1", 'l_qtd_def':"0", 'l_qtd_disp':"0", 'l_obs':"Nada a declarar"},
            {'l_name':"Camera", 'l_id':"SW2", 'l_qtd_tot':"2", 'l_qtd_uso':"1", 'l_qtd_def':"0", 'l_qtd_disp':"1", 'l_obs':"4K"},
            {'l_name':"Projetor", 'l_id':"SW3", 'l_qtd_tot':"3", 'l_qtd_uso':"1", 'l_qtd_def':"0", 'l_qtd_disp':"2", 'l_obs':"Epson"},
            {'l_name':"Cabo", 'l_id':"SW4", 'l_qtd_tot':"10", 'l_qtd_uso':"5", 'l_qtd_def':"3", 'l_qtd_disp':"2", 'l_obs':"HDMI"},
            {'l_name':"Caixa", 'l_id':"SW5", 'l_qtd_tot':"4", 'l_qtd_uso':"2", 'l_qtd_def':"1", 'l_qtd_disp':"1", 'l_obs':"Turbo"}, 
            ]
        #Adquire o widget atualizado pela função
        eq = self.PopulateEquip(items)
        self.wrapper2.items = items

        #Adiciona do widget atualizado à página em branco
        self.wrapper2.set_widget(eq)

        #Modifica a visualização do usuário para a devida página
        self.mng.current = self.wrapper2.name

    def PressEvents(self, instance):
        items = [
            {'l_name':"1", 'l_start':"30/04/2021", 'l_end':"31/04/2021", 'l_team':"Rena", 'l_check':"None", 'l_obs': "Turbo"}, 
            {'l_name':"2", 'l_start':"30/04/2021", 'l_end':"31/04/2021", 'l_team':"Bada", 'l_check':"Other", 'l_obs': "Blaster"}, 
            {'l_name':"3", 'l_start':"30/04/2021", 'l_end':"31/04/2021", 'l_team':"Rena", 'l_check':"KTC", 'l_obs': "Master"}, 
            {'l_name':"Bada", 'l_start':"30/13/2022", 'l_end':"31/82/2022", 'l_team':"Gabriel", 'l_check':"None", 'l_obs': "Leviousa"}
            ]        
        #Adquire o widget atualizado pela função
        event = self.PopulateEvents(items)

        #Adiciona o widget atualizado à página em branco
        self.wrapper3.set_widget(event)

        #Modifica a visualização do usuário para a devida página
        self.mng.current = self.wrapper3.name

    def PressChecks(self, instance):
        #Remove widgets desatualizados, se houver
        self.wrapper4.clear_widgets()
        
        #Adquire o widget atualizado pela função
        check = self.PopulateCheck()

        #Adiciona o widget atualizado à página em branco
        self.wrapper4.add_widget(check)

        #Modifica a visualização do usuário para a devida página
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

    def PopulateCheck(self):

        itensteste = [
            {'l_name':"1", 'l_items':"2"}, 
            {'l_name':"2", 'l_items':"3"}, 
            {'l_name':"3", 'l_items':"4"}, 
            {'l_name':"Bada", 'l_items':"5"}
            ]

        check = CheckScr()
        check.ids.back.bind(on_press = self.PressBack)

        ch_ls = Lista()
        ch_ls.viewclass = CheckItem
        ch_ls.data = itensteste

        check.ids.c_container.add_widget(ch_ls)

        return check

    #funções de outros botões
    def PressEqSearch(self, instance):
        equip: EquipScr
        scr = self.mng.current_screen
        equip = scr.widget

        equip.pesquisar = equip.ids.i_pesquisado.text

        items = self.PressSearch(equip.pesquisar, scr.items)

        new_equip = self.PopulateEquip(items)

        self.wrapper2.set_widget(new_equip)

    #funções em geral
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
