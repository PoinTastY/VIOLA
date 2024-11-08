class CarreraPcComponentes:
    def __init__(self, id_carrera: int = 0, min_cpu: str = "", rec_cpu: str = "", min_ram: str = "", rec_ram: str = "", min_gpu: str = "",
                 rec_gpu: str = "", min_storage: str = "", rec_storage: str = "", recomendacion_extra: str = ""):
        
        self.id_carrera = id_carrera
        self.min_cpu = min_cpu
        self.rec_cpu = rec_cpu
        self.min_ram = min_ram
        self.rec_ram = rec_ram
        self.min_gpu = min_gpu
        self.rec_gpu = rec_gpu
        self.min_storage = min_storage
        self.rec_storage = rec_storage
        self.recomendacion_extra = recomendacion_extra

    def __repr__(self):
        return (f"CarreraPcComponentes(id_carrera={self.id_carrera}, min_cpu='{self.min_cpu}', rec_cpu='{self.rec_cpu}', "
                f"min_ram='{self.min_ram}', rec_ram='{self.rec_ram}', min_gpu='{self.min_gpu}', rec_gpu='{self.rec_gpu}', "
                f"min_storage='{self.min_storage}', rec_storage='{self.rec_storage}', recomendacion_extra='{self.recomendacion_extra}')")