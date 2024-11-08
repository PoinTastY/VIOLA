from actions.infrastructure.repos.career_components_repo import CareerComponentsRepo
from actions.domain.entities.carrera_pc_componentes import CarreraPcComponentes
from actions.domain.entities.carrera_universitaria import CarreraUniversitaria

if __name__ == '__main__':
    repo = CareerComponentsRepo()

    carrera_universitaria = CarreraUniversitaria(nombre="Cine", 
                                                 area="Artes", 
                                                 duracion=4)
    
    
    try:
        carrera_universitaria = repo.save_carrera_universitaria(carrera_universitaria)
        if carrera_universitaria.id != 0:
            print(f"Se ha guardado la carrera universitaria: {carrera_universitaria}")
            carrera_pc_componentes = CarreraPcComponentes(id_carrera=1,
                                                        recomendacion_extra="No es necesaria una tarjeta grafica dedicada, con la integrada es suficiente, y esos componentes son suficientes para emular ;)",)
            repo.save_carrera_pc_componentes(carrera_pc_componentes)
            print(f"Se ha guardado los componentes de la carrera: {carrera_pc_componentes}")

        carrera_pc_componentes.id_carrera = carrera_universitaria.id
    except Exception as e:
        print(f"Error al guardar la carrera universitaria: {e}")