#coding=utf-8
from django.shortcuts import render
from report.models import Report
from django.views.generic import View, ListView
from forms import ReportForm

class HomeView(View):

    def get(self, request):
        """
        Esta función devuelve el home de la página
        """
        return render(request, 'report/home.html', {})


class CreateView(View):

    def get(self, request):
        """
        Muestra un formulario para crear una denuncia y la crea si la petición es POST
        """
        succes_message = ''
        form = ReportForm()
        context = {
            'form': form,
            'success_message': succes_message
        }
        return render(request, 'report/new_report.html', context)

    def post(self, request):
        """
        Aquí entra si la petición es POST (como debe ser)
        """
        success_message = ''
        report = Report()
        form = ReportForm(request.POST, instance=report)

        if form.is_valid():
            new_report = form.save()
            form = ReportForm
            success_message = u'Tu denuncia ha sido guardada con éxito!'

        context = {
            'form': form,
            'success_message': success_message
        }
        return render(request, 'report/new_report.html', context)
