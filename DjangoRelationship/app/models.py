from django.db import models

# Create your models here.
class Publication(models.Model):
    title=models.CharField(max_length=30)

    def __str__(self):
        return f"{self.id} - {self.title}"
    
    class Meta:
        ordering=('title',)


class Article(models.Model):
    headline=models.CharField(max_length=300)
    publications=models.ManyToManyField(Publication)


    def __str__(self):
        return f"{self.id} - {self.headline}"
    
    class Meta:
        ordering=('headline',)


class Reporter(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField()

    def __str__(self):
        return f'{self.id}-{self.first_name}'
    
class ReporterArticle(models.Model):
    headline=models.CharField(max_length=100)
    pub_date=models.DateField()
    reporter=models.ForeignKey(Reporter,on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.headline
    
    class Meta:
        ordering=('headline',)


class Place(models.Model):
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=150)


    def __str__(self) -> str:    
        return self.name

class Restaurant(models.Model):
    place=models.OneToOneField(Place,on_delete=models.CASCADE,primary_key=True)
    serves_hot_dogs=models.BooleanField(default=False)
    serves_pizza=models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.place.name
