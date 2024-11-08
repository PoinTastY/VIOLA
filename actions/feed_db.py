from actions.infrastructure.repos.career_components_repo import CareerComponentsRepo
from actions.domain.entities.carrera_pc_componentes import CarreraPcComponentes
from actions.domain.entities.carrera_universitaria import CarreraUniversitaria
import pandas as pd

if __name__ == '__main__':
    repo = CareerComponentsRepo()

    excel_path = "C:\\Users\\kbece\\Downloads\\Base de Conocimiento Experto Chatbot.xlsx"

    df = pd.read_excel(excel_path, engine="openpyxl")

    carrera_universitaria = CarreraUniversitaria(nombre="Cine", 
                                                 area="Artes", 
                                                 duracion=4)
    
    for _, row in df.iterrows():
    # Crear instancia de CarreraUniversitaria
        carrera_universitaria = CarreraUniversitaria(
            nombre=row['nombre'],
            area=row['area'],
            duracion=row['duracion']
        )

        try:
            # Guardar carrera universitaria
            carrera_universitaria = repo.save_carrera_universitaria(carrera_universitaria)
            if carrera_universitaria.id != 0:
                print(f"Se ha guardado o actualizado la carrera universitaria: {carrera_universitaria}")
                
                # Crear instancia de CarreraPcComponentes usando los datos de la fila
                carrera_pc_componentes = CarreraPcComponentes(
                    id_carrera=carrera_universitaria.id,
                    min_cpu=row['min_cpu'],
                    rec_cpu=row['rec_cpu'],
                    min_ram=row['min_ram'],
                    rec_ram=row['rec_ram'],
                    min_storage=row['min_storage'],
                    rec_storage=row['rec_storage'],
                    min_gpu=row['min_graphic'],
                    rec_gpu=row['rec_graphic'],
                    recomendacion_extra=row['recomendacion_extra'] if 'recomendacion_extra' in row else ""
                )
                
                # Guardar componentes de la carrera
                repo.save_carrera_pc_componentes(carrera_pc_componentes)

                #make a list from the column synonyms, wich contains a string with the synonyms separated by commas
                synonyms = row['synonyms'].split(",") if 'synonyms' in row else []

                # try to add each synonym to the database
                for synonym in synonyms:
                    try:
                        repo.add_synonym(synonym, carrera_universitaria.nombre, "carrera_universitaria", "nombre")
                    except Exception as e:
                        print(f"Error al añadir el sinónimo: {synonym}, {e}")
        
        except Exception as e:
            print(f"Error al guardar la carrera universitaria ({carrera_universitaria.nombre}) o sus componentes: {e}")