import db
from sqlalchemy import Column, Integer, String, Boolean

class Tarea(db.Base):
	__tablename__ = "tarea"
	id = Column(Integer, primary_key = True)
	contenido = Column(String(200), nullable = False)
	hecha = Column(Boolean)
	fecha_ini = Column(String(10), nullable = True)
	fecha_fin = Column(String(10), nullable = True)
	descripcion = Column(String(300), nullable = True)
	show_descr = Column(Boolean)

	def __init__(self, contenido, hecha, fecha_ini = "-", fecha_fin = "-", descripcion = "-", show_descr = False):
		self.contenido = contenido
		self.hecha = hecha
		self.fecha_ini = fecha_ini
		self.fecha_fin = fecha_fin
		self.descripcion = descripcion
		self.show_descr = show_descr
	
	def __str__(self):
		return "Tarea ({}: {}, {})".format(self.id, self.contenido, self.hecha)