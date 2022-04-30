import phonenumbers
from phonenumbers import timezone, geocoder, carrier


phoneNumber = phonenumbers.parse("") # <------ Fill that in with the phone number, for example; +27352859206

#  '+27' being the Country Code, replace it with your countries national code.

timeZone = timezone.time_zones_for_number(phoneNumber)


Carrier = carrier.name_for_number(phoneNumber, 'en')

Region = geocoder.description_for_number(phoneNumber, 'en')

print(phoneNumber)
print(timeZone)
print(Carrier)
print(Region)