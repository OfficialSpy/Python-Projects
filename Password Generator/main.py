# This will generate a strong and random password using Python
# Made by OfficialSpy#7261 on Discord

import secrets
import string as s

length = secrets.choice(range(18, 21))
symbols = s.ascii_letters + s.digits + s.punctuation
password = "".join(secrets.choice(symbols)
for i in range(length))

print(password)