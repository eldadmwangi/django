
from django.conf.urls import url
from django.contrib import admin

from django.urls import path, include


#configure all our urls here
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls'))
]







#urlpatterns = [
#    url(r'^admin/', admin.site.urls),
 #   url('', home),

#]