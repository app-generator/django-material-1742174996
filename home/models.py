# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    segundo_apellido = models.CharField(max_length=255, null=True, blank=True)
    idioma = models.CharField(max_length=255, null=True, blank=True)
    empresa = models.CharField(max_length=255, null=True, blank=True)
    telefono = models.CharField(max_length=255, null=True, blank=True)
    telefono_otro = models.CharField(max_length=255, null=True, blank=True)
    notas = models.TextField(max_length=255, null=True, blank=True)
    historial_auditoria = models.CharField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Departamentos(models.Model):

    #__Departamentos_FIELDS__
    departamento = models.CharField(max_length=255, null=True, blank=True)
    descripcion = models.CharField(max_length=255, null=True, blank=True)
    historial_auditoria = models.CharField(max_length=255, null=True, blank=True)

    #__Departamentos_FIELDS__END

    class Meta:
        verbose_name        = _("Departamentos")
        verbose_name_plural = _("Departamentos")


class Cargos(models.Model):

    #__Cargos_FIELDS__
    historial_auditoria = models.CharField(max_length=255, null=True, blank=True)

    #__Cargos_FIELDS__END

    class Meta:
        verbose_name        = _("Cargos")
        verbose_name_plural = _("Cargos")



#__MODELS__END
