def function(*args, **kwargs):
    print(args) 
    idade = kwargs.get('idade')
    
    if idade is not None:
        print(idade)
    
lista = [1,2,3,4,5,6]
function(*lista, nome = 'Vinícius', user = 'Daniel', idade = '30 anos')
