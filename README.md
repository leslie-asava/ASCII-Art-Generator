# Images-to-ASCII-Art
My implementation of an ASCII art generator using Python. It aims to generate ASCII art from images and videos.

#       Original vs Generated ASCII Art
![gumball](https://user-images.githubusercontent.com/51715921/209464016-fa642320-b321-47e1-b2f5-dbf8b2559adb.png)
<img src="https://user-images.githubusercontent.com/51715921/209464006-a7bb18e6-69bc-43c0-a5e7-c0773fa01001.png" width="189" height="267" />

```@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#-    .O@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%  -ii-  i@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@% :iiiiiii .#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@# :iiiiiiiii -@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#  iiiiiiiiiii +@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@| iiiiiiiiiiii- #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@# ..             i@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@#%|      :-iiiiii-:     |O@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@%:   :-iiiiiiiiiiiiiiiiii:   =#@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@#####@@@@@@@@@@#|   iiiiiiiiiiiiiiiiiiiiiiiiii:  i#@@@@@@@@@@@@@@@@@@@@@
@@@#+.      .iO@@@@#i  -iiiiiiiiiiiiiiiiiiiiiii--iiiii-  +@@@@@@@@@@@@@@@@@@@@
@@%  .-iiii-.   i#|  -iiiiiiiiiiiiiiiiiiiiiiii      -iii: :#@@@@@@@@@@@@@@@@@@
@+ :iiiiiiiiiii-   -ii.   .iiiiiiiiiiiiiiiiiii        -iii  O@@@@@@@@@@@@@@@@@
# :iiiiiiiiiiii. .ii       iiiiiiiiiiiiiiiiiii-        -iii  O@@@@@@@@@@@@@@@@
- iiiiiiiiiiii  ii-        iiiiiiiiiiiiiiiiiiiiiii-     iiii: O@@@@@@@@@@@@@@@
 -iiiiiiiiiii  iii      :-iiiiiiiiiiiiiiiiiiiiiiiiii:  :iiiii. #@@@@@@@@@@@@@@
 iiiiiiiiiii  iii-   .iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii  @@@@@@@@@@@@@@
 iiiiiiiiii  iiiii  :iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii =@@@@@@@@@@@@@
 iiiiiiiii  iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii- #@@@@@@@@@@@@
 iiiiiiii: iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii---iiiiiiiiii -@@@@@@@@@@@@
 :iiiiiii :iiiiiiiiiiiiii---iiiiiiiiiiiiiiiiiiii        :iiiiiii- #@@@@@@@@@@@
- iiiiii  iiiiiiiiiii.         iiiiiiiiiiiiiii  .%#####+  .iiiiii |@@@@@@@@@@@
+ iiiii- iiiiiiiiii:  =#@@@@#%.  iiiiiiiiiiii  O@@@@@@@@@%  iiiii- @@@@@@@@@@@
# -iiii  iiiiiiiii  +#@@@@@@@@@O  iiiiiiiiii i#@@@@@@@@@@@#. iiiii O@@@@@@@@@@
@: iiii -iiiiiiii  #@@@@@@@@@@@@@: iiiiiiii -@@@@@@@@@@@@@@#  iiii |@@@@@@@@@@
@O iii: iiiiiiii: #@@@@@@@@@@@@@@#. iiiiii: #@@@@@@@@@@@@@@@# -iii: @@@@@@@@@@
@@ .ii .iiiiiiii %@@@@@@@@@@@@@@@@# :iiiii %@@@@@@#%||%#@@@@@= iii- #@@@@@@@@@
@@+ ii iiiiiiii .@@@@@@@@#==O@@@@@@+ iiii- @@@@@@#      #@@@@# -iii #@@@@@@@@@
@@# :- iiiiiiii O@@@@@@#      O@@@@# :iii -@@@@@#        #@@@@: iii O@@@@@@@@@
@@@+ : iiiiiii- #@@@@@#        #@@@@i iii +@@@@@i        -@@@@= iii %@@@@@@@@@
@@@#   iiiiiii: @@@@@@|        :@@@@% iii %@@@@@          @@@@% iii +@@@@@@@@@
@@@@% .iiiiiii.:@@@@@@          #@@@# iii %@@@@#          @@@@% iii .O@@@@@@@@
@@@@# .iiiiiii -@@@@@@          #@@@# iii +@@@@@          @@@@+ iii-  -#@@@@@@
@@@@@ .iiiiiii..@@@@@@          #@@@# iii -@@@@@i        |@@@@i iiiiii  +@@@@@
@@@@@ .iiiiiii- @@@@@@|        :@@@@% iii- @@@@@#        #@@@@ :iiiiiii: =@@@@
@@@@@ .iiiiiiii #@@@@@#        #@@@@i iiii +@@@@@#     .#@@@@O iiiiiiiiii |@@@
@@@@@:.iiiiiiii |@@@@@@#      O@@@@# -iiii: #@@@@@@O==O@@@@@@  iiiiiiiiii- +@@
@@@@@- iiiiiiii- #@@@@@@#O==O#@@@@@+ iiiiii -@@@@@@@@@@@@@@@= iiiiiiiiiiii- #@
@@@@@| iiiiiiiii :@@@@@@@@@@@@@@@@# :iiiiiii i@@@@@@@@@@@@@+ -iiiiiiiiiiiii .@
@@@@@+ iiiiiiiiii |@@@@@@@@@@@@@@#  iiiiiiiii  #@@@@@@@@@#i -iiiiiiiiiiiiiii O
@@@@@O iiiiiiiiii- i#@@@@@@@@@@@#               .i+O@@@#|  iiiiiiiiiiiiiiiii i
@@@@@# iiiiiiiiiiii  O@@@@@@@@@+    |+%OOO:  :..         :iiiiiiiiiiiiiiiiii: 
@@@@@@ :iiiiiiiiiiii.  |%O#O%i  -ii  :+OOOO=     .OO+  iiiiiiiiiiiiiiiiiiiiii 
@@@@@@| iiiiiiiiiiiiii:       :iiiii-   :=OOOOO %OOOOO .iiiiiiiiiiiiiiiiiiiii 
@@@@@@# iiiiiiiiiiiiiiiiiiiiiiiiiiiiiii-     i= -%%%%= :iiiiiiiiiiiiiiiiiiiii 
@@@@@@@ -iii  -iiiiiiiiiiiiiiiiiiiiiiiiiiii-.         .iiiiiiiiiiiiiiiiiiiiii 
@@@@@@@- ii   iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii 
@@@@@@@O -   iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii-  iiii 
@@@@@@@#   .iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii   ii- 
@@@@@@@@% -iiiiiii-iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii.  : :
@@@@@@@@@ .iiiiii. -iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii-   +
@@@@@@@@@% -iiii-  iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii  #
@@@@@@@@@@- iiii  iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii.iiiiiiii :@
@@@@@@@@@@#  ii  -iiiiii-iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii   iiiiiii #@
@@@@@@@@@@@# .  :iiiiii-  iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii   iiiii i@@
@@@@@@@@@@@@%   iiiiiii  -iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii   iii  #@@
@@@@@@@@@@@@@O  iiiiii  :iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii   i  #@@@
@@@@@@@@@@@@@@O  -iii:  iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii    O@@@@
@@@@@@@@@@@@@@@#-  ii  iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii-  #@@@@@
@@@@@@@@@@@@@@@@@%    :iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii-  |@@@@@@@
@@@@@@@@@@@@@@@@@@@+   -iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii:  i#@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@#-   .-iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii:    =@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@O|.      :--iiiiiiiiiiiiiiii--:.      -+#@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@##O+i.     .:-iiiiiii-      .-=%##@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#        .-ii @@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@             #@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@O             +@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@i               .@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@% %OO.          - |@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@--OOO% i.       .% @@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@--OOOO OOOO%=:   O @@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@| OOOO%OOOOOOOO% O #@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@% OOOOOOOOOOOOO% O #@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@O OOOO=+OOOOOOO% % %@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@# OOOO.iOOOOOOOO + +@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ OOOO--OOOOOOOO |.|@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ %OOOi:OOOOOOOO:--i@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ +OOO| OOOOOOOOi.|:@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ |OOO= OOOOOOOO| = @@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@: i|=| OOOOOOOO+   #@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@|      OOOOOOOO%   #@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+      %OOOOOOOO   #@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%      %OOOOOOOO   #@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@O      +OOOOOOOO   O@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#      +OOOOOOOO.  +@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#      =OOOOOOOOi  |@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@      iOOOOOOOOO%- O@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ .:.  :+++++++++++.:@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@= -iii               @@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@# -iiii:    .ii:      @@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@i iiiii:             =@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@..- iii.            .#@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@: . i i             O@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#:   :: .            i#@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#=  i  .              +@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#  :iii   |           O@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@+  iiii- O@@           O@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@O :iiii- +@@@           O@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@..iiii: =@@@#           #@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@ :iii  +@@@@O           #@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@=    :#@@@@@%           #@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@#+%#@@@@@@@= OOO% OOO% #@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@--OOO+ OOO% @@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.|OOO= OOO% @@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%:  .::. ::.  :%@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#.  ::.      .:-. :#@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@| -.i-iii  iii-i.: %@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   .  iii  iii  :  i@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@i .. iii-  -iii  : +@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#.       =i       i#@@@@@@@@@@@@@@@@@@@@@@@```

