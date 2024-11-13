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
                    min_cpu=row['min_cpu'] if pd.notna(row['min_cpu']) else "",
                    rec_cpu=row['rec_cpu'] if pd.notna(row['rec_cpu']) else "",
                    min_ram=row['min_ram'] if pd.notna(row['min_ram']) else "",
                    rec_ram=row['rec_ram'] if pd.notna(row['rec_ram']) else "",
                    min_storage=row['min_storage'] if pd.notna(row['min_storage']) else "",
                    rec_storage=row['rec_storage'] if pd.notna(row['rec_storage']) else "",
                    min_gpu=row['min_graphic'] if pd.notna(row['min_graphic']) else "",
                    rec_gpu=row['rec_graphic'] if pd.notna(row['rec_graphic']) else "",
                    recomendacion_extra=row['recomendacion_extra'] if 'recomendacion_extra' in row and pd.notna(row['recomendacion_extra']) else ""
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