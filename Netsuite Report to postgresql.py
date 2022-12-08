import time

def get_pssql():
    import psycopg2
    import pandas as pd
    import openpyxl
    from sqlalchemy import create_engine
    from sqlalchemy import inspect
    from datetime import datetime

    host="localhost"  #update host
    user="root" #update user
    password="xxxxxxxxxxx"
    database="web_ns"  #Change database
    

    create_string = f'postgresql+psycopg2://{user}:{password}@{host}/{database}'

    engine = create_engine(create_string)
    insp = inspect(engine)
    print("TABLES", insp.get_table_names())

    conn = engine.connect()

    mydb = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=database,
        port=5432,
    )
    mydb.autocommit = True
    mycursor = mydb.cursor()


    try:
        data_sql = pd.read_sql_table('web_ns_data', engine, schema='public')
        print(data_sql.head())
    except:
        pass

    try:
        print(data_sql.Month.unique())
        print(engine.has_table('web_ns_data', schema='public'))
    except:
        pass

    import pandas as pd
    from pandas.io import sql
    import requests
    import pandas as pd
    import json
    import lxml
    from lxml import etree
    import urllib3, urllib
    from urllib.request import urlopen

    url = 'https://xxxxx.app.netsuite.com/app/reporting/webquery.nl?compid=xxxxxx&entity=-x&email=xxxxxxxxxxxxxx&role=x&cr=xxx&hash=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'    
    x = requests.get(url)
    html = etree.HTML(x.content)
    tr_nodes = html.xpath('//table/tr')

    td_content = [[td.text for td in tr.xpath('td')] for tr in tr_nodes[0:]]

    data = pd.DataFrame(td_content)

    header = data.iloc[0]
    data = data[1:]
    data.columns = header


    data.Date = pd.to_datetime(data.Date,format="%d/%m/%Y")




    try:
        data1 = pd.concat([data_sql,data],axis=0)
    except:
        data1 = data

    try:
        mycursor.execute("DROP TABLE web_ns_data")
    except:
        pass

    print(data1.shape)
    data1.to_sql('web_ns_data', con=engine, schema='public', index=False, if_exists='replace')

    updated_data_sql = pd.read_sql_table('web_ns_data', engine, schema='public')
    print("Updated",updated_data_sql.head())
    print("Updated", updated_data_sql.columns)


    return mycursor.close()


if __name__ == "__main__":
    get_pssql()
