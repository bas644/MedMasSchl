from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from .models import Apptmnts
from .utils import Calendar
from .forms import ApptForm
from django.http import HttpResponseRedirect


def home(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
	name = 'Steve'
	month = month.title()

	# Convert month from name to number
	month_number = list(calendar.month_name).index(month)
	month_number = int(month_number)

	# Create the calendar
	cal = HTMLCalendar().formatmonth(
		year,
		month_number)

	return render(request,
		'website/home.html',
		{
		'name':name,
		'year':year,
		'month':month,
		'month_number':month_number,
		'cal':cal,
		})

def all_appts(request):
	appt_list = Apptmnts.objects.all()
	return render(request, 'website/appt_list.html', {'appt_list':appt_list})


def appt_dtls(request, pk):
	appt = Apptmnts.objects.get(pk=pk)
	return render(request, 'website/appt_dtls.html', {'appt':appt})


def add_appt(request, room=None, dt=None):
	submitted = False
	if request.method == "POST":
		form = ApptForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/add_appt?submitted=True')
	else:
		form = ApptForm(initial={'appt_date':dt, 'room':room})
		if 'submitted' in request.GET:
			submitted = True
	return render(request, 'website/add_appt.html', {'form':form, 'submitted':submitted})


class CalendarView(generic.ListView):
    model = Apptmnts
    template_name = 'website/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # use today's date for the calendar
        d = get_date(self.request.GET.get('day', None))

        # Instantiate our calendar class with today's year and date
        cal = Calendar(d.year, d.month)

        # Call the formatmonth method, which returns our calendar as a table
        html_cal = cal.formatmonth(withyear=True)
        # context['calendar'] = mark_safe(html_cal)
        context['calendar'] = html_cal
        return context

def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()