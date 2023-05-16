import requests
from bs4 import BeautifulSoup
import json

from myapp.models import Sancionatorio


def scrape_sancionatorio(request):
    base_url = 'https://snifa.sma.gob.cl/Sancionatorio/Resultado'
    url = base_url + '?_search=false&nd=123456789&rows=1000&page={}&sidx=id_documento&sord=desc'
    page = 1
    all_data = []

    while True:
        response = requests.get(url.format(page))
        soup = BeautifulSoup(response.content, 'html.parser')
        rows = soup.select('.ui-jqgrid-btable tr')
        if len(rows) == 0:
            break

        for row in rows[1:]:
            columns = row.select('td')
            data = {
                'folio': columns[0].text.strip(),
                'fecha': columns[1].text.strip(),
                'empresa': columns[2].text.strip(),
                'region': columns[3].text.strip(),
                'comuna': columns[4].text.strip(),
            }
            all_data.append(data)

        page += 1

    with open('sancionatorio_data.json', 'w') as f:
        json.dump(all_data, f)

        for data in all_data:
            sancionatorio = Sancionatorio(
                folio=data['folio'],
                fecha=data['fecha'],
                empresa=data['empresa'],
                region=data['region'],
                comuna=data['comuna']
            )
            sancionatorio.save()
