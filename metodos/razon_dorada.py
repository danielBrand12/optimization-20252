import pandas as pd
import matplotlib.pyplot as plt
import math


def f(x):
  return 2 * math.sin(x) - (x**2)/10


def razon_dorada(f, xl, xu, error, method = 'minimize'):
  results = pd.DataFrame(columns=['xl', 'xu', 'x1', 'x2', 'd', 'error'])
  phi = (math.sqrt(5) - 1) / 2  # razón dorada conjugada
  iteraciones = 0 

  d = phi*(xu - xl)
  x1 = xl + d
  x2 = xu - d
  results.loc[len(results)] = [xl, xu, x1, x2, d, abs(x2 - x1)]

  while abs(x2 - x1) > error:
    if method == 'minimize':
      if f(x2) < f(x1):
        xu = x1
      else:
        xl = x2
    
    elif method == 'maximize':
      if f(x2) > f(x1):
        xu = x1
      else:
        xl = x2

    else:
      raise ValueError("Método no reconocido")

    d = phi*(xu - xl)
    x1 = xl + d
    x2 = xu - d

    results.loc[len(results)] = [xl, xu, x1, x2, d, abs(x2 - x1)]

    iteraciones += 1

  return x2, iteraciones, results


xl = 0

xu = 4

error = 0.0001

raiz, iteraciones, df = razon_dorada(f, xl, xu, error, method='maximize')

print("La raiz es: ", raiz)
print("Se realizaron ", iteraciones, " iteraciones")
print("La tabla de valores es: ")
print(df)

# plt.plot(df['error'])
# plt.xlabel('Iteración')
# plt.ylabel('Error')
# plt.title('Comportamiento del error en el método de bisección')
# plt.show()