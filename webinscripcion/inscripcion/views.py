from django.http import HttpResponseRedirect, HttpRequest, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404 
from django.views.generic.edit import CreateView, View
from .models import Alumno, Curp, Alumnogg, Alumno_bajo_tratamiento, Ficha_medica, Ficha_medica_dental, Ficha_medica_visual, Ficha_medica_auditiva, Alumno_convivencia , Aptitud_sobresaliente, Discapacidad, Datos_familiares, Acta_nacimiento, Responsable, Archivo
from .forms import AlumnoForm, AlumnoggForm, ActanForm, AlumnobajotratamientoForm, FichamedicaForm, FichamedicadentalForm, FichamedicavisualForm, FichamedicaauditivaForm, AlumnoconvivenciaForm , AptitudsobresalienteForm, DiscapacidadForm, DatosfamiliaresForm, ResponsableForm, ArchivoForm
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

import os
from django.conf import settings
from django.template import Context
from django.template.loader import get_template
from xhtml2pdf import pisa

# Create your views here.

class AlumnoCreate(CreateView):
	model = Alumno
	template_name = 'inscripcion/alumno_form.html'
	form_class = AlumnoForm
	success_url = reverse_lazy('inscripcion:alumnogg')


class AlumnoggCreate(CreateView):
	model = Alumnogg
	template_name = 'inscripcion/alumnogg_form.html'
	form_class = AlumnoggForm
	success_url = reverse_lazy('inscripcion:actan')


class ActanCreate(CreateView):
	model = Acta_nacimiento
	template_name = 'inscripcion/actan_form.html'
	form_class = ActanForm
	success_url = reverse_lazy('inscripcion:fmedica')

class FichamedicaCreate(CreateView):
	model = Ficha_medica
	template_name = 'inscripcion/fichamedica_form.html'
	form_class = FichamedicaForm
	success_url = reverse_lazy('inscripcion:fmdva')

class FichadvaCreate(CreateView):
	model = Ficha_medica_dental
	second_model=Ficha_medica_auditiva
	third_model=Ficha_medica_visual
	template_name = 'inscripcion/fichamedicadental_form.html'
	form_class = FichamedicadentalForm
	second_form_class= FichamedicaauditivaForm
	third_form_class= FichamedicavisualForm
	success_url = reverse_lazy('inscripcion:tratamiento')


	def get_context_data(self, **kwargs):
		context = super(FichadvaCreate, self).get_context_data(**kwargs)
		if 'form' not in context:
			context['form'] = self.form_class(self.request.GET)
		if 'form2' not in context:
			context['form2'] = self.second_form_class(self.request.GET)
		if 'form3' not in context:
			context['form3'] = self.third_form_class(self.request.GET)
		return context

	def post(self, request, *args, **kwargs):
		self.object = self.get_object
		form = self.form_class(request.POST)
		form2 = self.second_form_class(request.POST)
		form3 = self.third_form_class(request.POST)

		if form.is_valid() and form2.is_valid() and form3.is_valid():
			form.save()
			form2.save()
			form3.save()
			return HttpResponseRedirect(self.get_success_url())
		else:
			return self.render_to_response(self.get_context_data(form=form, form2=form2, form3=form3))


class TratamientoCreate(CreateView):
	model = Alumno_bajo_tratamiento
	template_name = 'inscripcion/alumnobajotratamiento_form.html'
	form_class = AlumnobajotratamientoForm
	success_url = reverse_lazy('inscripcion:discapacidad')

class DiscapacidadCreate(CreateView):
	model = Discapacidad
	template_name = 'inscripcion/discapacidad_form.html'
	form_class = DiscapacidadForm
	success_url = reverse_lazy('inscripcion:familia')


class FamiliaCreate(CreateView):
	model = Aptitud_sobresaliente
	second_model= Datos_familiares
	third_model= Alumno_convivencia
	template_name = 'inscripcion/alumnoconvivencia_form.html'
	form_class = AptitudsobresalienteForm
	second_form_class= DatosfamiliaresForm
	third_form_class= AlumnoconvivenciaForm
	success_url = reverse_lazy('inscripcion:tutor')


	def get_context_data(self, **kwargs):
		context = super(FamiliaCreate, self).get_context_data(**kwargs)
		if 'form' not in context:
			context['form'] = self.form_class(self.request.GET)
		if 'form2' not in context:
			context['form2'] = self.second_form_class(self.request.GET)
		if 'form3' not in context:
			context['form3'] = self.third_form_class(self.request.GET)
		return context

	def post(self, request, *args, **kwargs):
		self.object = self.get_object
		form = self.form_class(request.POST)
		form2 = self.second_form_class(request.POST)
		form3 = self.third_form_class(request.POST)

		if form.is_valid() and form2.is_valid() and form3.is_valid():
			form.save()
			form2.save()
			form3.save()
			return HttpResponseRedirect(self.get_success_url())
		else:
			return self.render_to_response(self.get_context_data(form=form, form2=form2, form3=form3))


	
class ResponsableCreate(CreateView):
	model= Responsable
	template_name = 'inscripcion/responsable_form.html'
	form_class = ResponsableForm
	success_url = reverse_lazy('inscripcion:tutor')


class ArchivoCreate(CreateView):
	model= Archivo
	template_name = 'inscripcion/archivo_form.html'
	form_class = ArchivoForm
	success_url = reverse_lazy('home')

class SaleInvoicePdfView(View):

    def link_callback(self, uri, rel):
        """
        Convert HTML URIs to absolute system paths so xhtml2pdf can access those
        resources
        """
        # use short variable names
        sUrl = settings.STATIC_URL  # Typically /static/
        sRoot = settings.STATIC_ROOT  # Typically /home/userX/project_static/
        mUrl = settings.MEDIA_URL  # Typically /static/media/
        mRoot = settings.MEDIA_ROOT  # Typically /home/userX/project_static/media/

        # convert URIs to absolute system paths
        if uri.startswith(mUrl):
            path = os.path.join(mRoot, uri.replace(mUrl, ""))
        elif uri.startswith(sUrl):
            path = os.path.join(sRoot, uri.replace(sUrl, ""))
        else:
            return uri  # handle absolute uri (ie: http://some.tld/foo.png)

        # make sure that file exists
        if not os.path.isfile(path):
            raise Exception(
                'media URI must start with %s or %s' % (sUrl, mUrl)
            )
        return path



    def get(self, request, *args, **kwargs):
        try:
            template = get_template('inscripcion/invoice.html')
            context = {
				'curp': Curp.objects.get(pk=self.kwargs['pk']),
				'icon': '{}{}'.format(settings.STATIC_URL, 'core/images/SEV.png')
			}
            html = template.render(context)
            response = HttpResponse(content_type='application/pdf')
            #response['Content-Disposition'] = 'attachment; filename="report.pdf"'
            pisaStatus = pisa.CreatePDF(
                html, dest=response,
                link_callback=self.link_callback
            )
            return response
        except:
            pass
        return HttpResponseRedirect(reverse_lazy('home'))
