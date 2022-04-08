import random
from datetime import datetime, timedelta

from run_id import Run_ID
from run_time import Start, End
from energy import Energy
from collision import Collision
from measurement import Measurement
from cyclus import Cyclus
from particle import Particle

class Entry:
	last_run_id = Run_ID()
	last_run_collision = ""
	collision_count = 0;
	def __init__(self): 
		random.seed()

		# Set id
		Entry.last_run_id = self.run_id = self.get_run_id()

		# Set start timestamp
		self.start = Start(datetime.now())
 
		# Generate cycle data
		self.cyclus = Cyclus(datetime.now())
		
		# Generate Measurement data
		self.measurement = Measurement(datetime.now())
 
		# Generate end timestamp
		self.end = End(datetime.now() +
			timedelta(
				seconds=random.randrange(0,1800),
				milliseconds=random.randrange(0,999)
			)
		)

		# Generate Collision data
		self.collision = Collision();
		Entry.last_run_collision = self.collision.collision_occurred
		Entry.collision_count += 1

		# Generate energy values
		self.energy = Energy(0, 100000)
 
		self.particles = [Particle() for n in range(5)]
	
	def get_run_id(self):
		# IF last run resulted in no collision, or if there's been 3 consequtive collisions
		if Entry.last_run_collision == "N" or Entry.collision_count > 2 :
			# Reset run counter and return a new ID
			Entry.collision_count = 0

			return Run_ID()

		# Otherwise return existing run id
		return Entry.last_run_id


	def __repr__(self):
		data: str = (
			f"{self.run_id}, "
			f"{self.start}, "
			f"{self.end}, "
			f"{self.energy}, "
			f"{self.collision}, "
			f"{self.cyclus}, "
			f"{self.measurement}"
		)
		for particle in self.particles:
			data += f", {particle}"
		
		return data + "\n"
 
	def get_headers() -> str:
		return (
			f"{Run_ID.get_headers()}, "
			f"{Start.get_headers()}, "
			f"{End.get_headers()}, "
			f"{Energy.get_headers()}, "
			f"{Collision.get_headers()}, "
			f"{Cyclus.get_headers()}, "
			f"{Measurement.get_headers()}, "
			f"{Particle.get_headers(5)}"
			"\n"
		)	