def conversionChiffreRomain(chiffreRomain):
  if chiffreRomain == "I" or chiffreRomain == "i":
    return 1
  elif chiffreRomain == "V" or chiffreRomain == "v":
    return 5
  elif chiffreRomain == "X" or chiffreRomain == "x":
    return 10
  elif chiffreRomain == "L" or chiffreRomain == "l":
    return 50
  elif chiffreRomain == "C" or chiffreRomain == "c":
    return 100
  elif chiffreRomain == "D" or chiffreRomain == "d":
    return 500
  elif chiffreRomain == "M" or chiffreRomain == "m":
    return 1000
  else:
    return "ERROR"


def chiffreRomainClassic(chiffreRomain):
  if type(chiffreRomain) is str:
    chiffreRomain=conversionChiffreRomain(chiffreRomain)
    somme=0
    for i in range(len(chiffreRomain)):
      valeurRomain=conversionChiffreRomain[chiffreRomain[i]]
      if (i+1<len(chiffreRomain)) and (conversionChiffreRomain[chiffreRomain[i+1]]>valeurRomain):
        somme=somme-valeurRomain
      else:
        somme=somme+valeurRomain
  else:
    return "ERROR_SYNTAX"
  return somme


def calculatriceChiffreRomain(chiffreRomain1,operateur,chiffreRomain2):
  if operateur=='-':
    return chiffreRomainClassic(chiffreRomain1)-chiffreRomainClassic(chiffreRomain2)
  elif operateur=='+':
    return chiffreRomainClassic(chiffreRomain1)+chiffreRomainClassic(chiffreRomain2)
  elif operateur=="*":
    return chiffreRomainClassic(chiffreRomain1) * chiffreRomainClassic(chiffreRomain2)
  elif operateur=='/':
    if chiffreRomain2==0:
      return "ERROR_DIVISION_BY_ZERO"
    else:
      return int(chiffreRomainClassic(chiffreRomain1)/chiffreRomainClassic(chiffreRomain2))
  else:
    return "ERROR_OPERATOR"


