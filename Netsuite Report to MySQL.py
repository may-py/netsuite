import time

def get_mysql():
    import mysql.connector
    import pandas as pd
    import openpyxl
    from sqlalchemy import create_engine
    from datetime import datetime

    host="localhost"
    user="root"
    password="xxxxxxxxxxx"
    database="web_ns"  #Change database
    auth_plugin='mysql_native_password'
    

    mydb = mysql.connector.connect( 
    host=host, 
    user=user, 
    password=password,
    auth_plugin=auth_plugin,
    db=database,
    )
    mycursor = mydb.cursor(buffered=True)
    engine = create_engine("mysql+mysqldb://{user}:{pw}@{host}/{db}"
				.format(host=host, db=database, user=user, pw=password))

    
    try:
        data_sql = pd.read_sql_table('web_ns_data', engine)
        data_sql['Month'] = data_sql['Date'].dt.month
        # value = datetime.now().month-3
        data_sql = data_sql.loc[data_sql.Month<7]
        mycursor.execute('DELETE FROM web_ns_data where Month(Date)>7')
    except:
        pass

    try:
        print(data_sql.Month.unique())
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
    
    url = 'https://xxxxx.app.netsuite.com/app/reporting/webquery.nl?compid=xxxxxx&entity=-x&email=xxxxxxxxxxxxxx&role=x&cr=xxx&hash=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'    x = requests.get(url)
    html = etree.HTML(x.content)
    tr_nodes = html.xpath('//table/tr')

    td_content = [[td.text for td in tr.xpath('td')] for tr in tr_nodes[0:]]

    data = pd.DataFrame(td_content)

    header = data.iloc[0]
    data = data[1:]
    data.columns = header

    ## Optional
    data['Total Revenue'] = data['Total Revenue'].str.replace("=","")
    data.Date = pd.to_datetime(data.Date,format="%d/%m/%Y")

    try:
        data1 = pd.concat([data_sql,data],axis=0)
    except:
        data1 = data

    try:
        mycursor.execute("DROP TABLE web_ns_data")
    except:
        pass

    data1.to_sql('web_ns_data', engine, index=False, if_exists='replace')


    return mycursor.close()


if __name__ == "__main__":
    get_mysql()

 
