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

## Technical Discussion
It's a little annoying that clippys requires two combos to copy or paste (e.g. ctrl+c followed by ctrl+alt+c+0). Why is ctrl+c required? Because I haven't figured out how to grab the selected text from a window. Once the user copies text to clipboard with ctrl+c, I can do whatever I want with it. Ideally, this extra step on the part of the user will not be necessary. 

Just realized if the user is doing the extra step of copying with ctrl+c, I don't need the win32 api to control the clipboard - could just use pyperclip. Will update the master branch to get it working like the win32 branch, but with pyperclip. Grabbing selected text from window would be really nice, and is next priority. 
