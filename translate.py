from deep_translator import GoogleTranslator

def translation(to_translate):
	translated = GoogleTranslator(source='auto',
		target='pl').translate(to_translate)
	return translated

with open('/home/devja/Dokumenty/PROG2023/tlumacz/en/controllers/tinymce/tinymce.php', 'r') as f:
	for line in f:
		if line.startswith('define'):
			x = line.find(",")	
			restline = line[x:]
			to_translate = restline[3:-3]
			translated = translation(to_translate)
			x = line.replace(to_translate,translated)
			print(x)
		else:
			print(line)