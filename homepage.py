import datetime
import tkinter
from tkinter import *
from tkinter import Label
import numpy as np
import matplotlib.pyplot as plt

from tkcalendar import Calendar, DateEntry

from DBConnectivity import DML_DBOperations as hosp_doc_db_name_space
from DBConnectivity import DBO_Hospital
from DBConnectivity import DBO_Doctor
from styles import configuration

hp = Tk()
hp.geometry("600x300")
hp.title("Doctors and Hospitals Information")
frame_home = Frame(hp)
frame_home.pack()


def graph():
    doc_db_object = hosp_doc_db_name_space.db_class()
    doc_detail_data_list = doc_db_object.read_doctors_fulllist()
    """doctor = ['Ridhvika Goud K', 'Raja Rushender Goud K', 'Narasimha Murthy K', 'Shivani Goud G A', 'Simon Praveen Kumar C', 'Anil Kumar Goud G S', 'Fernaz das', 'Nandan Rao', 'Carien Tray', 'RiChard Z']
    hospital = [124, 124, 121, 121, 121, 122, 124, 125, 125, 121]"""
    doctor=[]
    hospital =[]
    for x in doc_detail_data_list:
        hospital.append(x[4])
        doctor.append(x[1])

    #hospital = list(dict.fromkeys(hospital))
    print(hospital)
    print(doctor)

    plt.plot(hospital,doctor,'ro')
    plt.xlabel('Speciality')
    plt.ylabel('Doctor')

    plt.show()


def forget_frames():
    for frame in configuration.active_frame:
        frame.pack_forget()
    configuration.active_frame.clear()


def only_numeric_input(P):
    # checks if entry's value is an integer or empty and returns an appropriate boolean
    if P.isdigit():  # if a digit was entered or nothing was entered
        return True
    elif P == "":
        return True
    return False


def only_string_input(P):
    # checks if entry's value is an integer or empty and returns an appropriate boolean
    if P is not None or re.match("^[a-z]*$", P):
        return True
    return False


def func_insert_hosp_details(hospIdval, hospNamVal, bedcountval):
    forget_frames()
    hosp_class_obj_details = DBO_Hospital.objhospital
    insert_hosp_details_frame = Frame(hp)
    insert_hosp_details_frame.pack(side=TOP)
    configuration.active_frame.append(insert_hosp_details_frame)
    hosp_class_obj_details._hospital_Id = int(hospIdval)
    hosp_class_obj_details._hospital_name = hospNamVal
    hosp_class_obj_details._bedcount = int(bedcountval)
    hosp_insert_db_object = hosp_doc_db_name_space.db_class()
    result = hosp_insert_db_object.insert_hospital_details(hosp_class_obj_details)
    print(result)
    Label(insert_hosp_details_frame, text=result).grid(row=0, column=0)


def func_insert_doc_details(docIdVal, docName, hospIdval, specVal, salaryVal, expVal, dateofjoin):
    forget_frames()
    doc_class_obj_details = DBO_Doctor.objdoctor
    insert_doc_details_frame = Frame(hp)
    insert_doc_details_frame.pack(side=TOP)
    configuration.active_frame.append(insert_doc_details_frame)
    doc_class_obj_details._hospital_Id = int(hospIdval)
    doc_class_obj_details._doctor_Id = int(docIdVal)
    doc_class_obj_details._doctor_name = docName
    doc_class_obj_details._joining_date = datetime.datetime.strptime(dateofjoin, '%Y-%m-%d')
    doc_class_obj_details._speciality = specVal
    doc_class_obj_details._salary = salaryVal
    doc_class_obj_details._experience = expVal
    doc_insert_db_object = hosp_doc_db_name_space.db_class()
    result = doc_insert_db_object.insert_doctor_details(doc_class_obj_details)
    print(result)
    Label(insert_doc_details_frame, text=result).grid(row=0, column=0)


