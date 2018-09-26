import keyboard
import pyperclip as clipboard

clip_keys = ['0', '9', '8']
clips = {}

copy_hotkeys = {k: f'ctrl+<+{k}' for k in clip_keys}
paste_hotkeys = {k: f'ctrl+>+{k}' for k in clip_keys}

def copy(k):
	print(f'detected {copy_hotkeys[k]}')
	keyboard.send('ctrl+c') 	# copy selected text
	clips[k] = clipboard.paste()	# into the corresponding clipboard
	print('clips:')
	print(clips)

def paste(k):
	print(f'detected {paste_hotkeys[k]}')
	clipboard.copy(clips[k]) 	# take text from corresponding clipboard
	keyboard.send('ctrl+v') 	# paste it

print('setting up hotkeys')
for k in clip_keys:
	print(f'k={k}')
	keyboard.add_hotkey(copy_hotkeys[k], copy, args=[k])

for k in clip_keys:
	keyboard.add_hotkey(paste_hotkeys[k], paste, args=[k])

print('copy_hotkeys')
print(copy_hotkeys)
print('paste_hotkeys')
print(paste_hotkeys)

keyboard.wait()

