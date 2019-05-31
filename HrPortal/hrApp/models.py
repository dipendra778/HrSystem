from django.db import models
from multiselectfield import MultiSelectField

#---------------------------------------------------------
#====================Model For Job Form============================
class ApplicationModel(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    phone=models.CharField(max_length=20)
    #================Model For File and Image======================
    CvResume=models.FileField(blank=True)
    #================Choice Field For CheckBox=====================
    BATCH_CHOICE=(('Quality Assurence','Quality Assurence'),('Developer','Developer'),('Project Manager','Project Manager'),('Data Analyst','Data Analyst'),('Front End(UI/UX)','Front End(UI/UX)'))
    catagory=MultiSelectField(choices=BATCH_CHOICE,max_length=200)
    motivation=models.CharField(max_length=1000)

    def __str__(self):
        return self.name
