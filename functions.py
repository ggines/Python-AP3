import csv
MSG= "Aquests són els registres introduïts: "

def file_check(archivo): #Funció per comprovar si el fitxer existeix o no. Si existeix retorna True, i si no retorna False
  try:
    f = open(archivo, "r")
    return True
  except FileNotFoundError:
    return False

def file_header(archivo): #Funció per escriure la capçalera
  with open(archivo, 'a', encoding='utf-8', newline='') as csvfile:
    fieldnames = ['Curs', 'Aula', 'N. alumnes', 'N. professors/es', 'Dia', 'Hora de classe', 'Nom professor/a',
                  'Assignatura', 'Porta principal oberta', 'Porta principal tancada', 'Porta secundària oberta',
                  'Porta secundària tancada', 'Finestres externes obertes', 'Finestres externes tancades',
                  'Finestres internes obertes', 'Finestres internes tancades', 'Ventilació creuada']
    writeCSV = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writeCSV.writeheader()

def file_write(archivo, registro, data): #Funció per afegir els registres al fitxer
  with open(archivo, 'a', encoding='utf-8', newline='') as csvfile:
    fieldnames = ['Curs', 'Aula', 'N. alumnes', 'N. professors/es', 'Dia', 'Hora de classe', 'Nom professor/a',
                  'Assignatura', 'Porta principal oberta', 'Porta principal tancada', 'Porta secundària oberta',
                  'Porta secundària tancada', 'Finestres externes obertes', 'Finestres externes tancades',
                  'Finestres internes obertes', 'Finestres internes tancades', 'Ventilació creuada']
    writeCSV = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writeCSV.writerow({'Curs': registro['curs'], 'Aula': registro['aula'], 'N. alumnes': registro['alumnes'],
                      'N. professors/es': registro['profes'], 'Dia': data, 'Hora de classe': registro['hora'],
                      'Nom professor/a': registro['nomProfe'], 'Assignatura': registro['assignatura'],
                      'Porta principal oberta': registro['principalOberta'], 'Porta principal tancada': registro['principalTancada'],
                      'Porta secundària oberta': registro['secundariaOberta'], 'Porta secundària tancada': registro['secundariaTancada'],
                      'Finestres externes obertes': registro['finestresExOberta'], 'Finestres externes tancades': registro['finestresExTancada'],
                      'Finestres internes obertes': registro['finestresInOberta'], 'Finestres internes tancades': registro['finestresInTancada'],
                      'Ventilació creuada': registro['ventilacio']})

def file_read(archivo): #Funció per llegir el fitxer
    print(MSG)
    with open(archivo) as csvfile:
        readCSV = csv.reader(csvfile, delimiter='\t')
        for row in readCSV:
            print(', '.join(row))