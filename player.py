class Player:
	def __init__(self, id, codename, equipmentid, points):
		self.id = id
		self.codename = codename
		self.equipmentid= equipmentid
		self.points = points
		
		def getId(self):
			return self.id
		
		def getCodeName(self):
			return self.codename
			
		def getequipmentid(self):
			return self.equipmentid
		
		def getPoints(self):
			return self.points
			
		def setCodeName(self, codename):
			self.codename = codename
		
		def setEquipmentId(self, equipmentid):
			self.equipmentid = equipmentid
			
		def setPoints(self, points)
			self.points = points
