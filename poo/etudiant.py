class Etudiant:
	def __init__(self, nom, filiere):
		self.nom = nom
		self.filiere = filiere
		self.notes = []

	def ajouter_note(self, note):
		self.notes.append(note)
	
	def moyenne(self):
		if len(self.notes) == 0:
			return 0
		return sum(self.notes)/len(self.notes)
	
	def se_presenter(self):
		print(f"Je suis {self.nom}, en {self.filiere}, moyenne : {self.moyenne():.2f}")

class EtudiantBUT(Etudiant):
    def __init__(self, nom, filiere, semestre):
        super().__init__(nom,filiere)
        self .semestre = semestre
        self.competences_validees = []
    
    def valider_competence(self, competence):
        self.competences_validees.append(competence)
    
    def se_presenter(self):
        super().se_presenter()
        print(f"-> Semestre {self.semestre}, competences validées : {self.competences_validees}")

class EtudiantAlternant(EtudiantBUT):
    def __init__(self, nom, filiere, semestre, entreprise):
        super().__init__(nom, filiere, semestre)
        self.entreprise = entreprise
    
    def changer_entreprise(self, nouvelle_entreprise):
        self.entreprise = nouvelle_entreprise
    
    def se_presenter(self):
        super().se_presenter()
        print(f"Entreprise actuelle : {self.entreprise}")

if __name__ == "__main__":
    e3 = EtudiantAlternant("Maxens", "BUT Info", 3, "Capgemini")
    e3.ajouter_note(16)
    e3.ajouter_note(14)
    e3.valider_competence("Développer une application")
    e3.se_presenter()

