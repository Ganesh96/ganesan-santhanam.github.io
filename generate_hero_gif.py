import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# (The DoublePendulum class definition remains the same as before)
class DoublePendulum:
    def __init__(self, m1=2.0, m2=1.0, L1=1.4, L2=1.0, g=9.81, 
                 initial_state=[-np.pi/2, 0, np.pi, 0]):
        self.m1, self.m2 = m1, m2
        self.L1, self.L2 = L1, L2
        self.g = g
        self.state = np.array(initial_state, dtype=float)
        self.history = []
        self.time_points = []

    def _get_accelerations(self, state):
        t1, w1, t2, w2 = state
        a1 = (self.L1 * w1**2 * np.sin(t1 - t2) * np.cos(t1 - t2) +
              self.g * np.sin(t2) * np.cos(t1 - t2) -
              self.m2 * self.L2 * w2**2 * np.sin(t1 - t2) -
              (self.m1 + self.m2) * self.g * np.sin(t1) / self.m2) / \
             (self.L1 * ((self.m1 + self.m2) / self.m2 - np.cos(t1 - t2)**2))
        a2 = (-self.m2 * self.L2 * w2**2 * np.sin(t1-t2) * np.cos(t1-t2) +
              (self.m1 + self.m2) * self.g * np.sin(t1) * np.cos(t1-t2) -
              (self.m1 + self.m2) * self.L1 * w1**2 * np.sin(t1-t2) -
              (self.m1 + self.m2) * self.g * np.sin(t2)) / \
             (self.L2 * (self.m1 + self.m2 - self.m2 * np.cos(t1-t2)**2))
        return np.array([a1, a2])

    def step(self, dt):
        t1, w1, t2, w2 = self.state
        a1_curr, a2_curr = self._get_accelerations(self.state)
        t1_new = t1 + w1 * dt + 0.5 * a1_curr * dt**2
        t2_new = t2 + w2 * dt + 0.5 * a2_curr * dt**2
        next_state_for_accel = np.array([t1_new, w1, t2_new, w2])
        a1_next, a2_next = self._get_accelerations(next_state_for_accel)
        w1_new = w1 + 0.5 * (a1_curr + a1_next) * dt
        w2_new = w2 + 0.5 * (a2_curr + a2_next) * dt
        self.state = np.array([t1_new, w1_new, t2_new, w2_new])

    def run_simulation(self, t_final, dt):
        num_steps = int(t_final / dt)
        self.time_points = np.linspace(0, t_final, num_steps + 1)
        self.history = np.zeros((num_steps + 1, 4))
        self.history[0] = self.state
        for i in range(num_steps):
            self.step(dt)
            self.history[i+1] = self.state

    def get_cartesian_coords(self):
        t1, t2 = self.history[:, 0], self.history[:, 2]
        x1 = self.L1 * np.sin(t1)
        y1 = -self.L1 * np.cos(t1)
        x2 = x1 + self.L2 * np.sin(t2)
        y2 = y1 - self.L2 * np.cos(t2)
        return x1, y1, x2, y2


def generate_hero_animation():
    print("Generating hero banner animation...")
    t_final = 25.0
    dt = 0.02

    pendulum = DoublePendulum(initial_state=[-np.pi/2.2, 0, np.pi/1.8, 0])
    pendulum.run_simulation(t_final, dt)
    x1, y1, x2, y2 = pendulum.get_cartesian_coords()

    # Create a wide aspect ratio figure
    fig = plt.figure(figsize=(16, 9), facecolor='none')
    ax = fig.add_subplot(111, aspect='equal', autoscale_on=False,
                         xlim=(-3, 3), ylim=(-3, 3))
    ax.axis('off')

    line, = ax.plot([], [], 'o-', lw=3, color='#E3E3E3', markersize=12, markerfacecolor='#A5A5A5', markeredgecolor='#E3E3E3')
    trace, = ax.plot([], [], '-', lw=1.5, color='#f66338', alpha=0.8)

    def init():
        line.set_data([], [])
        trace.set_data([], [])
        return line, trace

    def animate(i):
        line.set_data([0, x1[i], x2[i]], [0, y1[i], y2[i]])
        start_index = max(0, i - 120)
        trace.set_data(x2[start_index:i], y2[start_index:i])
        return line, trace

    ani = FuncAnimation(fig, animate, frames=len(pendulum.time_points),
                        interval=dt*1000, blit=True, init_func=init)

    ani.save('hero_animation.gif', writer='imagemagick', fps=int(1/dt), savefig_kwargs={'facecolor': 'none'})
    print("Saved hero banner to 'hero_animation.gif'")

if __name__ == '__main__':
    generate_hero_animation()
