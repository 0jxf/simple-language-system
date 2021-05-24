import os, sys, json

class Language:

	def __init__(self):
		self.path = "languages"
		self.languages = {}
		for language in os.listdir(self.path):
			if(language.endswith(".json")):
				with open(f'{self.path}/{language}', encoding='utf-8') as language:
					languageJSON = json.loads(language.read())
					self.languages.update(languageJSON)

	def getWord(self, key:str, language:str):
		return self.languages[language][key]

Language = Language()

print(Language.getWord("greet","ar")) # -> @_pmy مرحبا حسابي في الانستقرام هو
print(Language.getWord("greet","en")) # -> Hello my Instagram is @_pmy