import csv

from functions import file_write
from functions import file_header
from functions import file_check
from functions import file_read
MSG= "**********BENVINGUT/DA**********\nComença a introduir les dades:"
MSG2= "Introdueix el nombre del fitxer on vols guardar el registre: "
MSG3= "L'aula té porta secundària? Sí=1 No=0 "
MSG4= "L'aula té finestres externes? Sí=1 No=0 "
MSG5= "L'aula te finestres internes? Si=1 No=0 "
MSG6= "S'ha donat ventilació creuada en algun moment? Sí=1 No=0 "

def main():
    archivo = input(MSG2) + '.csv'
    check= file_check(archivo)
    if check == False:
        file_header(archivo)
    print(MSG)
    registro= dict()
    registro['curs'] = input("Introdueix el curs: ")
    registro['aula'] = input("Introdueix l'aula: ")
    registro['alumnes'] = input("Introdueix el nombre d'alumnes: ")
    registro['profes'] = input("Introdueix el nombre de professors: ")
    registro['dia'] = input("Introdueix el número del dia: ")
    registro['mes'] = input("Introdueix el número del mes: ")
    registro['year'] = input("Introdueix l'any: ")
    registro['hora'] = input("Introdueix l'hora (format hh:mm): ")
    registro['nomProfe'] = input("Introdueix el nom del professor: ")
    registro['assignatura'] = input("Introdueix l'assignatura: ")
    registro['principalOberta'] = input("Indica el temps (en minuts) que ha estat oberta la porta principal: ")
    registro['principalTancada'] = input("Indica el temps (en minuts) que ha estat tancada la porta principal: ")
    secundariaOpcion= input(MSG3)
    if secundariaOpcion == '1':
        registro['secundariaOberta'] = input("Indica el temps (en minuts) que ha estat oberta la porta secundària: ")
        registro['secundariaTancada'] = input("Indica el temps (en minuts) que ha estat tancada la porta secundària: ")
    elif secundariaOpcion == '0':
        registro['secundariaOberta'] = "No n'hi ha"
        registro['secundariaTancada'] = "No n'hi ha"
    finestresExOpcion= input(MSG4)
    if finestresExOpcion == '1':
        registro['finestresExTancada'] = input("Indica el temps (en minuts) que han estat tancades les finestres externes: ")
        registro['finestresExOberta'] = input("Indica el temps (en minuts) que han estat obertes les finestres externes: ")
    elif finestresExOpcion == '0':
        registro['finestresExTancada'] = "No n'hi ha"
        registro['finestresExOberta'] = "No n'hi ha"
    finestresInOpcion= input(MSG5)
    if finestresInOpcion == '1':
        registro['finestresInTancada'] = input("Indica el temps (en minuts) que han estat tancades les finestres internes: ")
        registro['finestresInOberta'] = input("Indica el temps (en minuts) que han estat obertes les finestres internes: ")
    elif finestresInOpcion == '0':
        registro['finestresInTancada'] = "No n'hi ha"
        registro['finestresInOberta'] = "No n'hi ha"
    ventilacio= input(MSG6)
    if ventilacio == '1':
        registro['ventilacio'] = "Sí"
    elif ventilacio == '0':
        registro['ventilacio'] = "No"
    data= registro['dia'] + '/' + registro['mes'] + '/' + registro['year']
    file_write(archivo, registro, data)
    file_read(archivo)
if __name__ == '__main__':
    main()