import re

text = "The film     " \
       "" \
       "" \
       "" \
       "" \
       "" \
       "" \
       "" \
       "" \
       "       " \
       "Pulp Fiction      " \
       "" \
       "" \
       "" \
       "was released in  " \
       "" \
       " " \
       "year 1994."
print text
result = re.sub(r"\n+", " ", text, flags= re.I)
print(result)