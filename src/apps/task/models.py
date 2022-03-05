from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.


class TaskChoice(models.TextChoices):

    DAILY = "daily","Daily"
    MONTHLY = "monthly","Monthly"
    ONE_TIME = "ot","One Time"

class Curriculum(models.Model):
    user = models.ForeignKey("account.User",related_name="user_task_admin",on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    cover_image = models.ImageField(upload_to="task/",blank=True,null=True)
    content = RichTextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    expire_one = models.DateField(blank=True,null=True)
    task_type = models.CharField(max_length=100,default=TaskChoice.DAILY,choices=TaskChoice.choices)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.title

 

class UserTask(models.Model):
    user = models.ForeignKey("account.User",related_name="user_task",on_delete=models.CASCADE)
    curriculum = models.ForeignKey("task.Curriculum",related_name="task_task",on_delete=models.CASCADE)
    attachment = models.FileField(upload_to="task/",blank=True,null=True)
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "{0}".format(self.user)
