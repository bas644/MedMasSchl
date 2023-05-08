from django.db import models

class Rooms(models.Model):
	number = models.CharField('Room Number', max_length=6)
	available = models.BooleanField(default=True)

	def __str__(self):
		return self.number


class Therapists(models.Model):
	first_name = models.CharField('First Name', max_length=100)
	last_name = models.CharField('Last Name', max_length=100)
	disp_name = models.CharField('Display Name', max_length=200, blank=True, null=True)
	studentID = models.CharField('Student ID', max_length=10)
	email = models.EmailField('Email Address', blank=True, null=True)
	c_phone = models.CharField('Cell Phone', max_length=14, blank=True, null=True)
	schedule = models.DateTimeField('Schedule', blank=True, null=True)

	def __str__(self):
		return self.disp_name


class Clients(models.Model):
	first_name = models.CharField('First Name', max_length=100)
	last_name = models.CharField('Last Name', max_length=100)
	disp_name = models.CharField('Display Name', max_length=200, blank=True, null=True)
	email = models.EmailField('Email Address', blank=True, null=True)
	c_phone = models.CharField('Cell Phone', max_length=14, blank=True, null=True)
	notes = models.TextField(blank=True)

	def __str__(self):
		return self.first_name + ' ' + self.last_name


class Apptmnts(models.Model):
	client_name = models.ForeignKey(Clients, on_delete=models.DO_NOTHING)
	therapist_name = models.ForeignKey(Therapists, on_delete=models.DO_NOTHING)
	appt_date = models.DateTimeField('Appointment Date')
	room = models.ForeignKey(Rooms, on_delete=models.DO_NOTHING)

	def __str__(self):
		return self.client_name.last_name


class School_Staff(models.Model):
	first_name = models.CharField('First Name', max_length=100)
	last_name = models.CharField('Last Name', max_length=100)
	disp_name = models.CharField('Display Name', max_length=200, blank=True, null=True)
	email = models.EmailField('Email Address', blank=True, null=True)
	c_phone = models.CharField('Cell Phone', max_length=14, blank=True, null=True)

	def __str__(self):
		return self.disp_name