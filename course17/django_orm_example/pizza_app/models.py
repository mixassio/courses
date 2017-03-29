from __future__ import unicode_literals

from django.db import models
from django.db.models import Manager
from django.utils import timezone
from django.utils.six import python_2_unicode_compatible


@python_2_unicode_compatible
class Address(models.Model):
    full = models.CharField(max_length=150)

    class Meta:
        verbose_name = 'Address'
        verbose_name_plural = 'Addresses'

    def __str__(self):
        return str(self.full)


@python_2_unicode_compatible
class PizzaIngredient(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.name)


@python_2_unicode_compatible
class PizzaMenuItem(models.Model):
    name = models.CharField(max_length=50)
    ingredients = models.ManyToManyField(
        'PizzaIngredient',
        related_name='ingredients'
    )

    def __str__(self):
        return str(self.name)


@python_2_unicode_compatible
class PizzaSize(models.Model):
    LARGE = ('XL', 'Large')
    MEDIUM = ('MD', 'Medium')
    SMALL = ('SM', 'Small')
    __all = (LARGE, MEDIUM, SMALL)

    size = models.CharField(max_length=2, choices=__all)

    def __str__(self):
        return str(self.size)


class PizzaOrderManager(Manager):
    def get_queryset(self, **kwargs):
        return super(PizzaOrderManager, self).get_queryset().filter(
            delivered=True,
        )


@python_2_unicode_compatible
class PizzaOrder(models.Model):
    # Linking:
    kind = models.ForeignKey('PizzaMenuItem', related_name='pizzas')
    size = models.ForeignKey('PizzaSize', related_name='pizzas')
    delivery = models.ForeignKey('Address', related_name='pizzas')

    # Buisness logic:
    extra = models.ManyToManyField(
        'PizzaIngredient', blank=True, related_name='pizzas_extras')
    exclude = models.ManyToManyField('PizzaIngredient', blank=True)
    comment = models.CharField(max_length=140, blank=True)

    # Utils:
    delivered = models.BooleanField(default=False)
    date_created = models.DateTimeField(default=timezone.now)
    date_delivered = models.DateTimeField(default=None, null=True)

    objects = Manager()
    delivered_manager = PizzaOrderManager()

    def mark_delivered(self, commit=True):
        self.delivered = True
        self.date_delivered = timezone.now()
        if commit:
            self.save()

    def save(self, **kwargs):
        if not self.pk:
            print('Creating new PizzaOrder!')
        else:
            print('Updating the existing one')

        super(PizzaOrder, self).save(**kwargs)

    def __str__(self):
        return 'PizzaOrder [%s]' % self.id
