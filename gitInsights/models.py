from django.db import models

class Repository(models.Model):
    titre = models.CharField(max_length=100)
    starsgazers = models.IntegerField()
    commits_this_week = models.IntegerField()
    commits_last_week = models.IntegerField()
    top_language = models.TextField(default=None)

    class Meta:
        verbose_name = "repo"
        ordering = ['starsgazers']

    def __str__(self):

        return self.titre
