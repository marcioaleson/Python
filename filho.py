from pessoa import Pessoa
class Filho(Pessoa):
	def __init__(self, **kwargs):
		super(Filho,self).__init__(**kwargs)

	def aniversario(self):
		self.idade+=1

	def caminhar(self):
		print("Aprendendo a caminhar!")


