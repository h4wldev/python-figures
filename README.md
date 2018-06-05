# python-figures
> 😀Can use unicode symbols on any OS!

This project is based on [sindresorhus/figures](https://github.com/sindresorhus/figures).

<a href="https://github.com/h4wldev/python-figures/blob/master/LICENSE"><img src="https://img.shields.io/github/license/mashape/apistatus.svg?style=flat-square"></a>

## Usage
You can see supported symbols on this code or windows. You can also see this example on example.py
```python
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
```

## API
### Figure
#### add(key, default, windows)
You can add custom symbol with this function.

##### key
Type : `String`

Unicode symbol's key

##### default
Type : `String`

Unicode symbol (like 🎅)

##### windows
Type : `String`

if you enter this argument, it return unicode symbol on windows CMD

#### get(key, default)
Return os friendly unicode symbol with key

#### key
Type : `String`

Unicode symbols, see [Figures](#figures). also you can use custom symbol with add function.

#### default
Type : `String`

Return this when nonexistent key argument.

#### string(string)
replace string for windows CMD.

#### string
Type : `String`

String what have unicode symbols.

#### get_all()
Get all of symbols, include custom symbols

#### get_keys()
Get all of symbol's keys, include custom symbols


### figures(key=None, string=None, default=None)
Return os friendly unicode symbol with key, or replace string for windows CMD.

#### key
Type : `String`

Unicode symbols, see [Figures](#figures).

#### string
Type : `String`

String what have unicode symbols.

#### default
Type : `String`

Return this when nonexistent key argument.

## Figures
| Key                |  Default  | Windows |
| ------------------ | :-------: | :-----: |
| tick               |     ✔     |    √    |
| cross              |     ✖     |    ×    |
| star               |     ★     |    *    |
| square             |     ▇     |    █    |
| squareSmall        |     ◻     |   [ ]   |
| squareSmallFilled  |     ◼     |   [█]   |
| play               |     ▶     |    ►    |
| circle             |     ◯     |   ( )   |
| circleFilled       |     ◉     |   (*)   |
| circleDotted       |     ◌     |   ( )   |
| circleDouble       |     ◎     |   ( )   |
| circleCircle       |     ⓞ     |   (○)   |
| circleCross        |     ⓧ     |   (×)   |
| circlePipe         |     Ⓘ     |   (│)   |
| circleQuestionMark |     ?⃝    |   (?)   |
| bullet             |     ●     |    *    |
| dot                |     ․     |    .    |
| line               |     ─     |    ─    |
| ellipsis           |     …     |   ...   |
| pointer            |     ❯     |    >    |
| pointerSmall       |     ›     |    »    |
| info               |     ℹ     |    i    |
| warning            |     ⚠     |    ‼    |
| hamburger          |     ☰     |    ≡    |
| smiley             |     ㋡     |    ☺    |
| mustache           |     ෴     |   ┌─┐   |
| heart              |     ♥     |    ♥    |
| arrowUp            |     ↑     |    ↑    |
| arrowDown          |     ↓     |    ↓    |
| arrowLeft          |     ←     |    ←    |
| arrowRight         |     →     |    →    |
| radioOn            |     ◉     |   (*)   |
| radioOff           |     ◯     |   ( )   |
| checkboxOn         |     ☒     |   [×]   |
| checkboxOff        |     ☐     |   [ ]   |
| checkboxCircleOn   |     ⓧ     |   (×)   |
| checkboxCircleOff  |     Ⓘ     |   ( )   |
| questionMarkPrefix |     ?⃝    |    ？    |

### License : [MIT](https://github.com/h4wldev/python-figures/blob/master/LICENSE) @ h4wldev
