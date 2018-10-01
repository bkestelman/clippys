import keyboard
import pyperclip as clipboard

clip_keys = ['0', '9', '8']
clips = {}

copy_hotkeys = {k: f'ctrl+alt+c+{k}' for k in clip_keys}
paste_hotkeys = {k: f'ctrl+alt+v+{k}' for k in clip_keys}

def copyTo(k):
	print(f'detected {copy_hotkeys[k]}')
	clips[k] = clipboard.paste()	# into the corresponding clipboard
	print('clips:')
	print(clips)

def pasteFrom(k):
	print(f'detected {paste_hotkeys[k]}')
	clipboard.copy(clips[k]) 	# take text from corresponding clipboard

print('setting up hotkeys')
for k in clip_keys:
	print(f'k={k}')
	keyboard.add_hotkey(copy_hotkeys[k], copyTo, args=[k])

for k in clip_keys:
	keyboard.add_hotkey(paste_hotkeys[k], pasteFrom, args=[k])

print('copy_hotkeys')
print(copy_hotkeys)
print('paste_hotkeys')
print(paste_hotkeys)

keyboard.wait()

