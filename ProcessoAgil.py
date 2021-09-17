import requests, re, json

try:
	req = requests.get('http://g1.globo.com')
	#print(req.text)
	
	regex = r'"summary":(".*?"),"title":(".*?")'

	result = re.findall(regex, req.text)
	#print(result)
	#print()
	#print(result[1])
	
	#print(result[1][0])
	#print(result[1][1])
	
	result_json = [{"titulo": result[i][1], "subtitulo":result[i][0]} for i in range(len(result))
	
	print(json.dumps(result_json, indent = 4,ensure_ascii=False))

except Exception as e:
	print('Erro: ' , e)