def func_update_hosp_detail(hosp_id_val, hosp_name_val, bed_count_val):
    forget_frames()
    update_hosp_detail_by_hospital_id_frame = Frame(hp)
    hosp_class_object = DBO_Hospital.objhospital
    update_hosp_detail_by_hospital_id_frame.pack(side=TOP)
    configuration.active_frame.append(update_hosp_detail_by_hospital_id_frame)

    hosp_class_object._hospital_Id = int(hosp_id_val)
    hosp_class_object._hospital_name = hosp_name_val
    hosp_class_object._bedcount = int(bed_count_val)
    hosp_update_db_object = hosp_doc_db_name_space.db_class()
    result = hosp_update_db_object.update_hospital_details(hosp_class_object)
    print(result)
    Label(update_hosp_detail_by_hospital_id_frame, text=result).grid(row=0, column=0)


def func_update_doc_detail(doc_id_val, doc_name_val, hosp_id_val, join_date_val, spec_val, sal_val, exp_val):
    forget_frames()
    update_doc_detail_by_hospital_id_frame = Frame(hp)
    doc_class_object = DBO_Doctor.objdoctor
    update_doc_detail_by_hospital_id_frame.pack(side=TOP)
    configuration.active_frame.append(update_doc_detail_by_hospital_id_frame)
    doc_class_object._doctor_Id = int(doc_id_val)
    doc_class_object._doctor_name = doc_name_val
    doc_class_object._hospital_Id = int(hosp_id_val)
    doc_class_object._joining_date = datetime.datetime.strptime(join_date_val, '%Y-%m-%d')
    doc_class_object._speciality = spec_val
    doc_class_object._salary = sal_val
    doc_class_object._experience = exp_val
    hosp_update_db_object = hosp_doc_db_name_space.db_class()
    result = hosp_update_db_object.update_doctor_details(doc_class_object)
    print(result)
    Label(update_doc_detail_by_hospital_id_frame, text=result).grid(row=0, column=0)


def func_delete_hosp_detail_db(hosp_id_val):
    forget_frames()
    delete_hosp_detail_by_hospital_id_frame = Frame(hp)
    delete_hosp_detail_by_hospital_id_frame.pack(side=TOP)
    configuration.active_frame.append(delete_hosp_detail_by_hospital_id_frame)
    hosp_delete_db_object = hosp_doc_db_name_space.db_class()
    result = hosp_delete_db_object.delete_hospital_detail_by_hospital_id(int(hosp_id_val))
    print(result)
    Label(delete_hosp_detail_by_hospital_id_frame, text=result).grid(row=0, column=0)


def func_delete_doc_detail_db(doc_id_val):
    forget_frames()
    delete_doc_detail_by_hospital_id_frame = Frame(hp)
    delete_doc_detail_by_hospital_id_frame.pack(side=TOP)
    configuration.active_frame.append(delete_doc_detail_by_hospital_id_frame)
    doc_delete_db_object = hosp_doc_db_name_space.db_class()
    result = doc_delete_db_object.delete_doctor_detail_by_hospital_id(int(doc_id_val))
    print(result)
    Label(delete_doc_detail_by_hospital_id_frame, text=result).grid(row=0, column=0)


def func_get_doctor_full_list():
    forget_frames()
    doc_full_list_frame = Frame(hp)
    doc_full_list_frame.pack(side=TOP)
    configuration.active_frame.append(doc_full_list_frame)
    doctor_db_object = hosp_doc_db_name_space.db_class()
    dfl = doctor_db_object.read_doctors_fulllist()
    if dfl is not None:
        y = 1
        Label(doc_full_list_frame, text="Doctor ID").grid(row=0, column=0)
        Label(doc_full_list_frame, text="Doctor Name").grid(row=0, column=1)
        Label(doc_full_list_frame, text="Hospital ID").grid(row=0, column=2)
        Label(doc_full_list_frame, text="Joining Date").grid(row=0, column=3)
        Label(doc_full_list_frame, text="Speciality").grid(row=0, column=4)
        Label(doc_full_list_frame, text="Salary").grid(row=0, column=5)
        Label(doc_full_list_frame, text="Experience").grid(row=0, column=6)
        for p in dfl:
            Label(doc_full_list_frame, text=str(p[0])).grid(row=y, column=0)
            Label(doc_full_list_frame, text=str(p[1])).grid(row=y, column=1)
            Label(doc_full_list_frame, text=str(p[2])).grid(row=y, column=2)
            Label(doc_full_list_frame, text=str(p[3])).grid(row=y, column=3)
            Label(doc_full_list_frame, text=str(p[4])).grid(row=y, column=4)
            Label(doc_full_list_frame, text=str(p[5])).grid(row=y, column=5)
            Label(doc_full_list_frame, text=str(p[6])).grid(row=y, column=6)
            y = y + 1


