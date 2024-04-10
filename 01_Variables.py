#recomienda python escribir en minuscula o con _
my_variable_string = "my string variable"
print(my_variable_string)

my_variable_int = 5
print(my_variable_int)

my_variable_bool = False
print(my_variable_bool)

# me convierte en string el int 
my_int_to__str_variable = str(my_variable_int)
print(type(my_int_to__str_variable), type(my_variable_int))

# concatenar cadenas
print (my_variable_string, str(my_variable_int), my_variable_bool)

# funciones del sistema 
# len me cuenta cuantos caracteres hay 
print(len(my_variable_string))