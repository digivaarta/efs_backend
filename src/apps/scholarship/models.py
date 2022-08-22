from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class UserScholarshipTaskStatud(models.TextChoices):

    PENDING = "pending","Pending"
    APPROVED = "approved","Approved"
    REJECT = "reject","Reject"


class Scholarship(models.Model):
    user = models.ForeignKey("account.User",related_name="user_scholarship",on_delete=models.CASCADE)
    title = models.TextField(max_length=500)
    content = RichTextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.title

class ScholarshipTask(models.Model):
    scholarship = models.ForeignKey("scholarship.Scholarship",related_name="sch_scholarship",on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    minimum_age = models.IntegerField(default=0)
    maximum_age = models.IntegerField(default=0)
    start_date = models.DateField(blank=True,null=True)
    end_date = models.DateField(blank=True,null=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.title

class ScholarshipSubTask(models.Model):
    scholarship_task = models.ForeignKey("scholarship.ScholarshipTask",related_name="sch_scholarship_task",on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    creation_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.title


class UserScholarshipTask(models.Model):
    user = models.ForeignKey("account.User",related_name="user_scholarship_task",on_delete=models.CASCADE)
    sub_task = models.ForeignKey("scholarship.ScholarshipSubTask",related_name="sch_scholarship_sub_task",on_delete=models.CASCADE)
    content = models.TextField()
    attachment_one = models.FileField(upload_to="scholarship/",blank=True,null=True)
    attachment_two = models.FileField(upload_to="scholarship/",blank=True,null=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    status  = models.CharField(max_length=100,choices=UserScholarshipTaskStatud.choices,default=UserScholarshipTaskStatud.PENDING)

    def __str__(self) -> str:
        return "{0}".format(self.sub_task)

    class Meta:
        unique_together = ("user","sub_task",)  
