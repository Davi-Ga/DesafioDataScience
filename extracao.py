from google.colab import drive
import pandas as pd
from pandas_profiling import ProfileReport

dados=pd.read_csv('/content/drive/My Drive/houses_to_rent_v2.csv')

dados.head(10)

profile = ProfileReport(dados, title='Dados de alugueis',html={'style':{'full_width':True}})
profile.to_notebook_iframe()