class CasoClinico:
    def __init__(self, id, titulo, descricao, autor, data):
        self.id = id
        self.titulo = titulo
        self.descricao = descricao
        self.autor = autor
        self.data = data

    def __str__(self):
        return f"{self.titulo} ({self.data}) - por {self.autor}"
caso = CasoClinico(1, "Tumor raro", "Paciente com sintomas raros...", "Dr. Andreia Silva", "2025-07-09")
print(caso)
