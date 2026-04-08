from django.db import models

class Certificate(models.Model):
    title = models.CharField(max_length=200)
    issuer = models.CharField(max_length=200)
    image = models.ImageField(upload_to='certificates/')
    date = models.DateField()

    def __str__(self):
        return self.title

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    github_link = models.URLField(blank=True, null=True)
    live_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title


class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='projects/')

    def __str__(self):
        return self.project.title

