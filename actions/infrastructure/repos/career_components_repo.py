import psycopg2

from actions.domain.entities.carrera_pc_componentes import CarreraPcComponentes
from actions.domain.entities.carrera_universitaria import CarreraUniversitaria

class CareerComponentsRepo:
    def __init__(self):
        self.conn = psycopg2.connect(database = "viola",
                                    user = "postgres",
                                    host= 'localhost',
                                    password = "Isee420.69&hear",
                                    port = 5432)
        
        self.cursor = self.conn.cursor()

    def search_synonym(self, sting_attempt : str) -> str:

        #try to get carrera_pc_componentes first
        carrera = self.get_carrera_universitaria_by_name(sting_attempt)
        if carrera:
            return carrera.nombre

        self.cursor.execute(f"SELECT real_word FROM synonyms WHERE raw_string ILIKE '{sting_attempt}'")

        result = self.cursor.fetchone()

        if result:
            return result[0] if result else sting_attempt
        
    def get_carrera_pc_componentes(self, id_carrera: int) -> CarreraPcComponentes:
        # Consulta SQL para obtener los datos usando el id_carrera
        self.cursor.execute("""
            SELECT id_carrera, min_cpu, rec_cpu, min_ram, rec_ram, min_graphic, rec_graphic, min_storage, rec_storage, recomendacion_extra
            FROM carrera_pc_componentes
            WHERE id_carrera = %s
        """, (id_carrera,))
        
        # Obtener el resultado de la consulta
        result = self.cursor.fetchone()
        
        # Si no se encuentra un registro, retornar None
        if result is None:
            return None

        # Crear el objeto CarreraPcComponentes con los datos obtenidos
        carrera_componentes = CarreraPcComponentes(
            id_carrera=result[0],
            min_cpu=result[1],
            rec_cpu=result[2],
            min_ram=result[3],
            rec_ram=result[4],
            min_gpu=result[5] if result[5] is not None else "",  # Manejo de valores opcionales
            rec_gpu=result[6] if result[6] is not None else "",
            min_storage=result[7],
            rec_storage=result[8],
            recomendacion_extra=result[9] if result[9] is not None else ""
        )
        
        return carrera_componentes
    
    def get_carrera_universitaria_by_name(self, name: str) -> CarreraUniversitaria:
        # Consulta SQL para obtener el id de la carrera usando el nombre
        self.cursor.execute("""
            SELECT id, nombre, area, duracion
            FROM carrera_universitaria
            WHERE nombre ILIKE %s
        """, (name,))
        
        # Obtener el resultado de la consulta
        result = self.cursor.fetchone()
        
        # Si no se encuentra un registro, retornar None
        if result is None:
            return None
        
        carrera = CarreraUniversitaria(
            id=result[0],
            nombre=result[1],
            area=result[2],
            duracion=result[3]
        )

        return carrera
    
    def get_carrera_pc_componentes_by_id(self, id_carrera: int) -> CarreraPcComponentes:
        # Consulta SQL para obtener los datos usando el id_carrera
        self.cursor.execute("""
            SELECT id_carrera, min_cpu, rec_cpu, min_ram, rec_ram, min_graphic, rec_graphic, min_storage, rec_storage, recomendacion_extra
            FROM carrera_pc_componentes
            WHERE id_carrera = %s
        """, (id_carrera,))
        
        # Obtener el resultado de la consulta
        result = self.cursor.fetchone()
        
        # Si no se encuentra un registro, retornar None
        if result is None:
            return None

        # Crear el objeto CarreraPcComponentes con los datos obtenidos
        carrera_componentes = CarreraPcComponentes(
            id_carrera=result[0],
            min_cpu=result[1],
            rec_cpu=result[2],
            min_ram=result[3],
            rec_ram=result[4],
            min_gpu=result[5] if result[5] is not None else "",  # Manejo de valores opcionales
            rec_gpu=result[6] if result[6] is not None else "",
            min_storage=result[7],
            rec_storage=result[8],
            recomendacion_extra=result[9] if result[9] is not None else ""
        )
        
        return carrera_componentes
    
    def save_carrera_pc_componentes(self, carrera: CarreraPcComponentes) -> None:

        # Verificar si la carrera ya existe
        carrera_existente = self.get_carrera_pc_componentes_by_id(carrera.id_carrera)
        if carrera_existente is not None:

            # Actualizar los datos de la carrera
            self.cursor.execute(""" 
                UPDATE carrera_pc_componentes
                SET min_cpu = %s, rec_cpu = %s, min_ram = %s, rec_ram = %s, min_graphic = %s, rec_graphic = %s, min_storage = %s, rec_storage = %s, recomendacion_extra = %s
                WHERE id_carrera = %s
            """, (carrera.min_cpu, carrera.rec_cpu, carrera.min_ram, carrera.rec_ram, carrera.min_gpu, carrera.rec_gpu, carrera.min_storage, carrera.rec_storage, carrera.recomendacion_extra, carrera.id_carrera))
            
            # Confirmar la transacción
            self.conn.commit()

            return None

        # Insertar los datos en la base de datos
        self.cursor.execute("""
            INSERT INTO carrera_pc_componentes (id_carrera, min_cpu, rec_cpu, min_ram, rec_ram, min_graphic, rec_graphic, min_storage, rec_storage, recomendacion_extra)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (carrera.id_carrera, carrera.min_cpu, carrera.rec_cpu, carrera.min_ram, carrera.rec_ram, carrera.min_gpu, carrera.rec_gpu, carrera.min_storage, carrera.rec_storage, carrera.recomendacion_extra))

        # Confirmar la transacción
        self.conn.commit()

    def update_carrera_universitaria(self, carrera: CarreraUniversitaria) -> None:
            
            # Verificar si la carrera ya existe
            carrera_existente = self.get_carrera_universitaria_by_name(carrera.nombre)
            if carrera_existente is None:
                raise Exception("La carrera para editar no existe en la base de datos")
    
            # Actualizar los datos de la carrera
            self.cursor.execute(""" 
                UPDATE carrera_universitaria
                SET area = %s, duracion = %s
                WHERE nombre = %s
            """, (carrera.area, carrera.duracion, carrera.nombre))
            
            # Confirmar la transacción
            self.conn.commit()

    def add_synonym(self, raw_string: str, real_word: str, table_name : str, column_name : str) -> None:
        # si ya existe raw_string en la base de datos, no hacer nada
        self.cursor.execute("""SELECT * FROM synonyms WHERE raw_string = %s""", (raw_string,))
        if self.cursor.fetchone():
            print(f"Se omitio la insercion del sinonimo: {raw_string} porque ya existe en la base de datos")
            return
        
        self.cursor.execute("""
            INSERT INTO synonyms (raw_string, real_word, table_name, column_name)
            VALUES (%s, %s, %s, %s)
        """, (raw_string, real_word, table_name, column_name))

        self.conn.commit()

    def save_carrera_universitaria(self, carrera: CarreraUniversitaria) -> CarreraUniversitaria:

        # Verificar si la carrera ya existe
        carrera_existente = self.get_carrera_universitaria_by_name(carrera.nombre)
        if carrera_existente is not None:
            self.update_carrera_universitaria(carrera)
            return carrera_existente

        # Insertar la carrera en la base de datos
        self.cursor.execute("""
            INSERT INTO carrera_universitaria (nombre, area, duracion)
            VALUES (%s, %s, %s)
            RETURNING id
        """, (carrera.nombre, carrera.area, carrera.duracion))

        # Obtener el id de la carrera insertada
        id_carrera = self.cursor.fetchone()[0]

        # Asignar el id a la carrera
        carrera.id = id_carrera

        # Confirmar la transacción
        self.conn.commit()

        return carrera
    