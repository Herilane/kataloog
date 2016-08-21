# -*- coding: utf-8 -*-
from datetime import datetime
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

# Validaatorid

onlyNumbers = RegexValidator(r'^[0-9]*$', 'Lubatud ainult numbrid!')
onlyAlphanumerical = RegexValidator(r'^[a-zA-Z0-9_äöüõÄÖÕÜ\- ]*$', 'Lubatud ainult tähed ja numbrid!')
onlyAlphabet = RegexValidator(r'^[a-zA-ZäöüõÄÖÕÜ\-]*$', 'Lubatud ainult tähed!')

def validateDate(date):
	currentTime = datetime.now().date()
	if date > currentTime:
		raise ValidationError(u'Asutamise kuupäev ei saa olla tulevikus!')


