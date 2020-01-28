import pandas as pd 
from bokeh.plotting import figure, output_file, show
from bokeh.transform import factor_cmap
from bokeh.palettes import Spectral6
from bokeh.models import ColumnDataSource
import easygui


'''Exibe janela abrir arquivo, apos abrir o arquivo sera armazendo o caminho do mesmo na string vpath
'''
vpath = str(easygui.fileopenbox())
#print(vpath)


'''Gerar um dataframe 
'''
v_dframe = pd.read_excel(vpath, sheet_name='VendaCarros', encoding="utf-8", index_col=0)
#print(v_dframe)
#print(v_dframe[:2]) #linhas com indice
#print(v_dframe.values) #todos valores sem o nome das colunas
#print(v_dframe['Fabricante']) #uma coluna com o indice
#print(v_dframe.Estado) #uma coluna com o indice
#print(v_dframe[['Fabricante','Estado']])#mais de uma coluna com indice


'''# Gerar uma series do DataFrame pelo metodo groupby
'''
vseries = v_dframe.groupby('Ano').size()#agrupar e contar as unidades vendidas por ano
print(vseries)


'''# Definindo os indicadores X 
   # Definindo os Valores Y  
'''
dfx = list(map(str,(vseries.index)))
print(type(dfx))

dfy = list(vseries.values)
print(dfy)

''' #Grafico de LINHA simples 
'''

# versao1
output_file(vpath+'versao1.html')
p = figure(title="Vendas Anual", x_axis_label='Ano', y_axis_label='Unidades', plot_width=800, plot_height=350, background_fill_color="#4A92AE")
p.line(dfx,dfy, color="purple", legend="Total vendas.", line_width=2)
p.y_range.start = 0
p.y_range.end = 300
show(p)


# versao2
output_file(vpath+'versao2.html')
p2 = figure(title="Vendas Anual", x_axis_label='Ano', y_axis_label='Unidades', plot_width=800, plot_height=350, background_fill_color="#4A92AE")
p2.line(dfx,dfy, color="green", legend="Total vendas.", line_width=2)
p2.y_range.start = 0
p2.y_range.end = 300
show(p2)

