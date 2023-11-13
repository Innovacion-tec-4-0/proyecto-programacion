class Tipotramite():
    idTramite = 0
    tipode_tramite = 0
    def __init__(self, idTramite, tipode_tramite):
        self.idTramite = Tipotramite.getidTramite()
        self.tipode_tramite = Tipotramite.gettipode_tramite
    
    def getidTramite(self):
        return self.idTramite
    def gettipode_tramite(self):
        return self.tipode_tramite
    
    def  setidTramite(self, idTramite):
        self.idTramite= idTramite

    def  settipode_tramite(self, tipode_tramite):
        self.tipode_tramite = tipode_tramite
