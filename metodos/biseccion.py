import pandas as pd
import matplotlib.pyplot as plt

def f(x):
  return 3*x**2 - 120*x + 100

def biseccion(f, xl, xu, error):
  results = pd.DataFrame(columns=['xl', 'xu', 'xr', 'error'])
  iteraciones = 0

  if f(xl)*f(xu) > 0:
    print("No hay raiz en ese intervalo")
    return

  while abs(xu - xl) > error:
    xr = (xl + xu)/2
    results.loc[len(results)] = [xl, xu, xr, abs(xu - xl)]
    if f(xr) == 0:
      results.loc[len(results)] = [xl, xu, xr, abs(xu - xl)]

      return xr, iteraciones, results
    elif f(xl)*f(xr) < 0:
      xu = xr
    else:
      xl = xr
    iteraciones += 1


  return xr, iteraciones, results


xl = -10

xu = 20

error = 0

raiz, iteraciones, df = biseccion(f, xl, xu, error)

print("La raiz es: ", raiz)
print("Se realizaron ", iteraciones, " iteraciones")
print("La tabla de valores es: ")
print(df)

plt.plot(df['error'])
plt.xlabel('Iteración')
plt.ylabel('Error')
plt.title('Comportamiento del error en el método de bisección')
plt.show()