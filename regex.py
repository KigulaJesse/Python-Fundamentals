import re

txt = "Boom The rain in Spain The tomboys".strip()

x = re.sub("[t..s]","New",txt)

print(x)