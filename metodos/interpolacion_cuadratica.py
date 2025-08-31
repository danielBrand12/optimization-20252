import pandas as pd
import matplotlib.pyplot as plt
import math

# Función objetivo
def f(x):
    return 2 * math.sin(x) - (x**2)/10  # Puedes cambiar esta función

def interpolacion_cuadratica(f, x0, x1, x2, error, method = 'minimize'):
    results = pd.DataFrame(columns=['x0', 'x1', 'x2', 'x3', 'f(x3)', 
                                     'error_x0', 'error_x1', 'error_x2', 'error_min'])
    iteraciones = 0
    x3 = None

    while True:
        f0, f1, f2 = f(x0), f(x1), f(x2)

        # Fórmula de interpolación cuadrática
        num = (f0 * (x1**2 - x2**2) + f1 * (x2**2 - x0**2) + f2 * (x0**2 - x1**2))
        den = (2 * (f0*(x1 - x2) + f1*(x2 - x0) + f2*(x0 - x1)))

        if den == 0:
            print("Error: denominador cero")
            break

        x3 = num / den
        f3 = f(x3)

        # Errores individuales y el mínimo
        error_x0 = abs(x3 - x0)
        error_x1 = abs(x3 - x1)
        error_x2 = abs(x3 - x2)
        error_min = min(error_x0, error_x1, error_x2)

        # Guardar datos en el DataFrame
        results.loc[len(results)] = [x0, x1, x2, x3, f3, error_x0, error_x1, error_x2, error_min]

        # Verificar condición de parada
        if error_min < error:
            break

        # Actualizar los puntos
        #if method == 'maximize':  # Mantener el valor más alto
        if f3 > f1:
            x0 = x1
            x1 = x3
        else:
            x2 = x1
            x1 = x3
        # elif method == 'minimize':  # Mantener el valor más bajo
        #     if f3 < f1:
        #         x0 = x1
        #         x1 = x3
        #     else:
        #         x2 = x1
        #         x1 = x3
        # else:
            #raise ValueError("Método no reconocido")

        iteraciones += 1

    return x3, f3, iteraciones, results


# --- Ejemplo ---
x0 = 2
x1 = 4
x2 = 6
error = 0.0001

max_x, max_fx, iteraciones, df = interpolacion_cuadratica(f, x0, x1, x2, error, method='maximize')

print("El máximo está en x =", max_x)
print("f(x) máximo =", max_fx)
print("Iteraciones realizadas:", iteraciones)
print("\nTabla de iteraciones:")
print(df)

# # Graficar el error mínimo
# plt.plot(df['error_min'], marker='o', label='Error mínimo')
# plt.xlabel('Iteración')
# plt.ylabel('Error')
# plt.title('Comportamiento del error en interpolación cuadrática')
# plt.grid(True)
# plt.legend()
# plt.show()
