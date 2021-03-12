#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"></ul></div>

# In[ ]:


#http://projectpython.net/chapter11/index.html
class Ball:
    def __init__(self, start_x, start_y, start_v_x, start_v_y, radius=.4, r = 0.5, g = 0.5, b = 0.5):
        # Location and velocities of the ball.
        self.x = start_x
        self.y = start_y
        self.v_x = start_v_x
        self.v_y = start_v_y

        self.radius = radius   # radius (in pixels)

        # Color of the ball, for drawing purposes.
        self.r = r
        self.g = g
        self.b = b

    def update_position(self, timestep):
        self.x = self.x + timestep * self.v_x
        self.y = self.y + timestep * self.v_y

    def update_velocity(self, timestep):
        self.v_y = self.v_y + timestep * EARTH_GRAVITY_ACCELERATION

    def animate_step(self, timestep):
        self.update_position(timestep)
        self.update_velocity(timestep)

    # draw a ball, with scaling determined by ppu, pixels per unit
    def draw(self, ppu, window_height):
        disable_stroke()
        set_fill_color(self.r, self.g, self.b)
        draw_circle(self.x * ppu, window_height - self.y * ppu, self.radius * ppu)

    def __str__(self):
        return str(self.x) + ", " + str(self.y)