def func_get_hospital_full_list():
    forget_frames()
    hosp_full_list_frame = Frame(hp)
    hosp_full_list_frame.pack(side=TOP)
    configuration.active_frame.append(hosp_full_list_frame)

    hosp_db_object = hosp_doc_db_name_space.db_class()
    hfl = hosp_db_object.read_hospital_fulllist()
    if hfl is not None:
        y = 1
        Label(hosp_full_list_frame, text="Hospital ID").grid(row=0, column=0)
        Label(hosp_full_list_frame, text="Hospital Name").grid(row=0, column=1)
        Label(hosp_full_list_frame, text="Bed Count").grid(row=0, column=2)

        for p in hfl:
            Label(hosp_full_list_frame, text=str(p[0])).grid(row=y, column=0)
            Label(hosp_full_list_frame, text=str(p[1])).grid(row=y, column=1)
            Label(hosp_full_list_frame, text=str(p[2])).grid(row=y, column=2)
            y = y + 1


def func_get_hosp_detail_by_hospital_id(hosp_id):
    forget_frames()
    update_hosp_detail_by_id_frame = Frame(hp)
    update_hosp_detail_by_id_frame.pack(side=TOP)
    configuration.active_frame.append(update_hosp_detail_by_id_frame)

    hosp_db_object = hosp_doc_db_name_space.db_class()
    hosp_detail_data_list = hosp_db_object.read_hospital_details(hosp_id)
    if hosp_detail_data_list is not None:
        Label(update_hosp_detail_by_id_frame, text="Hospital ID").grid(row=0, column=0)
        Label(update_hosp_detail_by_id_frame, text="Hospital Name").grid(row=1, column=0)
        Label(update_hosp_detail_by_id_frame, text="Bedcount").grid(row=2, column=0)
        Label(update_hosp_detail_by_id_frame, text=str(hosp_detail_data_list._hospital_Id)).grid(row=0, column=1)
        upe1 = tkinter.StringVar()
        upe2 = tkinter.StringVar()
        e1 = Entry(update_hosp_detail_by_id_frame, text=upe1)
        e1.grid(row=1, column=1)
        upe1.set(hosp_detail_data_list._hospital_name)
        e2 = Entry(update_hosp_detail_by_id_frame, text=upe2)
        e2.grid(row=2, column=1)
        upe2.set(str(hosp_detail_data_list._bedcount))
        Button(update_hosp_detail_by_id_frame, text="update",
               command=lambda: func_update_hosp_detail(hosp_detail_data_list._hospital_Id, e1.get(), e2.get())).grid(
            row=3,
            column=0)


