from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class WorksManager(models.Manager):
    """
    Class to override 'all' in 'filter' method.
    """

    def get_queryset(self):
        """
        :return: Calling queryset method.
        """
        return super().get_queryset()

    def all(self):
        """
        :return: Returns the "filter" method, which will only return a queryset with "True"
                values in the "ordering_option" field.
        """
        return self.get_queryset().filter(ordering_option=True)


class Works(models.Model):
    """
    The main model for the artist works.
    """
    name = models.CharField(max_length=100)
    work_description = models.TextField(max_length=400)
    photo = models.ImageField(upload_to='master_works/')
    date = models.DateField()
    price = models.IntegerField()
    ordering_option = models.BooleanField(default=True)
    publishing_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    objects = WorksManager()

    def __str__(self):
        """
        :return: Output the work name.
        """
        return self.name


class Comments(models.Model):
    """
    Model for users comments and works descriptions.
    """
    work = models.ForeignKey(Works, on_delete=models.CASCADE)
    description = models.TextField(max_length=400)
    comment_author = models.ForeignKey(User, on_delete=models.CASCADE)
    publishing_time = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        """
        :return: Output the work description.
        """
        return self.description
