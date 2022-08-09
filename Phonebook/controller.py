import modul 
import view 
from logger import writer


def combiner():
   name = modul.get_name()
   writer (f'имя/name: {name}\n')
   surname = modul.get_surname()
   writer(f'фамилия/surname: {surname}\n')
   num = modul.number()
   writer(f'номер телефона/phone number: {num}\n/--------конец записи--------\ \n')
   view.get_information(data_1 = {name}, data_2 = {surname}, number= {num})


   