def func_get_doc_detail_by_hospital_id(doc_id):
    forget_frames()
    update_doc_detail_by_id_frame = Frame(hp)
    update_doc_detail_by_id_frame.pack(side=TOP)
    configuration.active_frame.append(update_doc_detail_by_id_frame)

    doc_db_object = hosp_doc_db_name_space.db_class()
    doc_detail_data_list = doc_db_object.read_doctor_details(doc_id)
    if doc_detail_data_list is not None:
        Label(update_doc_detail_by_id_frame, text="Doctor ID").grid(row=0, column=0)
        Label(update_doc_detail_by_id_frame, text="Doctor Name").grid(row=1, column=0)
        Label(update_doc_detail_by_id_frame, text="Hospital").grid(row=2, column=0)
        Label(update_doc_detail_by_id_frame, text="Joining Date").grid(row=3, column=0)
        Label(update_doc_detail_by_id_frame, text="Specialization").grid(row=4, column=0)
        Label(update_doc_detail_by_id_frame, text="Salary").grid(row=5, column=0)
        Label(update_doc_detail_by_id_frame, text="Experience").grid(row=6, column=0)
        Label(update_doc_detail_by_id_frame, text=str(doc_detail_data_list._doctor_Id)).grid(row=0, column=1)
        upe1 = tkinter.StringVar()
        # upe2 = tkinter.StringVar()
        e1 = Entry(update_doc_detail_by_id_frame, text=upe1)
        e1.grid(row=1, column=1)
        upe1.set(doc_detail_data_list._doctor_name)
        # e2 = Entry(update_doc_detail_by_id_frame, text=upe2)
        # e2.grid(row=2, column=1)

        OptionList = []
        hosp_db_object = hosp_doc_db_name_space.db_class()
        hfl = hosp_db_object.read_hospital_fulllist()

        if hfl is not None:
            for x in hfl:
                OptionList.append(str(x[0]) + ", \t" + str(x[1]))

        variable = StringVar(update_doc_detail_by_id_frame)
        variable.set("Select Hospital")

        opt = OptionMenu(update_doc_detail_by_id_frame, variable, *OptionList)
        opt.config()
        opt.grid(row=2, column=1)

        # upe2.set(str(doc_detail_data_list._hospital_Id))
        # upe3 = tkinter.StringVar()
        upe4 = tkinter.StringVar()
        # e3 = Entry(update_doc_detail_by_id_frame, text=upe3)
        # e3.grid(row=3, column=1)
        # upe3.set(doc_detail_data_list._joining_date)
        cal = DateEntry(update_doc_detail_by_id_frame, width=12, background='darkblue',
                        foreground='white', borderwidth=2, locale='en_US', date_pattern='y-mm-dd')
        cal.grid(row=3, column=1)
        e4 = Entry(update_doc_detail_by_id_frame, text=upe4)
        e4.grid(row=4, column=1)
        upe4.set(str(doc_detail_data_list._speciality))
        upe5 = tkinter.StringVar()
        upe6 = tkinter.StringVar()
        e5 = Entry(update_doc_detail_by_id_frame, text=upe5)
        e5.grid(row=5, column=1)
        upe5.set(doc_detail_data_list._salary)
        e6 = Entry(update_doc_detail_by_id_frame, text=upe6)
        e6.grid(row=6, column=1)
        upe6.set(str(doc_detail_data_list._experience))
        Button(update_doc_detail_by_id_frame, text="update",
               command=lambda: func_update_doc_detail(doc_detail_data_list._doctor_Id, e1.get(),
                                                      variable.get().partition(",")[0], cal.get(),
                                                      e4.get(), e5.get(), e6.get())).grid(row=7, column=0)


def func_hosp_update_get_hospital_id():
    forget_frames()
    update_hosp_detail_get_hospital_id_frame = Frame(hp)
    update_hosp_detail_get_hospital_id_frame.pack(side=TOP)
    configuration.active_frame.append(update_hosp_detail_get_hospital_id_frame)
    Label(update_hosp_detail_get_hospital_id_frame, text="Update Hospital Details").grid(row=0, column=0)
    hospital_id = Label(update_hosp_detail_get_hospital_id_frame, text="Hospital Id")
    hospital_id.grid(row=1, column=0)
    e1 = Entry(update_hosp_detail_get_hospital_id_frame)
    e1.grid(row=1, column=1)
    Button(update_hosp_detail_get_hospital_id_frame, text="Submit",
           command=lambda: func_get_hosp_detail_by_hospital_id(e1.get())).grid(row=4, column=0)


def func_doc_update_get_hospital_id():
    forget_frames()
    update_doc_detail_get_hospital_id_frame = Frame(hp)
    update_doc_detail_get_hospital_id_frame.pack(side=TOP)
    configuration.active_frame.append(update_doc_detail_get_hospital_id_frame)
    Label(update_doc_detail_get_hospital_id_frame, text="Update Doctor Details").grid(row=0, column=0)
    hospital_id = Label(update_doc_detail_get_hospital_id_frame, text="Doctor Id")
    hospital_id.grid(row=1, column=0)
    e1 = Entry(update_doc_detail_get_hospital_id_frame)
    e1.grid(row=1, column=1)
    Button(update_doc_detail_get_hospital_id_frame, text="Submit",
           command=lambda: func_get_doc_detail_by_hospital_id(e1.get())).grid(row=4, column=0)


