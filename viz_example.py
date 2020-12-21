# Making Data Into Something You Can See - PluralSight tutorial 


import pygal

bar = pygal.Bar()
bar.title = "Cyborg Kills"
bar.add('Alita', 3)
bar.add('Major', 4)
bar.add('Sarah', 100)

bar.render_in_browser()