from src.modelo.cancion import Cancion
from src.modelo.interprete import Interprete
from src.modelo.album import Album, Medio
from src.modelo.declarative_base import Session

if __name__ == '__main__':
    session = Session()
    cancion = session.query(Cancion).get(1)
    session.delete(cancion)
    session.commit()
    session.close()
