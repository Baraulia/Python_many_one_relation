from django.db import models


# Create your models here.
class PublishedModel(models.Model):
    name = models.CharField(max_length=100)


class AuthorModel(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return (self.name + ' ' + self.surname)


class GanreModel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ImageModel(models.Model):
    image = models.ImageField(upload_to='book/%Y/%m/%d')


class BookModel(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200)
    author = models.ManyToManyField(AuthorModel, related_name='author')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    published_by = models.ForeignKey(PublishedModel, on_delete=models.PROTECT)
    ganre = models.ManyToManyField(GanreModel)


class DescriptionModel(models.Model):
    book = models.OneToOneField(BookModel, on_delete=models.CASCADE, related_name='desc')
    description = models.TextField(verbose_name='Описание')
    image = models.ManyToManyField(ImageModel)

    def __str__(self):
        return self.book.name