def func_hosp_delete_get_hospital_id():
    forget_frames()
    delete_hosp_detail_get_hospital_id_frame = Frame(hp)
    delete_hosp_detail_get_hospital_id_frame.pack(side=TOP)
    configuration.active_frame.append(delete_hosp_detail_get_hospital_id_frame)
    Label(delete_hosp_detail_get_hospital_id_frame, text="Delete Hospital Details").grid(row=0, column=0)
    hospital_id = Label(delete_hosp_detail_get_hospital_id_frame, text="Hospital Id")
    hospital_id.grid(row=1, column=0)
    e1 = Entry(delete_hosp_detail_get_hospital_id_frame)
    e1.grid(row=1, column=1)
    reg = delete_hosp_detail_get_hospital_id_frame.register(only_numeric_input)
    e1.config(validate="key", validatecommand=(reg, '%P'))
    Button(delete_hosp_detail_get_hospital_id_frame, text="Submit",
           command=lambda: func_delete_hosp_detail_db(e1.get())).grid(row=4, column=0)


def func_doc_delete_get_hospital_id():
    forget_frames()
    delete_doc_detail_get_hospital_id_frame = Frame(hp)
    delete_doc_detail_get_hospital_id_frame.pack(side=TOP)
    configuration.active_frame.append(delete_doc_detail_get_hospital_id_frame)
    Label(delete_doc_detail_get_hospital_id_frame, text="Delete Doctor Details").grid(row=0, column=0)
    doctor_id = Label(delete_doc_detail_get_hospital_id_frame, text="Doctor Id")
    doctor_id.grid(row=1, column=0)
    e1 = Entry(delete_doc_detail_get_hospital_id_frame)
    e1.grid(row=1, column=1)
    reg = delete_doc_detail_get_hospital_id_frame.register(only_numeric_input)
    e1.config(validate="key", validatecommand=(reg, '%P'))
    Button(delete_doc_detail_get_hospital_id_frame, text="Submit",
           command=lambda: func_delete_doc_detail_db(e1.get())).grid(row=4, column=0)


def func_hosp_add_details():
    forget_frames()
    hosp_add_details_frame = Frame(hp)
    hosp_add_details_frame.pack(side=TOP)
    configuration.active_frame.append(hosp_add_details_frame)

    Label(hosp_add_details_frame, text="Add Hospital Details").grid(row=0, column=0)
    hospital_id = Label(hosp_add_details_frame, text="Hospital Id")
    hospital_id.grid(row=1, column=0)
    e1 = Entry(hosp_add_details_frame)
    e1.grid(row=1, column=1)
    hosp_name = Label(hosp_add_details_frame, text="Hospital Name")
    hosp_name.grid(row=2, column=0)
    e2 = Entry(hosp_add_details_frame)
    e2.grid(row=2, column=1)
    bed_count = Label(hosp_add_details_frame, text="Bed Count")
    bed_count.grid(row=3, column=0)
    e3 = Entry(hosp_add_details_frame)
    e3.grid(row=3, column=1)
    Button(hosp_add_details_frame, text="Submit",
           command=lambda: func_insert_hosp_details(e1.get(), e2.get(), e3.get())).grid(row=4, column=0)
    Button(hosp_add_details_frame, text="Cancel", command=lambda: func_get_doctor_full_list()).grid(row=4,
                                                                                                    column=1)


