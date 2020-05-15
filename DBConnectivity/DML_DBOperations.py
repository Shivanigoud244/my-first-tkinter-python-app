from DBConnectivity import DBConnection
from DBConnectivity import DBO_Doctor as OBJDoctor
from DBConnectivity import DBO_Hospital as OBJHospital
from mysql.connector.errors import Error
from datetime import datetime, date


class db_class():

    def __init__(self):
        self.mycon = DBConnection.con

    def __del__(self):
        print("db_class class object is deleted")

    def __str__(self):
        return "DB Object"

    def close_db_connection(self):
        self.mycon.close()

    def read_db_version(self):

        try:

            cur = self.mycon.cursor()
            cur.execute("select version()")
            result = cur.fetchall()
            return result

        except Error as err:
            return err.msg + "/" + err.errno

    def read_doctor_details(self, doctor_id):
        try:

            cur = self.mycon.cursor()
            sql = "select * from MT_Doctor where Doctor_Id =%s"
            cur.execute(sql, (doctor_id,))
            doc_detail = cur.fetchone()
            if doc_detail:
                objdoc = OBJDoctor.objdoctor
                objdoc._doctor_Id = int(doc_detail[0])
                objdoc._doctor_name = doc_detail[1]
                objdoc._hospital_Id = int(doc_detail[2])
                if doc_detail[3] is not None:
                    objdoc._joining_date = doc_detail[3]
                else:
                    objdoc._joining_date = None
                objdoc._speciality = doc_detail[4]
                objdoc._salary = float(doc_detail[5])
                objdoc._experience = doc_detail[6]

                return objdoc
            else:
                return None
        except Error as err:
            # return err.msg + "/" + err.errno
            print(err.msg)

    def read_doctors_fulllist(self):
        try:

            cur = self.mycon.cursor()
            sql = "select * from MT_Doctor"
            cur.execute(sql)
            doc_details = cur.fetchall()
            if doc_details:
                return doc_details
            else:
                return None
        except Error as err:
            # return err.msg + "/" + err.errno
            print(err.msg)

    def read_doctor_details_Speciality(self, speciality, salary):
        try:

            cur = self.mycon.cursor()
            sql = "select * from MT_Doctor where Speciality  =%s and Salary > %s"
            cur.execute(sql, (speciality, salary,))
            doc_details = cur.fetchall()
            if doc_details:
                return doc_details
            else:
                return None
        except Error as err:
            # return err.msg + "/" + err.errno
            print(err.msg)

    def read_doctor_details_WithinHospital(self, hospital_id):
        try:

            cur = self.mycon.cursor()
            sql = "select * from MT_Doctor where Hospital_Id  =%s"
            cur.execute(sql, (hospital_id,))
            doc_details = cur.fetchall()
            if doc_details:
                return doc_details
            else:
                return None
        except Error as err:
            # return err.msg + "/" + err.errno
            print(err.msg)

    def read_hospital_details(self, hospital_id):
        try:

            cur = self.mycon.cursor()
            sql = "select * from MT_Hospital where Hospital_Id = %s"
            cur.execute(sql, (hospital_id,))
            hosp_detail = cur.fetchone()
            if hosp_detail:

                objhos = OBJHospital.objhospital
                objhos._hospital_Id = int(hosp_detail[0])
                objhos._hospital_name = hosp_detail[1]
                objhos._bedcount = int(hosp_detail[2])
                return objhos
            else:
                return None
        except Error as err:
            # return err.msg + "/" + err.errno
            return None

    def read_hospital_fulllist(self):
        try:

            cur = self.mycon.cursor()
            sql = "select * from MT_Hospital "
            cur.execute(sql)
            hosp_details = cur.fetchall()
            if hosp_details:
                return hosp_details
            else:
                return None
        except Error as err:
            # return err.msg + "/" + err.errno
            return None

    def insert_doctor_details(self, insrtdoc):
        try:
            cur = self.mycon.cursor()
            sql = "insert into MT_Doctor (Doctor_Id,Doctor_Name,Hospital_Id,Joining_Date,Speciality,Salary,Experience) " \
                  "values (%s , %s , %s , %s ,%s, %s , %s) "
            val = (insrtdoc._doctor_Id, insrtdoc._doctor_name, insrtdoc._hospital_Id, insrtdoc._joining_date,
                   insrtdoc._speciality, insrtdoc._salary, insrtdoc._experience)
            cur.execute(sql, val)
            self.mycon.commit()
            return "Record inserted successfully"
            # print("Success")
        except Error as err:
            return err.msg + "/" + err.errno
            self.mycon.rollback()
            # print(err.msg)

    def insert_hospital_details(self, insrthosp):
        try:
            cur = self.mycon.cursor()
            print(insrthosp._hospital_Id, insrthosp._hospital_name, insrthosp._bedcount)
            sql = "insert into MT_Hospital (Hospital_Id,Hospital_Name,Bed_Count) " \
                  "values (%s , %s , %s) "
            val = (insrthosp._hospital_Id, insrthosp._hospital_name, insrthosp._bedcount)
            cur.execute(sql, val)
            self.mycon.commit()
            return "Record Inserted Successfully"
        except Error as err:
            # return err.msg + "/" + err.errno
            self.mycon.rollback()
            return err.msg

    def update_doctor_details(self, insrtdoc):
        try:
            cur = self.mycon.cursor()
            sql = "update MT_Doctor SET  Doctor_Name=%s, Hospital_Id=%s, Joining_Date=%s, Speciality = " \
                  "%s, Salary =%s , Experience =%s   Where Doctor_Id = %s "
            val = (insrtdoc._doctor_name, insrtdoc._hospital_Id, insrtdoc._joining_date,
                   insrtdoc._speciality, insrtdoc._salary, insrtdoc._experience, insrtdoc._doctor_Id,)
            cur.execute(sql, val)
            self.mycon.commit()
            return "Record updated successfully"
        except Error as err:
            return err.msg + "/" + err.errno
            self.mycon.rollback()
            # print(err.msg)

    def update_hospital_details(self, insrthosp):
        try:
            cur = self.mycon.cursor()
            sql = "update MT_Hospital SET  Hospital_Name=%s, Bed_Count = %s   Where Hospital_Id = %s "
            val = (insrthosp._hospital_name, insrthosp._bedcount, insrthosp._hospital_Id,)
            cur.execute(sql, val)
            self.mycon.commit()
            return "Record got updated Successfully"
        except Error as err:
            # return err.msg + "/" + err.errno
            self.mycon.rollback()
            return err.msg

    def delete_hospital_detail_by_hospital_id(self, hospital_id_val):
        try:
            "delete  from MT_Hospital where Hospital_Id = 130"
            cur = self.mycon.cursor()
            sql = "delete  from MT_Hospital where Hospital_Id = %s"
            val = (hospital_id_val,)
            cur.execute(sql, val)
            self.mycon.commit()
            return "Record got deleted Successfully"
        except Error as err:
            # return err.msg + "/" + err.errno
            self.mycon.rollback()
            return err.msg

    def delete_doctor_detail_by_hospital_id(self, doctor_id_val):
        try:

            cur = self.mycon.cursor()
            sql = "delete  from MT_Doctor where Doctor_Id = %s"
            val = (doctor_id_val,)
            cur.execute(sql, val)
            self.mycon.commit()
            return "Record got deleted Successfully"
        except Error as err:
            # return err.msg + "/" + err.errno
            self.mycon.rollback()
            return err.msg
