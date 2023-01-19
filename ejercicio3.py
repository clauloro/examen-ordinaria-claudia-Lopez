def equilibrio_estable(num):
    num=str(num)
    digitos=[]
    for digito in num:
        digitos.append(digito_a_palabra(digito))
    palabra=''.join(digitos)
    letras=len(palabra)
    if letras == 4:
        return palabra
    else:
        return[palabra]+equilibrio_estable(letras)
def digito_a_palabra(digito):
    if digito=='0':
        return 'zero'
    if digito =='1':
        return 'one'
    if digito == '2':
        return 'two'
    if digito == '3':
        return 'three'
    if digito == '4':
        return 'four'
    if digito == '5':
        return 'five'
    if digito == '6':
        return 'six'
    if digito == '7':
        return 'seven'
    if digito == '8':
        return 'eight'
    if digito == '9':
        return 'nine'