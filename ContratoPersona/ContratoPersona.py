class ContratoPersona:
    def __init__(self,id=None,idpersona=None,idcontrato=None) -> None:
        self._id = id
        self._idpersona = idpersona
        self._idcontrato = idcontrato


    @property
    def idcontrato(self):
        return self._idcontrato
    @property
    def idpersona(self):
        return self._idpersona
    @property
    def idcontrato(self):
        return self._idcontrato

    def __str__(self) -> str:
        return f"\nID ContraPer: {self._id} \nID Contrato: {self._idpersona} \nID Contrato: {self._idcontrato}"

