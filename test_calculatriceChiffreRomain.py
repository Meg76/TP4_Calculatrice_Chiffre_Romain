import calculatriceChiffreRomain.calculatriceChiffreRomain as calculatrice

def test_chiffreRomainClassic():
  assert calculatrice.chiffreRomainClassic('I')==1
  assert calculatrice.chiffreRomainClassic('V')==5
  assert calculatrice.chiffreRomainClassic('X')==10
  assert calculatrice.chiffreRomainClassic('L')==50
  assert calculatrice.chiffreRomainClassic('C')==100
  assert calculatrice.chiffreRomainClassic('D')==500
  assert calculatrice.chiffreRomainClassic('M')==1000
  assert calculatrice.chiffreRomainClassic('10')=="ERROR_SYNTAX"

def test_calculatriceChiffreRomain():
  assert calculatrice.calculatriceChiffreRomain('M','+',"M")==2000
  assert calculatrice.calculatriceChiffreRomain('M','-',"D")==500
  assert calculatrice.calculatriceChiffreRomain('V','*',"X")==50
  assert calculatrice.calculatriceChiffreRomain('M','/',"M")==1
  assert calculatrice.calculatriceChiffreRomain('I','^',"L")=="ERROR_OPERATOR"

