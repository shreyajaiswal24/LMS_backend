from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser, UserManager
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.db.models import Q
from PIL import Image

from course.models import Program
from .validators import ASCIIUsernameValidator


# LEVEL_COURSE = "Level course"
CPT = _("CPT: 22Days")
CPTE = _("CPTE: 44Days")

LEVEL = (
    # (LEVEL_COURSE, "Level course"),
    (CPT, _("CPT(22Days)")),
    (CPTE, _("CPTE(44Days)")),
)

FATHER = _("Father")
MOTHER = _("Mother")
# BROTHER = _("Brother")
# SISTER = _("Sister")
# GRAND_MOTHER = _("Grand mother")
# GRAND_FATHER = _("Grand father")
# OTHER = _("Other")

RELATION_SHIP = (
    (FATHER, _("Father")),
    (MOTHER, _("Mother")),
    # (BROTHER, _("Brother")),
    # (SISTER, _("Sister")),
    # (GRAND_MOTHER, _("Grand mother")),
    # (GRAND_FATHER, _("Grand father")),
    # (OTHER, _("Other")),
)


class CustomUserManager(UserManager):
    def search(self, query=None):
        queryset = self.get_queryset()
        if query is not None:
            or_lookup = (
                Q(username__icontains=query)
                | Q(first_name__icontains=query)
                | Q(last_name__icontains=query)
                | Q(email__icontains=query)
            )
            queryset = queryset.filter(
                or_lookup
            ).distinct()  # distinct() is often necessary with Q lookups
        return queryset

    def get_trainee_count(self):
        return self.model.objects.filter(is_trainee=True).count()

    def get_instructor_examiner_count(self):
        return self.model.objects.filter(is_instructor_examiner=True).count()

    def get_superuser_count(self):
        return self.model.objects.filter(is_superuser=True).count()

    # def get_student_count(self):
    #     """Alias for get_trainee_count to maintain backward compatibility"""
    #     return self.model.objects.filter(is_trainee=True).count()

    # def get_lecturer_count(self):
    #     """Alias for get_instructor_examiner_count to maintain backward compatibility"""
    #     return self.model.objects.filter(is_instructor_examiner=True).count()
    
    def make_random_password(self, length=10, allowed_chars='abcdefghjkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789'):
        """Generate a random password with the given length and given allowed_chars."""
        from django.utils.crypto import get_random_string
        return get_random_string(length, allowed_chars)


GENDERS = ((_("M"), _("Male")), (_("F"), _("Female")))


class User(AbstractUser):
    is_trainee = models.BooleanField(default=False)
    is_instructor_examiner = models.BooleanField(default=False)
    # is_parent = models.BooleanField(default=False)
    is_operations = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    gender = models.CharField(max_length=1, choices=GENDERS, blank=False, null=False, default="M")
    phone = models.CharField(max_length=60, blank=False, null=False, default="")
    address = models.CharField(max_length=60, blank=True, null=True)
    picture = models.ImageField(
        upload_to="profile_pictures/%y/%m/%d/", default="default.png", null=True
    )
    email = models.EmailField(blank=True, null=True)

    username_validator = ASCIIUsernameValidator()

    objects = CustomUserManager()

    class Meta:
        ordering = ("-date_joined",)

    @property
    def get_full_name(self):
        full_name = self.username
        if self.first_name and self.last_name:
            full_name = self.first_name + " " + self.last_name
        return full_name

    def __str__(self):
        return "{} ({})".format(self.username, self.get_full_name)

    @property
    def get_user_role(self):
        if self.is_superuser:
            role = _("Superuser")
        elif self.is_trainee:
            role = _("Trainee")
        elif self.is_instructor_examiner:
            role = _("Instructor/Examiner")
        elif self.is_operations:
            role = _("Operations")
        # elif self.is_parent:
        #     role = _("Parent")

        return role

    def get_picture(self):
        try:
            return self.picture.url
        except:
            no_picture = settings.MEDIA_URL + "default.png"
            return no_picture

    def get_absolute_url(self):
        return reverse("profile_single", kwargs={"user_id": self.id})

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        try:
            img = Image.open(self.picture.path)
            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                img.save(self.picture.path)
        except:
            pass

    def delete(self, *args, **kwargs):
        if self.picture.url != settings.MEDIA_URL + "default.png":
            self.picture.delete()
        super().delete(*args, **kwargs)


class StudentManager(models.Manager):
    def search(self, query=None):
        qs = self.get_queryset()
        if query is not None:
            or_lookup = Q(level__icontains=query) | Q(program__icontains=query)
            qs = qs.filter(
                or_lookup
            ).distinct()  # distinct() is often necessary with Q lookups
        return qs


class Student(models.Model):
    student = models.OneToOneField(User, on_delete=models.CASCADE)
    id_number = models.CharField(max_length=20, unique=True, blank=False, null=False, default="")  # Ensure this is required
    level = models.CharField(max_length=25, choices=LEVEL, null=True)
    program = models.ForeignKey(Program, on_delete=models.CASCADE, null=True)

    objects = StudentManager()

    class Meta:
        ordering = ("-student__date_joined",)

    def __str__(self):
        return self.student.get_full_name

    @classmethod
    def get_gender_count(cls):
        males_count = Student.objects.filter(student__gender="M").count()
        females_count = Student.objects.filter(student__gender="F").count()

        return {"M": males_count, "F": females_count}

    def get_absolute_url(self):
        return reverse("profile_single", kwargs={"user_id": self.id})

    def delete(self, *args, **kwargs):
        self.student.delete()
        super().delete(*args, **kwargs)


# class Parent(models.Model):
#     """
#     Connect student with their parent, parents can
#     only view their connected students information
#     """

#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     student = models.OneToOneField(Student, null=True, on_delete=models.SET_NULL)
#     first_name = models.CharField(max_length=120)
#     last_name = models.CharField(max_length=120)
#     phone = models.CharField(max_length=60, blank=True, null=True)
#     email = models.EmailField(blank=True, null=True)

#     # What is the relationship between the student and
#     # the parent (i.e. father, mother, brother, sister)
#     relation_ship = models.TextField(choices=RELATION_SHIP, blank=True)

#     class Meta:
#         ordering = ("-user__date_joined",)

#     def __str__(self):
#         return self.user.username


class DepartmentHead(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.ForeignKey(Program, on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ("-user__date_joined",)

    def __str__(self):
        return "{}".format(self.user)
