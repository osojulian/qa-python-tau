def user_info(name, age, city = 'Medellin'):
    '''
    This function takes three parameters: name, age, city
    from an argument provided to the function
    You also can use keyword arguments to pass values to the function parameters like this city ='New York'
    '''

    print(f'name {name}, age {age}, city {city}')

user_info('John', 25, 'New York')
user_info('Alice', 30, 'Los Angeles') 
user_info('Bob', 35)  # Uses default city 'Medellin'



## *args y **kwargs
def mostrar_frutas(*args):
    for fruta in args:
        print(fruta)
    pass

mostrar_frutas('manzana', 'banana', 'naranja')


def configurar_prueba(**kwargs):
    for clave, valor in kwargs.items():
        print(f'{clave}:{valor}')

configurar_prueba(navegador='Chrome', version='89.0', sistema_operativo='Windows 10')