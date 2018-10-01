# clippys
simple clipboard manager for efficiency freaks

Check out win32 branch for a working version (Windows only)

### Technical Discussion

master branch contains a sort of working version, but has some problems: basically, programs like google docs have a keyboard shortcut for every useless functionality you could possibly think of, so all the ctrl+whatever combos are taken (yes, even ctrl+< and ctrl+>). My solution to this would have been to use alt, but this causes another problem: the way the code on master works is it literally sends 'ctrl+c' whenever the "copy_hotkey" is pressed. But if the copy_hotkey contains alt, essentially ctrl+alt+c will be pressed simultaneously. As you can test for yourself, this will fail to copy. 

Thus, I had to develop a solution that would copy text without sending keystrokes (ctrl+c or ctrl+v), but rather using system api's. 

So far, I have only developed this for Windows using pywin32. 
