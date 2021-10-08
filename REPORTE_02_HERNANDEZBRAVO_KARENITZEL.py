from csv import reader

list_of_rows = []

class Transporte() :
    
    def __init__(self, transporte, n):

        self.transporte = transporte
        self.n = n

    def __str__(self) -> str:
        return self.transporte + " n = " + str(self.n) + "\n"

    def sumar(self):
        self.n += 1

    def getName(self):
        return self.transporte
    
transportes = [Transporte("Sea", 0),  Transporte("Air", 0), Transporte("Rail", 0),  Transporte("Road", 0),  Transporte("Konica", 0)]

with open('synergy_logistics_database.csv', 'r') as csv_file:
    csv_reader = reader(csv_file)
    # Passing the cav_reader object to list() to get a list of lists
    list_of_rows = list(csv_reader)

for i in range(0, len(transportes)):
   for j in range (1, len(list_of_rows)):
       if(transportes[i].getName() == list_of_rows[j][7]):
           transportes[i].sumar()

print(transportes[0])
print(transportes[1])
print(transportes[2])
print(transportes[3])
print(transportes[4])

#Caso 1
import pandas as pd
import seaborn as sns
  
fileLocation = 'C:/Users/Karen Bravo/OneDrive/Escritorio/py/py/'
fileName = 'synergy_logistics_database.csv'

synergyDF = pd.read_csv(fileLocation + fileName, index_col='register_id')
print(synergyDF)

index = synergyDF.index
print(index)

columns = synergyDF.columns
print(columns)


synergyDF.head(10)

simpleDF = synergyDF [['direction','origin','destination','transport_mode','total_value']]
print(simpleDF)

simpleDF.groupby(['direction','origin','destination','transport_mode']).count()

rutasUnicas = simpleDF.groupby(['direction','origin','destination','transport_mode']).count()
print(rutasUnicas)



rutasUnicas = rutasUnicas.rename(columns={'total_value' : 'count'})
print(rutasUnicas)


rutasUnicas.sort_values('count',ascending=False)
rutasUnicas.head(10)

rutasExp = rutasUnicas.xs('Exports').head(10)
print(rutasExp)

rutasExp.head(10)

rutasUnicas.xs('Exports')
 
rutasUnicas.xs('Imports')

agrupadosExp = rutasUnicas.xs('Exports')
agrupadosImp = rutasUnicas.xs('Imports')

agrupadosExp.head(10)

agrupadosImp.head(10)

agrupadosExp['name'] = agrupadosExp.index.to_list()
print(agrupadosExp)

def primer_punto(text):
   nombre = f'{text[0]}/{text[1]}\n{text[2]}'
    return nombre

agrupadosExp['name'] = agrupadosExp['name'].apply(primer_punto)
print(agrupadosExp)

sns.set(rc={"figure.figsize": (18, 6)})  #width=8, height=4
sns.barplot(data=agrupadosExp.head(10), x='name', y='count')

agrupadosExp['medio'] = agrupadosExp.index.to_list()


# Función para cambiar el contenido de la columna
def medio_transp(text):
    return text[2]


# Aplicamos la transformación
agrupadosExp['medio'] = agrupadosExp['medio'].apply(medio_transp)
# Graficamos
sns.set(rc={"figure.figsize": (18, 6)})  #width=8, height=4
sns.barplot(data=agrupadosExp.head(10), x='name', y='count', hue='medio')

synergyDF.groupby('transport_mode').count()

data = synergyDF.groupby('transport_mode').count()
sns.set(rc={"figure.figsize": (8, 6)})  #width=8, height=4
sns.barplot(data=data, y='direction', x=data.index)


paisValor = synergyDF.groupby(['direction', 'origin']).sum()
paisValor = paisValor.sort_values(by=['total_value'], ascending=False)

expPaisValor = paisValor.xs('Exports')
impPaisValor = paisValor.xs('Imports')

expPaisValor['porcentaje_acumulado'] = 100 * (expPaisValor.total_value.cumsum() / expPaisValor.total_value.sum())
print(expPaisValor)

top_80 = expPaisValor[expPaisValor["porcentaje_acumulado"] < 80]
top_80