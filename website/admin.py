from django.contrib import admin
from .models import Rooms
from .models import Therapists
from .models import Clients
from .models import Apptmnts

admin.site.register(Rooms)
admin.site.register(Therapists)
admin.site.register(Clients)
admin.site.register(Apptmnts)
