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
