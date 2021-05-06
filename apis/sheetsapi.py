class Sheets():

    #Os métodos a seguir devem solicitar as informações à DB e computar elas de forma
    #que os retornos sejam compatíveis com as interfaces criadas. Estes métodos são os
    #mediadores de recepção
    def GetEquips():
        equips = [
            {'l_name':"Vuze", 'l_id':"SW1", 'l_qtd_tot':"1", 'l_qtd_uso':"1", 'l_qtd_def':"0", 'l_qtd_disp':"0", 'l_obs':"Nada a declarar"},
            {'l_name':"Camera", 'l_id':"SW2", 'l_qtd_tot':"2", 'l_qtd_uso':"1", 'l_qtd_def':"0", 'l_qtd_disp':"1", 'l_obs':"4K"},
            {'l_name':"Projetor", 'l_id':"SW3", 'l_qtd_tot':"3", 'l_qtd_uso':"1", 'l_qtd_def':"0", 'l_qtd_disp':"2", 'l_obs':"Epson"},
            {'l_name':"Cabo", 'l_id':"SW4", 'l_qtd_tot':"10", 'l_qtd_uso':"5", 'l_qtd_def':"3", 'l_qtd_disp':"2", 'l_obs':"HDMI"},
            {'l_name':"Caixa", 'l_id':"SW5", 'l_qtd_tot':"4", 'l_qtd_uso':"2", 'l_qtd_def':"1", 'l_qtd_disp':"1", 'l_obs':"Turbo"}, 
            ]

        return equips
    
    def GetEvents():
        events = [
            {'l_name':"1", 'l_start':"30/04/2021", 'l_end':"31/04/2021", 'l_team':"Rena", 'l_check':"None", 'l_obs': "Turbo"}, 
            {'l_name':"2", 'l_start':"30/04/2021", 'l_end':"31/04/2021", 'l_team':"Bada", 'l_check':"Other", 'l_obs': "Blaster"}, 
            {'l_name':"3", 'l_start':"30/04/2021", 'l_end':"31/04/2021", 'l_team':"Rena", 'l_check':"KTC", 'l_obs': "Master"}, 
            {'l_name':"Bada", 'l_start':"30/13/2022", 'l_end':"31/82/2022", 'l_team':"Gabriel", 'l_check':"None", 'l_obs': "Leviousa"}
            ]     

        return events

    def GetChecks():
        checks = [
            {'l_name':"1", 'l_items':"2"}, 
            {'l_name':"2", 'l_items':"3"}, 
            {'l_name':"3", 'l_items':"4"}, 
            {'l_name':"Bada", 'l_items':"5"}
            ]

        return checks