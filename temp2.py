from pandas import DataFrame
import requests
from bs4 import BeautifulSoup

'''      Dont Delete     it is linked    '''

def get_details(name):
    details = []
    all_heading = []
    list_of_details = ["quarters", "profit-loss", "balance-sheet", "cash-flow", "ratios"]
    type_of_AR = ['/','/consolidated/']
    for data in range(0,len(list_of_details)):
        for x in range(0, len(type_of_AR)):
            URL = str('https://www.screener.in/company/')+str(name)+type_of_AR[x]

            page = requests.get(URL)
            soup = BeautifulSoup(page.content, 'html.parser')

            results = soup.find(id= str(list_of_details[data]))
            # results = soup.find(id='quarters')
            table = results.find('table', attrs={'class':'data-table responsive-text-nowrap'})
            rows = table.find_all("tr")
            table_contents = []  # store your table here
            for tr in rows:
                if rows.index(tr) == 0:
                    row_cells = [th.getText().strip() for th in tr.find_all('th') if th.getText().strip() != '']
                else:
                    row_cells = ([tr.find('th').getText()] if tr.find('th') else []) + [td.getText().strip() for td in
                                                                                        tr.find_all('td') if
                                                                                        td.getText().strip() != '']
                if len(row_cells) > 1:
                    table_contents += [row_cells]
            # print(table_contents)
            heading_name = ["time"]
            try:
                table_contents_updated =[table_contents[0]]
                for z in range(1, len(table_contents)):
                    table_contents_updated.append(table_contents[z][1:])
                    che = table_contents[z][0]
                    che = che.split(" %")[0]
                    che = che.split("+")[0]
                    che = che.rstrip()
                    heading_name.append(che)
                # details.append(table_contents)
                df = DataFrame(table_contents_updated).transpose()
                df.columns = [heading_name]
                # print(df)
                details.append(df)
                all_heading.append(heading_name)
            except:
                pass
    All_data =[]
    list_of_details_twice = []
    for twice in list_of_details:
        list_of_details_twice.append(twice)
        list_of_details_twice.append(twice)

    # print(len(details))
    for y in range(0, len(details)):
        temp = details[y]
        head = temp.columns.values.tolist()
        head_new = []
        for new in head:
            head_new.append(''.join(new))

        if len(details) == len(list_of_details):
            catogory = "Standalone"
            fin_type = list_of_details[y]
        else:
            no = y + 1
            if (no % 2) == 0:
                catogory = "Consolidated"
                fin_type = list_of_details_twice[y]
            else:
                catogory = "Standalone"
                fin_type = list_of_details_twice[y]
        for yy in range(0, len(head)):
            each_col = [fin_type, catogory, head_new[yy], temp.get(head[yy]).values.tolist()]
            All_data.append(each_col)
    for zzz in All_data:
        print(zzz)

get_details("INFY")
