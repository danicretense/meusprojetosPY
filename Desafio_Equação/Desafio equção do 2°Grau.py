import numpy as np
def delta(a,b,c):
    calculo1= b**2
    calculo2=a*c
    calculo3=calculo2*-4
    calculo4=calculo3+calculo1
    return calculo4
def baskara(delta,b,a):
   raiz_delta=np.sqrt(delta)
   calc1=raiz_delta+(-b)
   calc2=2*a
   calc3=calc1/calc2
   #----------------
   c1= -b-raiz_delta
   c2=c1/calc2
   return calc3,c2

def main():
  a=0
  b=0
  c=0
  a=int(input("Digite o valor de A "))
  b=int(input("Digite o valor de B "))
  c=int(input("Digite o valor de C "))
  resul_delta=delta(a,b,c)
  x1_x2=baskara(resul_delta,b,a)
  print(x1_x2)

main()  