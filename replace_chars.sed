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
