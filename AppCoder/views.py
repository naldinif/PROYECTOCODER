from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.models import Curso, Profesor, Estudiante, Entregable
from AppCoder.forms import CursoFormulario, ProfesorFormulario, EstudianteFormulario, EntregableFormulario

# Create your views here.
def curso(self):
    curso = Curso(nombre='Desarrollo Web', camada='19881')
    curso.save()

    documentodeTexto = f'---->Curso: {curso.nombre} Camada: {curso.camada}'

    return HttpResponse(documentodeTexto)


def inicio(request):
    return render(request, 'inicio.html')



def cursos(request):
    if request.method == "POST":
        miFormulario = CursoFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            
            curso = Curso(nombre=informacion['nombre'], camada=informacion['camada'])
            curso.save()
            
            mensaje = "Formulario enviado con éxito"  # Mensaje a mostrar
            return render(request, 'cursos.html', {"miFormulario": miFormulario, "mensaje": mensaje})

    else:
        miFormulario = CursoFormulario()

    return render(request, 'cursos.html', {"miFormulario": miFormulario})





def profesores(request):
    if request.method == "POST":
        miFormulario = ProfesorFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            profesor = Profesor(nombre=informacion['nombre'], 
                                apellido=informacion['apellido'],
                                email=informacion['email'],
                                profesion=informacion['profesion'])
            profesor.save()

            mensaje = "Formulario enviado con éxito"  # Mensaje a mostrar
            return render(request, 'profesorFormulario.html', {'miFormulario': miFormulario, 'mensaje': mensaje})

    else:
        miFormulario = ProfesorFormulario()

    return render(request, 'profesorFormulario.html', {'miFormulario': miFormulario})


def estudiantes(request):
    if request.method == "POST":
        miFormulario = EstudianteFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            estudiante = Estudiante(nombre=informacion['nombre'], 
                                apellido=informacion['apellido'],
                                email=informacion['email'])
            estudiante.save()

            mensaje = "Formulario enviado con éxito"  # Mensaje a mostrar
            return render(request, 'estudianteFormulario.html', {'miFormulario': miFormulario, 'mensaje': mensaje})

    else:
        miFormulario = EstudianteFormulario()

    return render(request, 'estudianteFormulario.html', {'miFormulario': miFormulario})


def entregables(request):
    if request.method == "POST":
        miFormulario = EntregableFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            entregable = Entregable(entrega=informacion['entrega'])
            entregable.save()

            mensaje = "Formulario enviado con éxito"  # Mensaje a mostrar
            return render(request, 'entregableFormulario.html', {'miFormulario': miFormulario, 'mensaje': mensaje})

    else:
        miFormulario = EntregableFormulario()

    return render(request, 'entregableFormulario.html', {'miFormulario': miFormulario})



def busquedaCamada(request):
    return render(request, 'busquedaCamada.html')






def buscar(request):
    if request.GET['camada']:

        #respuesta = f"Estoy buscando la Camada nro.: {request.GET['camada']}"
        camada = request.GET['camada']
        cursos = Curso.objects.filter(camada__icontains=camada)

        return render(request, 'resultadosBusqueda.html', {'cursos':cursos, 'camada':camada})
    
    else:
        respuesta = "No enviaste datos."

    #return HttpResponse(respuesta)
    return render(request, 'resultadosBusqueda.html', {'respuesta':respuesta})



def leerProfesores(request):
    profesores = Profesor.objects.all() #trae todos los profes.
    contexto = {'profesores':profesores}

    return render(request, 'leerProfesores.html', contexto)





def eliminarProfesor(request, profesor_nombre):
    profesor = Profesor.objects.get(nombre=profesor_nombre)
    profesor.delete()

    profesores = Profesor.objects.all()
    contexto = {'profesores':profesores}

    return render(request, 'leerProfesores.html', contexto)




def editarProfesor(request, profesor_nombre):
    profesor = Profesor.objects.get(nombre=profesor_nombre)

    if request.method == "POST":
        miFormulario = ProfesorFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data

            profesor.nombre = informacion['nombre']
            profesor.apellido = informacion['apellido']
            profesor.email = informacion['email']
            profesor.profesion = informacion['profesion']

            profesor.save()

            return render(request, 'inicio.html')
    else:
        miFormulario = ProfesorFormulario(initial={'nombre':profesor.nombre, 'apellido':profesor.apellido,
                                                   'email':profesor.email, 'profesion': profesor.profesion})
        
    return render(request, 'editarProfesor.html', {'miFormulario':miFormulario, 'profesor_nombre':profesor_nombre})
