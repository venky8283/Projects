from sanic import Sanic
from sanic.response import html, text
import sqlalchemy
from sqlalchemy import Table, Column, String
def connect(user, password, db, host='localhost', port=5432):
	url='postgresql://{}:{}@{}:{}/{}'
	url=url.format(user,password, host, port, db)
	con=sqlalchemy.create_engine(url, client_encoding='utf8')
	meta=sqlalchemy.MetaData(bind=con, reflect=True)
	return con, meta


con, meta=connect('postgres','Venky*@*32','test')

try:
	'''
	question=Table('Question',meta,
		Column('Q', String, primary_key=True),

		Column('OA', String),
		Column('OB', String),
		Column('OC', String),
		Column('OD', String)
	)
	##meta.drop_all()
	##question.drop(con, checkfirst=False)
	##question.create(con, checkfirst=True)
	'''

except:
	print('ALready created')
for table in meta.tables:
	print (table)

#clause=question.insert().values(Q='What is this test about?', OA='timepass', OB='testing',OC='leisure work',OD='learning')

results=meta.tables['Question']
temp=''
for row in con.execute(results.select()):
	temp=row

print(temp)


app=Sanic()

@app.route("/")
async def test(request):
	
	string='<h1>'+temp[0]+'</h1><br>'+'<input type="radio">'+temp[1]+'<input type="radio">'+temp[2]+'<input type="radio">'+temp[3]+'<input type="radio">'+temp[4]+'<br><br><input value="Submit" type="submit">';
		
	return html(string)



if __name__ =="__main__":
	app.run(host="0.0.0.0",port=8000)


