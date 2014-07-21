# -*- encoding: utf-8 -*-
from django.shortcuts import render
from programaciones.models import Programacion
from horarios_programacion.models import HorarioProgramacion
from franjas.models import Franja
from datetime import date
from paginas.models import Pagina
import datetime

def programacion_view(request):
	pagina = Pagina.objects.get(id=21)
	fechaActual = date.today()
	horariosProgramacion = HorarioProgramacion.objects.filter().order_by('manana')
	fechaPrimerDiaSemana = getFechaPrimerDiaSemana(fechaActual)
	programacionCompletaSemana = []
	fechasSemana = []
	# Trae la programacion de los 7 dias de la semana
	for i in range(7):
		# Cadenas para encabezados por dia
		fechaDia = fechaPrimerDiaSemana + datetime.timedelta(days=i)
		strFecha = getDia(fechaDia) + "<br>" + fechaDia.strftime("%d") + " de " + getMes(fechaDia)
		fechasSemana.append(strFecha)
		#Trae la programacion del dia (puede traer horas sin programas)
		programacionDia = Programacion.objects.filter(fecha=fechaDia)

		# se trae el listado de horas con programacion
		horasProgramadasDia = Programacion.objects.filter(fecha=fechaDia).values_list('horario__manana',flat=True)

		# Se completa la programacion del dia incluyendo programas vacios para un renderizado correcto
		sinFranjaAsignada = Franja.objects.get(nombre="Sin Franja Asignada")
		programacionCompletaDia = []
		for horario in horariosProgramacion:
			if horario.manana in horasProgramadasDia:
				programa = programacionDia.get(horario=horario)
				programa.programa = programa.programa + "\nFranja: " + programa.franja.nombre
			else:
				programa = Programacion(fecha=fechaDia, horario=horario, programa="",franja=sinFranjaAsignada)
			programacionCompletaDia.append(programa)			
		programacionCompletaSemana.append(programacionCompletaDia)

	fechaUltimoDiaSemana = fechaPrimerDiaSemana + datetime.timedelta(days=6)
	descripcionSemana = "Semana del " + fechaPrimerDiaSemana.strftime("%d") + " de " + getMes(fechaPrimerDiaSemana) + \
						" al " + fechaUltimoDiaSemana.strftime("%d") + " de " + getMes(fechaUltimoDiaSemana) + " de " + \
						fechaUltimoDiaSemana.strftime("%Y")
	zippedProgramacion = zip(fechasSemana, programacionCompletaSemana)

	ctx = {
		"descripcionSemana":descripcionSemana,
		"horariosProgramacion":horariosProgramacion,
		"zippedProgramacion":zippedProgramacion,
		'pagina':pagina,
	}
	return render(request, 'home/programacion.html',ctx)

def getDia(fecha):
	dicDias = {
		'MONDAY':'Lunes',
		'TUESDAY':'Martes',
		'WEDNESDAY':'Miércoles',
		'THURSDAY':'Jueves',
		'FRIDAY':'Viernes',
		'SATURDAY':'Sábado',
		'SUNDAY':'Domingo',
	}
	return dicDias[fecha.strftime('%A').upper()]

def getFechaPrimerDiaSemana(fecha):
	diaActual = getDia(fecha)
	dicDiferenciaDiasInicioSemana = {
		'Lunes':0,
		'Martes':-1,
		'Miércoles':-2,
		'Jueves':-3,
		'Viernes':-4,
		'Sábado':-5,
		'Domingo':-6,
	}
	diferenciaDias = dicDiferenciaDiasInicioSemana[diaActual]
	return fecha + datetime.timedelta(days=diferenciaDias)

def getMes(fecha):
	dicMeses = {
		'January':'Enero',
		'February':'Febrero',
		'March':'Marzo',
		'April':'Abril',
		'May':'Mayo',
		'June':'Junio',
		'July':'Julio',
		'August':'Agosto',
		'September':'Septiembre',
		'October':'Octubre',
		'November':'Noviembre',
		'December':'Diciembre',
	}
	return dicMeses[fecha.strftime('%B')]
