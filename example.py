# -*- coding: utf-8 -*-

from figures import Figures, figures as f


figures = Figures()

print(figures.get('tick'))

figures.add('santa', '🎅🏻')
print(figures.get('santa'))

print(figures.get('nonexistent', default=''))

print(figures.string('✔ ✔ ✔')) # ✔ ✔ ✔ or √ √ √

 # or you can use just like this
print(f('tick'))
print(f(string='✔ ✔ ✔')) # ✔ ✔ ✔ or √ √ √
