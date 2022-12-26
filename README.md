# Images-to-ASCII-Art
My implementation of an ASCII art generator using Python. It aims to generate ASCII art from images and videos.

#       Original vs Generated ASCII Art
![gumball](https://user-images.githubusercontent.com/51715921/209464016-fa642320-b321-47e1-b2f5-dbf8b2559adb.png)
<img src="https://user-images.githubusercontent.com/51715921/209464006-a7bb18e6-69bc-43c0-a5e7-c0773fa01001.png" width="189" height="267" />

```
@@@@@@@@@@@@@@@@@@@@@@@@@#:   .O@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@O .iii- =@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@# -iiiiii +@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@:.iiiiiiii #@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@% :.      . .@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@Oi    .::---:.   .=#@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@Oi  .iiiiiiiiiiiiiiii  :O@@@@@@@@@@@@@@@@
@@@+:. ..|O@@@O. .iiiiiiiiiiiiiiiii-iii: -#@@@@@@@@@@@@@@
@%  -iii-.  i: -iiiiiiiiiiiiiiiii-    .ii. %@@@@@@@@@@@@@
O -iiiiiiii: :i     iiiiiiiiiiiiii      -ii =@@@@@@@@@@@@
.-iiiiiiii  i:      iiiiiiiiiiiiiiii:    iii =@@@@@@@@@@@
 iiiiiiii  ii    -iiiiiiiiiiiiiiiiiiii: :iiii %@@@@@@@@@@
 iiiiiii  iii  -iiiiiiiiiiiiiiiiiiiiiiiiiiiiii #@@@@@@@@@
 iiiiii  iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii.-@@@@@@@@@
 iiiii- iiiiiiiiiiiiiiiiiiiiiiiiiiii.   :iiiiii #@@@@@@@@
 iiiii -iiiiiii-      :iiiiiiiiii-  |OO+-  iiii:-@@@@@@@@
i.iii: iiiiiii .%#@@@O: -iiiiiii: %@@@@@@#i iiii #@@@@@@@
O iii iiiiiii +@@@@@@@@O -iiiii- #@@@@@@@@@+ iii %@@@@@@@
@ -i- iiiiii %@@@@@@@@@@# -iiii #@@@@@@@@@@@| ii:i@@@@@@@
@+ i .iiiii i@@@@@@@@@@@@% iii:-@@@@#i .%@@@# ii-.@@@@@@@
@@ i -iiiii #@@@@%   -#@@@.-ii O@@@#     |@@@i.ii @@@@@@@
@@+  iiiii-.@@@@O      @@@= ii #@@@.      #@@% ii #@@@@@@
@@@  iiiii.|@@@@       %@@# ii @@@@       =@@O ii #@@@@@@
@@@% iiiii.=@@@@       |@@# ii #@@@       +@@O ii. |#@@@@
@@@O iiiii:i@@@@       +@@# ii O@@@i      #@@= iiii  O@@@
@@@O iiiii-.@@@@+      #@@% ii.i@@@#     %@@@ -iiiii- O@@
@@@# iiiiii #@@@@|    O@@@::iii #@@@#%i=#@@@% iiiiiiii O@
@@@# iiiiii.-@@@@@#O#@@@@O iiii: #@@@@@@@@@# -iiiiiiii- #
@@@@ iiiiiii +@@@@@@@@@@# -iiiii: O@@@@@@@O :iiiiiiiiii +
@@@@.iiiiiiii =@@@@@@@@#            -%##%. -iiiiiiiiiii-.
@@@@-:iiiiiiii  +#@@@#i : :%OOO      :   -iiiiiiiiiiiiii 
@@@@+ iiiiiiiii-      .iii:  -%O%+ =OOO- iiiiiiiiiiiiiii 
@@@@# iii-iiiiiiiiiiiiiiiiiii.   .  ==i :iiiiiiiiiiiiiii 
@@@@@.-i. :iiiiiiiiiiiiiiiiiiiiii-:   .-iiiiiiiiiiiiiiii 
@@@@@+   :iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii- -ii 
@@@@@@  -iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii  :i 
@@@@@@= iiiii iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii.  :
@@@@@@# -iii  iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii- %
@@@@@@@% ii  iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii iiiiii #
@@@@@@@@|   -iiii  iiiiiiiiiiiiiiiiiiiiiiiiiiiii  iiii +@
@@@@@@@@@i :iiii- :iiiiiiiiiiiiiiiiiiiiiiiiiiiiii  ii :@@
@@@@@@@@@@| -iii  iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii   .#@@
@@@@@@@@@@@%  i  iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii- -#@@@
@@@@@@@@@@@@#i  -iiiiiiiiiiiiiiiiiiiiiiiiiiiiiii-  %@@@@@
@@@@@@@@@@@@@@#|   -iiiiiiiiiiiiiiiiiiiiiiiii-   +#@@@@@@
@@@@@@@@@@@@@@@@@#=.     .:-iiiiiiii:..      :+#@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@#O%+|i    :iii: i|=+O#@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@#         .@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@+          O@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@|.=:         O@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@ OOO .      +:@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@ OOO:OOO%=- % @@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@.%OOOOOOOOO.+ @@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@:+OO=%OOOOO-| @@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@i|OO-|OOOOO|: @@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@=-OOiiOOOOO+..#@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@%:OO=-OOOOO% :%@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@O +%=.OOOOOO  =@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@#     OOOOOO  |@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@#     OOOOOO  -@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@     OOOOOO. .@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@     OOOOOO-  @@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@.    %OOOOO+  #@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@:    +%%%%%%%i:@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@O -ii    :::    @@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@ -iii          :@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@ i.ii          O@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@O .  i         i@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@#i . :          i@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@%  ii  :        |@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@= -ii- #@        =@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@# iii: #@@        +@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@# i-  #@@#        +@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@=.:+#@@@# =|. .: %@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@# OO=-OO.O@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@%.%OiiO% %@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@+            #@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@# .-:ii :ii-:..@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@O    ii .ii .  @@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@#.     -      =@@@@@@@@@@@@@@@@@

```

