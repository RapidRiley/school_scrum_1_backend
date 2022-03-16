import random

class Particle:
	particles: list[str] = [
		"Antihydrogon",
		"Baryon",
		"Diquark",
		"Electron neutrino",
		"Gluon",
		"Graviton",
		"Lepton",
		"Meson",
		"Muon neutrino",
		"Pentaquark",
		"Photon",
		"Preons",
		"Quarkonium",
		"Tau neutrino",
		"W Boson",
		"Z Boson"
	]
	def __init__(self):
		self.name = Particle.particles[random.randrange(0, len(Particle.particles))]
		self.number = random.randrange(0, 1000)
 
	def __repr__(self):
		return f"{self.name}, {self.number}"
 
	def get_headers(particle_amount: int) -> str:
		headers: str = ""
		for i in range(1, particle_amount + 1):
			headers += f"Particle_{i}, Particle_{i}_n, "
		return headers[:-2]