# la carpeta que se constituya como un paquede debe tener el archivo "__init__.py" vacio o con codigo
# importar un modulo de un paquete es igual que importar un modulo suelto, pero es mejor para organizar los modulos
# debido a que agrega la ruta completa del paquete, de esta manera python busca mas rapido y organizado

import paquete.mod_saludar
print(paquete.mod_saludar.saludar("angel"))

# __init__: El archivo puede incluir código que se ejecutará automáticamente cuando se importe el paquete por ejemplo, 
# puedes usarse para inicializar algunos valores o configuraciones que deban estar disponibles en todos los módulos dentro del paquete.

# Organización: Al usar paquetes, puedes organizar tus módulos de manera más estructurada y coherente.

# Nombres de módulos únicos: Al usar paquetes, puedes asegurarte de que los nombres de tus módulos sean únicos y 
# evitar posibles conflictos con otros módulos.

# Reutilización de código: Al tener módulos organizados en paquetes, es más fácil reutilizar código entre proyectos.

# Mejora la legibilidad: Al tener módulos organizados en paquetes, se hace más fácil entender y seguir 
# la estructura y relación entre los módulos.