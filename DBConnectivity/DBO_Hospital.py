class objhospital:
    def __init__(self):
        self._hospital_Id = 0
        self._hospital_name = ""
        self._bedcount = 0

    @property
    def hospital_id(self):
        return self._hospital_Id

    @hospital_id.setter
    def hospital_id(self, val):
        self._hospital_Id = val

    @property
    def hospital_name(self):
        return self._hospital_name

    @hospital_name.setter
    def hospital_name(self, val):
        self._hospital_name = val

    @property
    def bedcount(self):
        return self._bedcount

    @bedcount.setter
    def bedcount(self, val):
        self._bedcount = val
