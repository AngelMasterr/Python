# Un modulo es un archivo de python, cualquier archivon que termine en .py es un modulo
# Los modulos se usan para crear funciones especificas para luego llamarlas desde otro archivo
# practicamente todo lo que hacemos es un modulo, pero no sirve para organizar mejor el trabajo

def Saludar(name):
    return(f"hola {name} espero que hayas tenido un día maravilloso")

def Despedirse(name):
    return(f"adios {name}, que tenga un excelente día")
    
# Es recomendable crear las funciones con la primera letra en mayuscula para diferenciarla de varibles que se llamen igual