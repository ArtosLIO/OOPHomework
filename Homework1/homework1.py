
class Element(object):
	def agg_state(self, t):
		if(t < self.temperature_melting):
			return "Chlorine in solid state." # твердое состояние
		elif(t >= self.temperature_melting and t < self.temperature_evaporation):
			return "Chlorine in liquid state." # жидкое состояние
		elif(t >= self.temperature_evaporation):
			return "Chlorine in gaseous state." # газообразное состояние

	def convert_temperature(self, scale):
		if(scale == 'C' and self.scale_temperature != 'C'):
			if(self.scale_temperature == 'K'):
				self.temperature_melting -= 273.15
				self.temperature_evaporation -= 273.15
			elif(self.scale_temperature == 'F'):
				self.temperature_melting = (self.temperature_melting - 32) * 5/9
				self.temperature_evaporation = (self.temperature_evaporation - 32) * 5/9
			self.scale_temperature = scale

		elif(scale == 'K' and self.scale_temperature != 'K'):
			if(self.scale_temperature == 'C'):
				self.temperature_melting += 273.15
				self.temperature_evaporation += 273.15
			elif(self.scale_temperature == 'F'):
				self.temperature_melting = (self.temperature_melting - 32) * 1.8 + 273.15
				self.temperature_evaporation = (self.temperature_evaporation - 32) * 1.8 + 273.15
			self.scale_temperature = scale

		elif(scale == 'F' and self.scale_temperature != 'F'):
			if(self.scale_temperature == 'C'):
				self.temperature_melting = (self.temperature_melting * 1.8) + 32
				self.temperature_evaporation = (self.temperature_evaporation * 1.8) + 32
			elif(self.scale_temperature == 'K'):
				self.temperature_melting = (self.temperature_melting - 273.15) * 1.8 + 32
				self.temperature_evaporation = (self.temperature_evaporation - 273.15) * 1.8 + 32
			self.scale_temperature = scale


class Chlorine(Element):
	scale_temperature = 'C'
	temperature_melting = -100 # температура плавления
	temperature_evaporation = -34 # температура испарения

	


chlor = Chlorine()

print(chlor.agg_state(-120))
print(chlor.agg_state(-100))
print(chlor.agg_state(-57))
print(chlor.agg_state(-34))
print(chlor.agg_state(24))

print(chlor.scale_temperature)
print(chlor.temperature_melting, chlor.temperature_evaporation)

chlor.convert_temperature('K')
print(chlor.scale_temperature)
print(chlor.temperature_melting, chlor.temperature_evaporation)

chlor.convert_temperature('F')
print(chlor.scale_temperature)
print(chlor.temperature_melting, chlor.temperature_evaporation)

chlor.convert_temperature('C')
print(chlor.scale_temperature)
print(chlor.temperature_melting, chlor.temperature_evaporation)

