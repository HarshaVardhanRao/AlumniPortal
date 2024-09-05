from django.contrib import admin
from portalapp.models import alumniUser,Department,alumniInfo,events,job_list

admin.site.register(alumniUser)
admin.site.register(Department)
admin.site.register(alumniInfo)
admin.site.register(events)
admin.site.register(job_list)

