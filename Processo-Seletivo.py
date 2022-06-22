

grau_esquerdo = int(input('Digite o grau esquerdo '))
grau_direito = int(input('Digite o grau direito '))
tipo_de_lente_esquerda = str(input(
    'Digite se a lente esquerda é  cilíndrica ou esférica '))
tipo_de_lente_direita = str(input(
    'Digite se a lente direita é cilíndrica ou esférica '))

tipo_de_lente_esquerda = tipo_de_lente_esquerda.casefold()
tipo_de_lente_direita = tipo_de_lente_direita.casefold()
tipo_de_lente_esquerda = tipo_de_lente_esquerda.strip()
tipo_de_lente_direita = tipo_de_lente_direita.strip()

if grau_direito < 1 and grau_esquerdo < 1:
    if grau_direito > -16 and grau_esquerdo > -16:
        if (('esférica' or 'esferica') in tipo_de_lente_esquerda) and (('esférica' or 'esferica') in tipo_de_lente_direita):
            if grau_direito > -12 and grau_esquerdo > -12:
                if grau_direito < -3 and grau_esquerdo < -3:
                    print('Será usado a lente Prime')
        elif (('cilíndrica' or 'cilindrica') in tipo_de_lente_esquerda) and (('cilíndrica' or 'cilindrica') in tipo_de_lente_direita):
            if (grau_direito > -2) and (grau_esquerdo > -2):
                print('Será usado a lente Prime')
        elif (('cilíndrica' or 'cilindrica') in tipo_de_lente_esquerda) or (('cilíndrica' or 'cilindrica') in tipo_de_lente_direita):
            if (grau_direito > -2) or (grau_esquerdo > -2):
                if (('esférica' or 'esferica') in tipo_de_lente_esquerda) or (('esférica' or 'esferica') in tipo_de_lente_direita):
                    if grau_direito > -13 or grau_esquerdo > -13:
                        if grau_direito < -3 or grau_esquerdo < -3:
                            print('Será usado a lente Prime')
        else:
            if (('esférica' or 'esferica') in tipo_de_lente_esquerda) and (('esférica' or 'esferica') in tipo_de_lente_direita):
                if grau_direito > -16 and grau_esquerdo > -16:
                    if grau_direito < 1 and grau_esquerdo < 1:
                        print('Será usado a lente Vision')
            elif (('cilíndrica' or 'cilindrica') in tipo_de_lente_esquerda) and (('cilíndrica' or 'cilindrica') in tipo_de_lente_direita):
                if (grau_direito > -6) and (grau_esquerdo > -6):
                    print('Será usado a lente  Vision')
            else:
                print('Digite corretamente e não deixe nem uma imfornação em branco')
    else:
        print('O grau tem que ser menor que 1 e maior -16. Digite corretamente e não deixe nem uma imfornação em branco')
