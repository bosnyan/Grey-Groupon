import regex as re

text = open("rhode.txt", 'r')
rappers = text.read()
rappers = rappers.split('\n')
for rapper in range(0, len(rappers)):
    rappers[rapper] = re.sub("feat.*", '', rappers[rapper], flags=re.IGNORECASE).upper()
    rappers[rapper] = re.sub(" \(.*", '', rappers[rapper], flags=re.IGNORECASE)
    rappers[rapper] = re.sub("['-.,!?/\<>*|:\"]", '', rappers[rapper])
    rappers[rapper] = re.sub(" and.*", '', rappers[rapper], flags=re.IGNORECASE)
    rappers[rapper] = re.sub(" &.*", '', rappers[rapper])
    rappers[rapper] = re.sub(" with.*", '', rappers[rapper], flags=re.IGNORECASE).replace(" ", "")

rappers = set(rappers)
rappers = list(rappers)
print(rappers)
