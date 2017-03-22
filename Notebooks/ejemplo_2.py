"""
Modulo ejemplo_2

>>> ej("2")
'Hola mundo dos'
>>> ej()
'Hola mundo '
"""

def ej(s="", d=" "):
	"""Ejemplo

	>>> ej("!")
	'Hola mundo !'
	"""
	return( 'Hola mundo' + d + s )

if __name__ == "__main__":

	import argparse

	parser = argparse.ArgumentParser(description='Hola mundo mas algo...')

	parser.add_argument('Text', metavar='T', type=str, nargs=1,
                   help='Texto a imprimir')

	parser.add_argument('--sep', type=str, default=" ", help='FOO!')

	args = parser.parse_args()

	salida = ej( args.Text[0], args.sep[0] )

	print(salida)
