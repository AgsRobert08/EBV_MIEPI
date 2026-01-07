from django.urls import path
from django.contrib.auth.views import LogoutView
from django.views.generic import TemplateView
from . import views

app_name = 'miepi'

urlpatterns = [
    path('', views.login_view, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', LogoutView.as_view(next_page='miepi:login'), name='logout'),

    #Inscripciones
    path('inscrito/create/', views.InscritoCreateView.as_view(), name='inscrito_create'),
    path('inscritos/', views.InscritosListView.as_view(), name='inscritos_list'),
    path('inscritos/eliminar/<int:id>/',views.eliminar_registros,name='eliminar_registros'),
    path('inscritos/editar/<int:pk>/', views.InscritoUpdateView.as_view(), name='editar_inscrito'),
    path('inscritos/pdf/',views.RegistrosPDFView.as_view(),name='inscritos_pdf'),

    #Pase de lista
    path('asistencia/escanear/',views.escanear_asistencia,name='escanear_asistencia'),
    path('asistencia/registrar/', views.registrar_asistencia, name='registrar_asistencia'),

    #Lista de Asistencias
    path('asistencia/lista/',views.AsistenciasListView.as_view(),name='lista_asistencias'),
    path('asistencias/pdf/',views.AsistenciaPDFView.as_view(),name='asistencias_pdf'),
    path('asistencia/eliminar/<int:id>/',views.eliminar_asistencia,name='eliminar_asistencia'),
    path('buscar-inscrito/', views.buscar_inscrito, name='buscar_inscrito'), 


]