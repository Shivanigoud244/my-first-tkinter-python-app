from datetime import date
class objdoctor:
    def __init__(self):
        self._doctor_Id = 0
        self._doctor_name = ""
        self._hospital_Id = 0
        self._joining_date = date.today()
        self._speciality = ""
        self._salary = 0.0
        self._experience = ""

    @property
    def doctor_id(self):
        return self._doctor_Id

    @doctor_id.setter
    def doctor_id(self, val):
        self._doctor_Id = val

    @property
    def doctor_name(self):
        return self._doctor_name

    @doctor_name.setter
    def doctor_name(self, val):
        self._doctor_name = val

    @property
    def hospital_id(self):
        return self._hospital_Id

    @hospital_id.setter
    def hospital_id(self, val):
        self._hospital_Id = val

    @property
    def joining_date(self):
        return self._joining_date

    @joining_date.setter
    def joining_date(self, val):
        self._joining_date = val

    @property
    def speciality(self):
        return self._speciality

    @speciality.setter
    def speciality(self, val):
        self._speciality = val

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, val):
        self._salary = val

    @property
    def experience(self):
        return self._experience

    @experience.setter
    def experience(self, val):
        self._experience = val

    @property
    def doctor_id(self):
        return self._doctor_Id

    @doctor_id.setter
    def doctor_id(self, val):
        self._doctor_Id = val
