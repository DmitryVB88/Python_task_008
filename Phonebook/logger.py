from pathlib import Path
from datetime import datetime as dt
from time import time

def writer(data: str) -> None:
     time = dt.now().strftime('%H:%M')
     print(f'{data}\n')
     filepath = Path('PhoneBook', 'NP', 'PhonBook.csv')
     with open(filepath, 'a', encoding='utf-8') as file:
          file.write(f'\n{time}, {data}') 

         