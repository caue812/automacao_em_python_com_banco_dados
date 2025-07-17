import yagmail
from pandas.plotting import table

from comunicacao_banco import criar_conexao, cursor
import pandas as pd

with criar_conexao() as conn:
    cursor = conn.cursor()
    sql ='''SELECT * FROM cervejas'''
    cursor.execute(sql)
    produtos = cursor.fetchall()
    cursor.close()

with criar_conexao() as conn:
    cursor = conn.cursor()
    sql = '''SELECT * FROM cervejas'''
    df = pd.read_sql(sql, conn)

df = df.fillna('')

tabela = df.to_html(index=False, border=False, header=False)
df.to_csv('cervejas.csv')
#
# tabela='a'
# for produto in produtos:
#      tabela += f'''
#      <tr>
#          <td>{produto[1]}<td>
#          <td>{produto[2]}<td>
#          <td>{produto[3]}<td>
#          <td>{produto[4]}<td>
#          <td>{produto[5]}<td>
#      <tr>
#          '''
# tabela += '</table>'
senha_app = 'fukz ejwp twhm kqyx'
email = yagmail.SMTP('cauepravato5138@gmail.com',senha_app)
email.send(
     to='cauepravato5138@gmail.com',
     subject='Email com Yagmail',
     contents=tabela,
    attachments='cervejas.csv'
)

