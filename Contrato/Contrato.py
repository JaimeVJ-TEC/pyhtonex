class Contrato:
    def __init__(self,idcontrato=None,nocontrato=None,costo=None,fechainicio=None, fechafin=None) -> None:
        self._idcontrato = idcontrato
        self._nocontrato = nocontrato
        self._costo = costo
        self._fechainicio = fechainicio
        self._fechafin = fechafin
        

    @property
    def idcontrato(self):
        return self._idcontrato
    @property
    def nocontrato(self):
        return self._nocontrato
    @property
    def costo(self):
        return self._costo
    @property
    def fechainicio(self):
        return self._fechainicio
    @property
    def fechafin(self):
        return self._fechafin
   

    def __str__(self) -> str:
        return f"\nId Contrato: {self._idcontrato} \nNo. contrato: {self._nocontrato} \nCosto: {self._costo} \nFecha inicio: {self._fechainicio}\nFecha fin: {self.fechafin}\n"

