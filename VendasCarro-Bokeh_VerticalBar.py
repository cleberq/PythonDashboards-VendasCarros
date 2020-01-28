import pandas as pd 
from bokeh.plotting import figure, output_file, show
from bokeh.transform import factor_cmap
from bokeh.palettes import Spectral6
from bokeh.models import ColumnDataSource
import easygui


'''Exibe janela abrir arquivo, apos abrir o arquivo sra armezando o caminho do mesmo na string xfile
'''
# removendo os caracteres .xlsx do final  do arquvo
openfile = easygui.fileopenbox()
file_caract = int(len(openfile) - 5)
vpath = openfile[:file_caract]
#print(vpath)


'''Gerar um dataframe 
'''
v_dframe = pd.read_excel(openfile, sheet_name='VendaCarros', encoding="utf-8", index_col=0)
#print(v_dframe)
#print(v_dframe[:2]) #linhas com indice
#print(v_dframe.values) #todos valores sem o nome das colunas
#print(v_dframe['Fabricante']) #uma coluna com o indice
#print(v_dframe.Estado) #uma coluna com o indice
#print(v_dframe[['Fabricante','Estado']])#mais de uma coluna com indice


'''# Gerar uma series do DataFrame pelo metodo groupby
'''
vseries = v_dframe.groupby(by='Fabricante').size()#agrupar e contar as fabricantes que mais venderam
#print(vseries)


'''# Definindo os indicadores X 
   # Definindo os Valores Y  
'''
dfx = list(vseries.index)
print(dfx)

dfy = list(vseries.values)
print(dfy)


''' Grafico de barras vertical 
    OBS os indicadores X devem ser do tipo String
'''
# versao1
output_file(vpath+'bar1.html')
p = figure(x_range=dfx, plot_height=350, plot_width=380, title="Fabricante",toolbar_location=None, )
p.vbar(x=dfx, top=dfy, width=0.8, fill_color="purple", line_color ="purple")
p.xgrid.grid_line_color = None
p.y_range.start = 0
p.y_range.end = 300
show(p)

# versao2
output_file(vpath+'bar2.html')
source = ColumnDataSource(data=dict(dfx=dfx, dfy=dfy))
p = figure(x_range=dfx, plot_height=350, title="Vendas por Fabricante", toolbar_location=None)
p.vbar(x='dfx', 
       top='dfy', 
       width=0.8, 
       source=source,
       legend="dfx",
       line_color='white', 
       fill_color=factor_cmap('dfx', palette=Spectral6, factors=dfx))
p.xgrid.grid_line_color = None
p.y_range.start = 0
p.y_range.end = 300
p.legend.orientation = "horizontal"
p.legend.location = "top_center"
show(p)
