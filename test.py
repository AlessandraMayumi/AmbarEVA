from flask import redirect, request
import requests
from app import Meteorology, db

"""
b22460a8b91ac5f1d48f5b7029891b53

http://apiadvisor.climatempo.com.br/api/v1/anl/synoptic/locale/BR?token=your-app-token

http://apiadvisor.climatempo.com.br/api/v1/anl/synoptic/locale/BR?token=b22460a8b91ac5f1d48f5b7029891b53

http://apiadvisor.climatempo.com.br/api/v1/forecast/locale/3477/days/15?token=your-app-token
"""
adr = 'http://apiadvisor.climatempo.com.br/api/v1/forecast/locale/3477/days/15?token=b22460a8b91ac5f1d48f5b7029891b53'
r = requests.get(adr)

# new_data = Meteorology(
#     id=r.json()['id'],
#     name=r.json()['name'],
#     state=r.json()['state'],
#     country=r.json()['country'],
#     date=r.json()['data'][0]['date'],
#     probability=r.json()['data'][0]['rain']['probability'],
#     precipitation=r.json()['data'][0]['rain']['precipitation'],
#     temp_min=r.json()['data'][0]['temperature']['min'],
#     temp_max=r.json()['data'][0]['temperature']['max']
# )
#
# try:
#     db.session.add(new_data)
#     db.session.commit()
# except:
#     pass
#
# id_city = '3477'
# db_element = Meteorology.query.filter_by(id=id_city).first()

print(db_element)
# redirect(prefix+id_city+token, code=302)
new_data = Meteorology(id=3476, name='Sao Paulo', state='SP', country=r'Brasil', date='01-01-2020', probability=40, precipitation=20, temp_min=20, temp_max=30)