# Laboratorio_A01769232

El repositorio tiene dos programas el "convertion.py" y "ConverPAdding.py"
Estos son independientes uno del otro. pero ambos dependen de las mismas librerias.

Los  programa  busca realizar una convolución de una matriz ingresada por el usuario a traves de un filtro (kernel) que tambien es ingresado por el usuario. estos son los unicos parametros que resive el metodo 
en el "convolutionPadding" para el programa "converPadding" y "convolution" para el programa "Convertion"
# numpy

NumPy es una librería de Python especializada en el cálculo numérico y el análisis de datos, especialmente para un gran volumen de datos.

#spicy 
SciPy es un ecosistema de software de código abierto basado en Python para matemáticas, ciencia e ingeniería.

## Instalación

Utilice el administrador de paquetes [pip] (https://pip.pypa.io/en/stable/) para instalar numpy y Spicy.

`` python3 -m pip3 install --scipy ''

"pip install numpy"

## Uso 

"import numpy as np" se crea np que sera de la clase numpy para trabajar con los arrays
"from scipy import signal"
se hara uso del modulo "signal.convoled2d" para sacar la convolución con o sin padding.
