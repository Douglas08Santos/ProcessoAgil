import requests, re, json

# execucao: python3 ProcessoAgil.py
#bibliotecas necessarias:
	# - requests
	# - re
	# - json
	
'''
Utilizando try-expect para capturar de exceções caso 
não seja possivel se obter resposta da requisição
'''
try:
	#usando o get requests e obtendo como resposta uma string com o codigo(ex HTML) da pagina
	req = requests.get('http://g1.globo.com')
	
	'''
	Analisando o codigo da pagina foi possivel notar que o titulo(title) e
	o subtitle(summary) aparece na seguinte ordem:
		
		..."summary":"Texto do Subtitulo","title":"texto do subtitulo"
	
	assim criei essa expressão regular que captura somente o conteudo dos pares subtitulo e do titulo.
	'''
	regex = r'"summary":(".*?"),"title":(".*?")'

	# procura todas as substrings que se encaixa no regex que criei
	result = re.findall(regex, req.text)
	
	'''
	Utilizando Compreensão de lista crio uma lista de dicionarios para que seja mais facil impressão em Json
	
	'''
	result_json = [{"titulo": result[i][1], "subtitulo":result[i][0]} for i in range(len(result))]
	
	#Impressão no terminal o Json obtido
	
	print(json.dumps(result_json, indent = 4,ensure_ascii=False))

except Exception as e:
	print('Erro: ' , e)
