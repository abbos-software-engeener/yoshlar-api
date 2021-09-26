from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files import File


class HomePage(models.Model):
    slug = models.SlugField()

    def url(self):
        return f'http://127.0.0.1:8000/{self.slug}/'


class AboutTeacher(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="Ism")
    last_name = models.CharField(max_length=50, verbose_name="Familiya")
    middle_name = models.CharField(max_length=50, verbose_name="Otasini ismi")
    subject = models.CharField(max_length=50, verbose_name="Fan")
    title = models.CharField(max_length=100, verbose_name="Sarlavha")
    context = models.TextField(verbose_name='Kontekst')
    photo = models.ImageField(verbose_name="Surat", upload_to='media/')

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.middle_name}'

    def get_photo(self):
        if self.photo:
            return "http://127.0.0.1:8000" + self.photo.url
        else:
            self.photo = self.make_photo(self.photo)
            self.save()
            return "http://127.0.0.1:8000" + self.photo.url

    def make_photo(self, image, size=(200, 200)):
        photo = Image.open(image)
        photo.convert("RGB")
        photo.photo(size)

        photo_io = BytesIO()
        photo.save(photo_io, 'JPEG', qualily=85)

        photo = File(photo_io, name=photo.name)
        return photo


class CourseRegister(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Ism')
    last_name = models.CharField(max_length=50, verbose_name='Familiya')
    middle_name = models.CharField(max_length=50, verbose_name='Otasini ismi')
    phone = models.DecimalField(max_digits=9, decimal_places=0, verbose_name="Telefon raqam")
    email = models.EmailField(verbose_name="Elektron po'chka")


class Course(models.Model):
    teacher = models.ForeignKey(AboutTeacher, on_delete=models.CASCADE, verbose_name="O'qtuvchi")
    name = models.CharField(max_length=50, verbose_name="Kurs nomi")
    image = models.ImageField(verbose_name="Rasm",blank=True, upload_to='media/')
    title = models.CharField(max_length=100, verbose_name="Savlaha")
    context = models.TextField(verbose_name="Text")

    def __str__(self):
        return f"{self.teacher} {self.name}"


    def get_image(self):
        if self.image:
            return "http://127.0.0.1:8000" + self.image.url
        else:
            self.photo = self.make_photo(self.image)
            self.save()
            return "http://127.0.0.1:8000" + self.photo.url

    def make_photo(self, image, size=(200, 200)):
        img = Image.open(image)
        img.convert("RGB")
        img.photo(size)

        photo_io = BytesIO()
        img.save(photo_io, 'JPEG', qualily=85)

        photo = File(photo_io, name=img.name)
        return photo


class Training(models.Model):
    photo = models.ImageField(verbose_name="Surat", upload_to='media/')
    person_name = models.CharField(max_length=50, verbose_name="Trener")
    title = models.CharField(max_length=100, verbose_name='Savloha')
    date_time = models.DateTimeField(verbose_name="Sana")

    def get_image(self):
        if self.photo:
            return "http://127.0.0.1:8000" + self.photo.url
        else:
            self.photo = self.make_photo(self.photo)
            self.save()
            return "http://127.0.0.1:8000" + self.photo.url

    def make_photo(self, image, size=(200, 200)):
        img = Image.open(image)
        img.convert("RGB")
        img.photo(size)

        photo_io = BytesIO()
        img.save(photo_io, 'JPEG', qualily=85)

        photo = File(photo_io, name=img.name)
        return photo


class TrainingRegister(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="Ism")
    last_name = models.CharField(max_length=50, verbose_name="Familiya")
    middle_name = models.CharField(max_length=50, verbose_name="Otasini ismi")
    phone = models.DecimalField(max_digits=9, decimal_places=0, verbose_name="Telefon raqam")
    email = models.EmailField(verbose_name="Elektron po'chta")























