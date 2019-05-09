from django.contrib import admin
from .models import Faculdade, Departamento, Curso, UnidadeCurricular, Turno, Aula, Presenca, AlunoAulaUC, ProfessorAula
# Register your models here.
admin.site.register(Faculdade)
admin.site.register(Departamento)
admin.site.register(Curso)
admin.site.register(UnidadeCurricular)
admin.site.register(Turno)
admin.site.register(Aula)
admin.site.register(Presenca)
admin.site.register(AlunoAulaUC)
admin.site.register(ProfessorAula)
