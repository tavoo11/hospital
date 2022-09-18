from django.contrib import admin
from .models.usuario import Usuario
from .models.paciente import Paciente
from .models.auxiliar import Auxiliar
from .models.famiPacinete import FamiPaciente
from .models.medico import Medico 
from .models.signosVitales import SignosVitales

admin.site.register(Usuario)
admin.site.register(Paciente)
admin.site.register(Auxiliar)
admin.site.register(FamiPaciente)
admin.site.register(Medico)
admin.site.register(SignosVitales)
# Register your models here.
