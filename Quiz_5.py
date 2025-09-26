import numpy as np
import matplotlib.pyplot as plt


area_size = 5000              
num_drones = 10              
radio_deteccion = 200        
tiempo_max = 120              
velocidad_dron = 15           
num_iteraciones = 100         
particulas = 30               

grid_size = 50  
prob_map = np.random.rand(grid_size, grid_size)  
x_coords = np.linspace(0, area_size, grid_size)
y_coords = np.linspace(0, area_size, grid_size)

def evaluar_posiciones(posiciones):
    cobertura = np.zeros((grid_size, grid_size))
    for dron in posiciones:
        x, y = dron
        for i, xi in enumerate(x_coords):
            for j, yj in enumerate(y_coords):
                distancia = np.sqrt((xi - x)**2 + (yj - y)**2)
                if distancia <= radio_deteccion:
                    cobertura[i, j] = 1
    return np.sum(cobertura * prob_map)

class PSO:
    def __init__(self, n_particulas, n_drones, iteraciones):
        self.n_particulas = n_particulas
        self.n_drones = n_drones
        self.iteraciones = iteraciones
        self.posiciones = np.random.rand(n_particulas, n_drones, 2) * area_size
        self.velocidades = np.random.randn(n_particulas, n_drones, 2) * 50
        self.best_posiciones = np.copy(self.posiciones)
        self.best_valores = np.array([evaluar_posiciones(p) for p in self.posiciones])
        self.global_best = self.best_posiciones[np.argmax(self.best_valores)]
        self.global_best_valor = np.max(self.best_valores)

    def optimizar(self):
        w = 0.7
        c1 = 1.5
        c2 = 1.5
        for _ in range(self.iteraciones):
            for i in range(self.n_particulas):
                r1, r2 = np.random.rand(), np.random.rand()
                self.velocidades[i] = (
                    w * self.velocidades[i]
                    + c1 * r1 * (self.best_posiciones[i] - self.posiciones[i])
                    + c2 * r2 * (self.global_best - self.posiciones[i])
                )
                self.posiciones[i] += self.velocidades[i]
                self.posiciones[i] = np.clip(self.posiciones[i], 0, area_size)

                valor = evaluar_posiciones(self.posiciones[i])
                if valor > self.best_valores[i]:
                    self.best_valores[i] = valor
                    self.best_posiciones[i] = self.posiciones[i].copy()
                    if valor > self.global_best_valor:
                        self.global_best_valor = valor
                        self.global_best = self.posiciones[i].copy()

        return self.global_best, self.global_best_valor


pso = PSO(particulas, num_drones, num_iteraciones)
mejores_posiciones, mejor_valor = pso.optimizar()

print("Mejor cobertura encontrada:", mejor_valor)

plt.imshow(prob_map.T, extent=[0, area_size, 0, area_size], origin="lower", cmap="YlOrRd")
plt.colorbar(label="Probabilidad de supervivientes")
plt.scatter(mejores_posiciones[:, 0], mejores_posiciones[:, 1], c="blue", marker="o", label="Drones")
plt.legend()
plt.title("Distribución de drones optimizada con PSO")
plt.xlabel("X (m)")
plt.ylabel("Y (m)")
plt.show()
