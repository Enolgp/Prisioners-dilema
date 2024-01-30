# Dilema del prisionero
Un proyecto orientado a poner a prueba mis habilidades de programación en Python, analisis de datos e Inteligencia Artificial usando el dilema del prisionero como punto de partida y desarrollandolo según vea conveniente.
Soy de España por lo que la guía se realizará en Castellano aunque intentaré que los comentarios y esta guía (copiada o adaptada en archivo README_ENG.md) sean en inglés

## Contexto
La idea de este proyecto surgió al ver el [video](https://www.youtube.com/watch?v=vBgrvVY1jGo "Video sobre el dilema del prisionero") ya que me se me ocurrió intentar recrear el proyecto mencionado con los mismos u otros algoritmos y obtener los datos correspondientes a la iteraciones entre los diferentes algoritmos para tratarlos mostrarlos y analizarlos intentando dar un análisis sociológico/filosófico basándome en la similitud entre el comportamiento humano y los algoritmos que interactúan.

## Descripción del royecto
El proyecto tiene varias carpetas:
- data: guarda los datos a estudiar/representar en formato csv
- diagramas: contiene los diagramas e imágenes del proyecto
- scripts: contiene todos los archivos con código del proyecto

La carpeta scripts tiene varias subcarpetas:
- Agents: todas las clases que se heredarán de la superclase Agente y que ejecutan los diferentes algoritmos que van a interactuar entre sí
- Analysis: scripts de python que leen los datos de la carpeta _data_ y los tratan y muestan en pos de hacer su analisis
- Phases: Scripts que gestionan la interacción entre los diferentes agentes según una serie de normas dadas a lo que llamaremos una **Fase**
A su vez, está el script _rules.py_ con una clase que implementa las reglas del dilema del prisionero.

## Desarrollo del proyecto
### Fase 1
En la fase 1 cada pareja de agentes interacionará 500 veces. Número fijo y conocido por los agentes, por lo que el algoritmo puede tomarlo en cuenta.
Las parejas de agentes se establecerán de tal forma que un agente se enfrente a cada otro tipo de agente y a una copia de si mismo