def func_doc_add_details():
    forget_frames()
    doc_add_details_frame = Frame(hp)
    doc_add_details_frame.pack(side=TOP)
    configuration.active_frame.append(doc_add_details_frame)
    Label(doc_add_details_frame, text="Add Doctor Details").grid(row=0, column=0)
    doctor_id = Label(doc_add_details_frame, text="Doctor Id")
    doctor_id.grid(row=1, column=0)
    e1 = Entry(doc_add_details_frame)
    e1.grid(row=1, column=1)
    doctor_name = Label(doc_add_details_frame, text="Doctor Name")
    doctor_name.grid(row=2, column=0)
    e2 = Entry(doc_add_details_frame)
    e2.grid(row=2, column=1)

    hospital_id = Label(doc_add_details_frame, text="Hospital")
    hospital_id.grid(row=3, column=0)
    # e3 = Entry(doc_add_details_frame)
    # e3.grid(row=3, column=1)
    OptionList = []
    hosp_db_object = hosp_doc_db_name_space.db_class()
    hfl = hosp_db_object.read_hospital_fulllist()

    if hfl is not None:
        for x in hfl:
            OptionList.append(str(x[0]) + ", \t" + str(x[1]))

    variable = StringVar(doc_add_details_frame)
    variable.set("Select Hospital")

    opt = OptionMenu(doc_add_details_frame, variable, *OptionList)
    opt.config()
    opt.grid(row=3, column=1)

    specialization = Label(doc_add_details_frame, text="Speciality")
    specialization.grid(row=4, column=0)
    e4 = Entry(doc_add_details_frame)
    e4.grid(row=4, column=1)
    salary = Label(doc_add_details_frame, text="Salary")
    salary.grid(row=5, column=0)
    e5 = Entry(doc_add_details_frame)
    e5.grid(row=5, column=1)
    experience = Label(doc_add_details_frame, text="Experience")
    experience.grid(row=6, column=0)
    e6 = Entry(doc_add_details_frame)
    e6.grid(row=6, column=1)
    dateofJoining: Label = Label(doc_add_details_frame, text="Date of Joining")
    dateofJoining.grid(row=7, column=0)
    # e7 = Entry(doc_add_details_frame)
    # e7.grid(row=7, column=1)
    cal = DateEntry(doc_add_details_frame, width=12, background='darkblue',
                    foreground='white', borderwidth=2, locale='en_US', date_pattern='y-mm-dd')
    cal.grid(row=7, column=1)
    """docIdVal, docName, hospIdval, specVal, salaryVal, expVal, dateofjoin"""
    Button(doc_add_details_frame, text="Submit",
           command=lambda: func_insert_doc_details(e1.get(), e2.get(), variable.get().partition(",")[0], e4.get(),
                                                   e5.get(), e6.get(),
                                                   cal.get())).grid(row=8, column=0)
    Button(doc_add_details_frame, text="Cancel", command=lambda: func_get_doctor_full_list()).grid(row=8,
                                                                                                   column=1)


def func_db_version():
    forget_frames()
    db_version_frame = Frame(hp)
    db_version_frame.pack(side=TOP)
    configuration.active_frame.append(db_version_frame)
    db_version_object = hosp_doc_db_name_space.db_class()

    output = db_version_object.read_db_version()
    Label(db_version_frame, text="DB Version").grid(row=0, column=0)
    Label(db_version_frame, text=str(output)).grid(row=1, column=0)


menu_bar_list = Menu(hp)
doc = Menu(menu_bar_list, tearoff=0)
doc.add_command(label="List", command=func_get_doctor_full_list)
doc.add_command(label="Add", command=func_doc_add_details)
doc.add_command(label="Update", command=func_doc_update_get_hospital_id)
doc.add_command(label="Delete", command=func_doc_delete_get_hospital_id)

menu_bar_list.add_cascade(label="Doctor", menu=doc)

hosp = Menu(menu_bar_list, tearoff=0)
hosp.add_command(label="List", command=func_get_hospital_full_list)
hosp.add_command(label="Add", command=func_hosp_add_details)
hosp.add_command(label="Update", command=func_hosp_update_get_hospital_id)
hosp.add_command(label="Delete", command=func_hosp_delete_get_hospital_id)

menu_bar_list.add_cascade(label="Hospital", menu=hosp)

dbv = Menu(menu_bar_list, tearoff=0)
dbv.add_command(label="DB Version", command=func_db_version)

menu_bar_list.add_cascade(label="DB Version", menu=dbv)

pl = Menu(menu_bar_list, tearoff=0)
pl.add_command(label="Graphs", command=graph)

menu_bar_list.add_cascade(label="Graphs", menu=pl)

search_bar = Entry(menu_bar_list)
search_button = Button(menu_bar_list, text="Cancel")
search_button.pack()

hp.config(menu=menu_bar_list)

hp.mainloop()
