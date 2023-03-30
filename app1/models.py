from django.db import models
from django.core.validators import FileExtensionValidator


class Fe_b(models.Model):
    title= models.CharField(max_length=100)
    pdf=models.FileField(upload_to='FE/',validators=[FileExtensionValidator(["pdf"])])
    image = models.ImageField(upload_to='img/')
    
    def __str__(self):
        return self.title

# cs course start#

class cs_Decode(models.Model):
    title= models.CharField(max_length=100)
    pdf=models.FileField(upload_to='cs_decode/',validators=[FileExtensionValidator(["pdf"])])
    image = models.ImageField(upload_to='img/')
    
    def __str__(self):
        return self.title

class cs_SE(models.Model):
    title= models.CharField(max_length=100)
    pdf=models.FileField(upload_to='cs_SE/',validators=[FileExtensionValidator(["pdf"])])
    image = models.ImageField(upload_to='img/')
    
    def __str__(self):
        return self.title


class cs_TE(models.Model):
    title= models.CharField(max_length=100)
    pdf=models.FileField(upload_to='cs_TE/',validators=[FileExtensionValidator(["pdf"])])
    image = models.ImageField(upload_to='img/')
    
    def __str__(self):
        return self.title


class cs_BE(models.Model):
    title= models.CharField(max_length=100)
    pdf=models.FileField(upload_to='cs_BE/',validators=[FileExtensionValidator(["pdf"])])
    image = models.ImageField(upload_to='img/')
    
    def __str__(self):
        return self.title
# Aids couse

class Aids_Decode(models.Model):
    title= models.CharField(max_length=100)
    pdf=models.FileField(upload_to='Aids_decode/',validators=[FileExtensionValidator(["pdf"])])
    image = models.ImageField(upload_to='img/')
    
    def __str__(self):
        return self.title

class Aids_SE(models.Model):
    title= models.CharField(max_length=100)
    pdf=models.FileField(upload_to='Aids_SE/',validators=[FileExtensionValidator(["pdf"])])
    image = models.ImageField(upload_to='img/')
    
    def __str__(self):
        return self.title


class Aids_TE(models.Model):
    title= models.CharField(max_length=100)
    pdf=models.FileField(upload_to='Aids_TE/',validators=[FileExtensionValidator(["pdf"])])
    image = models.ImageField(upload_to='img/')
    
    def __str__(self):
        return self.title


class Aids_BE(models.Model):
    title= models.CharField(max_length=100)
    pdf=models.FileField(upload_to='Aids_BE/',validators=[FileExtensionValidator(["pdf"])])
    image = models.ImageField(upload_to='img/')
    
    def __str__(self):
        return self.title


# It couse



class It_Decode(models.Model):
    title= models.CharField(max_length=100)
    pdf=models.FileField(upload_to='It_decode/',validators=[FileExtensionValidator(["pdf"])])
    image = models.ImageField(upload_to='img/')
    
    def __str__(self):
        return self.title

class It_SE(models.Model):
    title= models.CharField(max_length=100)
    pdf=models.FileField(upload_to='It_SE/',validators=[FileExtensionValidator(["pdf"])])
    image = models.ImageField(upload_to='img/')
    
    def __str__(self):
        return self.title


class It_TE(models.Model):
    title= models.CharField(max_length=100)
    pdf=models.FileField(upload_to='It_TE/',validators=[FileExtensionValidator(["pdf"])])
    image = models.ImageField(upload_to='img/')
    
    def __str__(self):
        return self.title


class It_BE(models.Model):
    title= models.CharField(max_length=100)
    pdf=models.FileField(upload_to='It_BE/',validators=[FileExtensionValidator(["pdf"])])
    image = models.ImageField(upload_to='img/')
    
    def __str__(self):
        return self.title

# Etc couse



class Etc_Decode(models.Model):
    title= models.CharField(max_length=100)
    pdf=models.FileField(upload_to='Etc_decode/',validators=[FileExtensionValidator(["pdf"])])
    image = models.ImageField(upload_to='img/')
    
    def __str__(self):
        return self.title

class Etc_SE(models.Model):
    title= models.CharField(max_length=100)
    pdf=models.FileField(upload_to='Etc_SE/',validators=[FileExtensionValidator(["pdf"])])
    image = models.ImageField(upload_to='img/')
    
    def __str__(self):
        return self.title


class Etc_TE(models.Model):
    title= models.CharField(max_length=100)
    pdf=models.FileField(upload_to='Etc_TE/',validators=[FileExtensionValidator(["pdf"])])
    image = models.ImageField(upload_to='img/')
    
    def __str__(self):
        return self.title


class Etc_BE(models.Model):
    title= models.CharField(max_length=100)
    pdf=models.FileField(upload_to='Etc_BE/',validators=[FileExtensionValidator(["pdf"])])
    image = models.ImageField(upload_to='img/')
    
    def __str__(self):
        return self.title

# Mech couse



class Mech_Decode(models.Model):
    title= models.CharField(max_length=100)
    pdf=models.FileField(upload_to='Mech_decode/',validators=[FileExtensionValidator(["pdf"])])
    image = models.ImageField(upload_to='img/')
    
    def __str__(self):
        return self.title

class Mech_SE(models.Model):
    title= models.CharField(max_length=100)
    pdf=models.FileField(upload_to='Mech_SE/',validators=[FileExtensionValidator(["pdf"])])
    image = models.ImageField(upload_to='img/')
    
    def __str__(self):
        return self.title


class Mech_TE(models.Model):
    title= models.CharField(max_length=100)
    pdf=models.FileField(upload_to='Mech_TE/',validators=[FileExtensionValidator(["pdf"])])
    image = models.ImageField(upload_to='img/')
    
    def __str__(self):
        return self.title


class Mech_BE(models.Model):
    title= models.CharField(max_length=100)
    pdf=models.FileField(upload_to='Mech_BE/',validators=[FileExtensionValidator(["pdf"])])
    image = models.ImageField(upload_to='img/')
    
    def __str__(self):
        return self.title


# civil couse



class civil_Decode(models.Model):
    title= models.CharField(max_length=100)
    pdf=models.FileField(upload_to='civil_decode/',validators=[FileExtensionValidator(["pdf"])])
    image = models.ImageField(upload_to='img/')
    
    def __str__(self):
        return self.title

class civil_SE(models.Model):
    title= models.CharField(max_length=100)
    pdf=models.FileField(upload_to='civil_SE/',validators=[FileExtensionValidator(["pdf"])])
    image = models.ImageField(upload_to='img/')
    
    def __str__(self):
        return self.title


class civil_TE(models.Model):
    title= models.CharField(max_length=100)
    pdf=models.FileField(upload_to='civil_TE/',validators=[FileExtensionValidator(["pdf"])])
    image = models.ImageField(upload_to='img/')
    
    def __str__(self):
        return self.title


class civil_BE(models.Model):
    title= models.CharField(max_length=100)
    pdf=models.FileField(upload_to='civil_BE/',validators=[FileExtensionValidator(["pdf"])])
    image = models.ImageField(upload_to='img/')
    
    def __str__(self):
        return self.title


class Q_p(models.Model):
    
    year=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    pdf=models.FileField(upload_to='Q_paper/',validators=[FileExtensionValidator(["pdf"])])
    def __str__(self):
        return self.name

