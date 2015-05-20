Title: zsh 技巧一则
Date: 2012-05-02 23:40
Author: Kardinal
Category: Tips
Slug: zsh-tip-2

其实这条配置在 eshell 里面用了很久了，用 zsh 的同学可能没有注意。

相当简单：空行的时候按回车，执行 `ls`。
  
“cd ....”之类，会根据点的个数补全路径，比如 “...” 补全为 “../../”，“....” 补全为 “../../..”

配合我修改的 tab 键：空行 tab 出 “cd ”，自己点点点后回车，O 了

    user-ret(){
        if [[ $BUFFER = "" ]] ;then
            BUFFER="ls"
            zle end-of-line
            zle accept-line
        elif [[ $BUFFER =~ "^cd\ ...+$" ]] ;then
            BUFFER=${${BUFFER//./..\\/}/..\\//}
            zle end-of-line
            zle accept-line
        else
            zle accept-line
        fi
    }
    zle -N user-ret
    bindkey "\r" user-ret
