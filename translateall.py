from deep_translator import GoogleTranslator
from pathlib import Path
import os 


def translation(to_translate):
	translated = GoogleTranslator(source='auto',
		target='pl').translate(to_translate)
	return translated


with open('/home/devja/Dokumenty/PROG2023/tlumacz/allfiles.txt', 'r') as ffiles:
	for ffile in ffiles:
		os.makedirs('/home/devja/Dokumenty/PROG2023/tlumacz/'+ 'pl' +os.path.dirname(ffile[1:]), exist_ok=True)
		with open('/home/devja/Dokumenty/PROG2023/tlumacz' + ffile[1:].strip(), 'r') as fsource:
			with open('/home/devja/Dokumenty/PROG2023/tlumacz/' + 'pl' + ffile[1:].strip(), 'a+') as fwrite:
				print(fsource)
				for line in fsource:
					if line.lstrip().startswith('define'):
						x = line.find(",")	
						restline = line[x:]
						a, b = restline.find("'"), restline.rfind("'")
						to_translate = restline[a+1:b]
						translated = translation(to_translate)
						try:
							x = line.replace(to_translate,translated)
						except:
							pass
						fwrite.write(str(x))
					else:
						fwrite.write(line)