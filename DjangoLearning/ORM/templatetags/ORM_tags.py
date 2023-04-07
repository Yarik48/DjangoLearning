from django import template
from ORM.models import *

from ORM.models import Catigoris

register = template.Library()
@register.simple_tag()
def get_cats():
    return Catigoris.objects.all()