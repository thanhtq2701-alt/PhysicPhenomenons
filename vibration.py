import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def system_dynamics(state, t, m, c, k):
    x, v = state  # Position and Velocity
    # dxdt = v
    # dvdt = (Force - c*v - k*x) / m
    dxdt = v
    dvdt = (-c*v - k*x) / m
    return [dxdt, dvdt]

# --- Parameters ---
m = 2.0      # Mass (kg)
k = 50.0     # Spring constant (N/m)
c = 1.5      # Damping coefficient (Try 0 for undamped!)
x0 = 1.0     # Initial displacement (m)
v0 = 0.0     # Initial velocity (m/s)

# Time vector
t = np.linspace(0, 10, 1000)

# --- Solve ---
solution = odeint(system_dynamics, [x0, v0], t, args=(m, c, k))
displacement = solution[:, 0]

# --- Plotting ---
plt.figure(figsize=(10, 5))
plt.plot(t, displacement, label='Displacement (x)', color='blue')
plt.axhline(0, color='black', lw=1)
plt.title(f'Damped Harmonic Motion (m={m}, c={c}, k={k})')
plt.xlabel('Time (s)')
plt.ylabel('Position (m)')
plt.grid(True)
plt.legend()
plt.show()