import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.recycleview import RecycleView, RecycleViewBehavior
from kivy.uix.screenmanager import ScreenManager, Screen

kivy.require('2.0.0')

class ScreenWrapper(Screen):
    pass

class Lista(RecycleView):
    pass

#List items

class EquipItem(RecycleViewBehavior, GridLayout):
    pass

class CheckItem(RecycleViewBehavior, GridLayout):
    pass

class EventItem(RecycleViewBehavior, GridLayout):
    pass

#Screens
class StartScr(GridLayout):
    pass

class EquipScr(GridLayout):
    pass

class EventScr(GridLayout):
    pass

class CheckScr(GridLayout):
    pass

class AdminScr(GridLayout):
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
        #Remove widgets desatualizados, se houver
        self.wrapper2.clear_widgets()

        #Adquire o widget atualizado pela função
        eq = self.PopulateEquip()

        #Adiciona do widget atualizado à página em branco
        self.wrapper2.add_widget(eq)

        #Modifica a visualização do usuário para a devida página
        self.mng.current = self.wrapper2.name

    def PressEvents(self, instance):
        #Remove widgets desatualizados, se houver
        self.wrapper3.clear_widgets()
        
        #Adquire o widget atualizado pela função
        event = self.PopulateEvents()

        #Adiciona o widget atualizado à página em branco
        self.wrapper3.add_widget(event)

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

    def PopulateEquip(self):

        itensteste = [
            {'l_name':"1", 'l_id':"SW1"}, 
            {'l_name':"2", 'l_id':"SW2"}, 
            {'l_name':"3", 'l_id':"SW3"}, 
            {'l_name':"Bada", 'l_id':"SW4"}
            ]

        equip = EquipScr()
        equip.ids.back.bind(on_press = self.PressBack)

        eq_ls = Lista()
        eq_ls.viewclass = EquipItem
        eq_ls.data = itensteste

        equip.ids.e_container.add_widget(eq_ls)

        return equip

    def PopulateEvents(self):

        itensteste = [
            {'l_name':"1", 'l_start':"30/04/2021", 'l_end':"31/04/2021"}, 
            {'l_name':"2", 'l_start':"30/04/2021", 'l_end':"31/04/2021"}, 
            {'l_name':"3", 'l_start':"30/04/2021", 'l_end':"31/04/2021"}, 
            {'l_name':"Bada", 'l_start':"30/13/2022", 'l_end':"31/82/2022"}
            ]

        event = EventScr()
        event.ids.back.bind(on_press = self.PressBack)

        ev_ls = Lista()
        ev_ls.viewclass = EventItem
        ev_ls.data = itensteste

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


if __name__ == '__main__':
    Main().run()
