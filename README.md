# clippys
simple clipboard manager for efficiency freaks

## Usage
```python clippys.py```
clippys currently lets you manage up to 3 clipboards, called 0, 8, and 9. 

To copy something into clippys, first copy to the system clipboard with ctrl+c

Then store it in one of clippy's clipboards with ctrl+alt+c+'0, 9, or 8'

To paste from one of clippy's clipboards, first load from the system clipboard with ctrl+alt+v+'0, 9, or 8'

Then paste with ctrl+v

## Customizing
The code is really simple and easy to edit. 

If you want to change the hotkeys, simply modify the "clip_keys" list. You can have as many as you want. You don't need to touch any other part of the code - just change the list and it will work. But be aware that many key combos are used by other programs. 
