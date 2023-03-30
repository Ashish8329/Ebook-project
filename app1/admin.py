from django.contrib import admin
from .models import Fe_b,cs_Decode,cs_SE,cs_TE,cs_BE
from .models import Aids_Decode,Aids_SE,Aids_TE,Aids_BE
from .models import It_Decode,It_SE,It_TE,It_BE
from .models import Etc_Decode,Etc_SE,Etc_TE,Etc_BE

from .models import civil_Decode,civil_SE,civil_TE,civil_BE
from .models import Mech_Decode,Mech_SE,Mech_TE,Mech_BE
from .models import Q_p


# Register your models here.
admin.site.register(Fe_b)
admin.site.register(Q_p)

#cs books table
 
admin.site.register(cs_SE)
admin.site.register(cs_TE)
admin.site.register(cs_BE)
admin.site.register(cs_Decode)


#Aids books table
 
admin.site.register(Aids_SE)
admin.site.register(Aids_TE)
admin.site.register(Aids_BE)
admin.site.register(Aids_Decode)

#It books table
 
admin.site.register(It_SE)
admin.site.register(It_TE)
admin.site.register(It_BE)
admin.site.register(It_Decode)

#Etc books table
 
admin.site.register(Etc_SE)
admin.site.register(Etc_TE)
admin.site.register(Etc_BE)
admin.site.register(Etc_Decode)

#civil books table
 
admin.site.register(civil_SE)
admin.site.register(civil_TE)
admin.site.register(civil_BE)
admin.site.register(civil_Decode)

#Mech books table
 
admin.site.register(Mech_SE)
admin.site.register(Mech_TE)
admin.site.register(Mech_BE)
admin.site.register(Mech_Decode)