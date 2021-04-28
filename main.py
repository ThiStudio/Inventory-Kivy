import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen

kivy.require('2.0.0')

class ScreenWrapper(Screen):
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

    def build(self):
        start = StartScr()
        equip = EquipScr()
        event = EventScr()
        check = CheckScr()
        admin = AdminScr()
        
        #atrelando funções aos botões
        start.ids.b1.bind(on_press = self.PressEquips)
        start.ids.b2.bind(on_press = self.PressEvents)
        start.ids.b3.bind(on_press = self.PressChecks)
        start.ids.b4.bind(on_press = self.PressAdmin)
        
        equip.ids.back.bind(on_press = self.PressBack)
        
        event.ids.back.bind(on_press = self.PressBack)
        
        check.ids.back.bind(on_press = self.PressBack)

        admin.ids.back.bind(on_press = self.PressBack)

        self.wrapper1.add_widget(start)
        self.wrapper2.add_widget(equip)
        self.wrapper3.add_widget(event)
        self.wrapper4.add_widget(check)
        self.wrapper5.add_widget(admin)

        self.mng.add_widget(self.wrapper1)
        self.mng.add_widget(self.wrapper2)
        self.mng.add_widget(self.wrapper3)
        self.mng.add_widget(self.wrapper4)
        self.mng.add_widget(self.wrapper5)

        return self.mng

    #botões do menu

    def PressEquips(self, instance):
        self.mng.current = self.wrapper2.name
        print("Botão: <%s>" % instance.text)

    def PressEvents(self, instance):
        self.mng.current = self.wrapper3.name
        print("Botão: <%s>" % instance.text)

    def PressChecks(self, instance):
        self.mng.current = self.wrapper4.name
        print("Botão: <%s>" % instance.text)

    def PressAdmin(self, instance):
        self.mng.current = self.wrapper5.name
        print("Botão: <%s>" % instance.text)

    def PressBack(self, instance):
        self.mng.current = self.wrapper1.name
        print("Voltando ao início...")


if __name__ == '__main__':
    Main().run()
