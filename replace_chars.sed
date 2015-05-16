s:[\]\.:.:g
s:[\]\*:*:g
s:[\]\^:^:g
s:[\]\$:$:g
s:[\]#:#:g
s:[\]`:`:g
s:[\]~:~:g
s:[\]<:<:g
s:[\]>:>:g
s/^(Author: )admin$/\1toy/
s/^(Category:.*?),.*$/\1/
s/^(Tags:.*?)GTK2(.*)$/\1GTK\2/
s/^(Tags:.*?)gtk3(.*)$/\1GTK\2/
s/^(Tags:.*?)kde4(.*)$/\1KDE\2/
s/^(Tags:.*?)KDE5(.*)$/\1KDE\2/
s/^(Tags:.*?)qt4(.*)$/\1QT\2/
s/^(Tags:.*?)qt5(.*)$/\1QT\2/
s/^(Tags:.*?)KDE 4,(.*)$/\1\2/
s/^(Tags:.*?)KDE 4\.[0-9](.*)$/\1\2/
