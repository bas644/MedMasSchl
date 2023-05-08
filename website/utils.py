from datetime import datetime, timedelta
from calendar import HTMLCalendar
from .models import Apptmnts, Rooms


class Calendar(HTMLCalendar):
	def __init__(self, year=None, month=None):
		self.year = year
		self.month = month
		super(Calendar, self).__init__()

	# add room schedules to the mix
	def roomschedule(self, events_per_day, day):
		today = 1
		if day:
			today = day
		now = datetime.now()
		openinghour = 8
		closinghour = 21
		hours = closinghour - openinghour
		opening = now.replace(day=today, hour=openinghour, minute=0, second=0, microsecond=0)
		closing = now.replace(day=today, hour=closinghour, minute=0, second=0, microsecond=0)
		loopinghour = openinghour
		rooms = Rooms.objects.all()
		rms = f'<div class="table-responsive">\n'
		rms = f'<table border="0" cellpadding="0" cellspacing="0" class="table">\n'
		rms += f'<thead>\n'
		rms += f'<tr>\n'
		for room in rooms:
			if room.available:
				rms += f'<th scope="col">{room.number}</th>\n'
		rms += f'</tr>\n'
		rms += f'</thead>\n'
		rms += f'<tbody>\n'
		l = []
		d = {}
		if events_per_day:
			for event in events_per_day:
				l.append((event.room.number, event.appt_date.time()))
				d[f'({event.room.number}, {event.appt_date.time()})'] = [event.client_name.last_name, event.pk]
		for hour in range(hours):
			loopinghour = now.replace(day=today, hour=openinghour+hour, minute=0, second=0, microsecond=0)
			rms += f'<tr>\n'
			rpk = 0
			for room in rooms:
				rpk += 1
				if room.available:
					if (room.number, loopinghour.time()) in l:
						name = d[f'({room.number}, {loopinghour.time()})'][0]
						pk = d[f'({room.number}, {loopinghour.time()})'][1]
						rms += f'<td class="room" style="background-color:rgb(255, 199, 206);"><a href="/appt_dtls/{pk}">{name}</a></td>\n'
					else:
						rms += f'<td class="room" style="background-color:rgb(198, 239, 206);"><a href="/add_appt/{rpk}/{loopinghour}">{loopinghour.time()}</a></td>\n'
			rms += f'</tr>\n'
		rms += f'</tbody>\n'
		rms += f'</table>\n'
		rms += f'</div>\n'
		return rms
		

	# formats a day as a td
	# filter events by day
	def formatday(self, day, events):
		events_per_day = events.filter(appt_date__day=day)
		d = self.roomschedule(events_per_day, day)

		if day != 0:
			return f"<td><span class='date'>{day}</span> {d} </td>"
		return '<td></td>'

	# formats a week as a tr 
	def formatweek(self, theweek, events):
		week = ''
		for d, weekday in theweek:
			week += self.formatday(d, events)
		return f'<tr> {week} </tr>'

	# formats a month as a table
	# filter events by year and month
	def formatmonth(self, withyear=True):
		events = Apptmnts.objects.filter(appt_date__year=self.year, appt_date__month=self.month)

		cal = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
		cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
		cal += f'{self.formatweekheader()}\n'
		for week in self.monthdays2calendar(self.year, self.month):
			cal += f'{self.formatweek(week, events)}\n'
		return cal