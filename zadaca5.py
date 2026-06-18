import re

email_regex = r"^[a-zA-Z]+\.[a-zA-Z]+@fpmoz\.sum\.ba$"
eduid_regex = r"^[a-zA-Z]+\.[a-zA-Z]+\d*@sum\.ba$"

email_unos = input()
eduid_unos = input()

if re.match(email_regex, email_unos):
    print("Email: OK")
else:
    print("Email: X")

if re.match(eduid_regex, eduid_unos):
    print("eduId: OK")
else:
    print("eduId: X")