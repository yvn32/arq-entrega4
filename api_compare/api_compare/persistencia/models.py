# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Producto(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=90, blank=True, null=True)
    descripcion = models.CharField(max_length=500, blank=True, null=True)
    precio = models.IntegerField(blank=True, null=True)
    preciodcto = models.IntegerField(blank=True, null=True)
    stock = models.IntegerField(blank=True, null=True)
    idempresa = models.IntegerField(blank=True, null=True)
    rutaimg = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'producto'

    def to_json(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'descripcion': self.descripcion,
            'precio': self.precio,
            'preciodcto': self.preciodcto,
            'stock': self.stock,
            'idempresa': self.idempresa,
            'rutaimg': self.rutaimg
        }

