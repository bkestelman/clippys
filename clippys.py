import keyboard
import pyperclip as clipboard

clip_keys = ['0', '9', '8']
clips = {}

def copy(k):
	print(f'detected ctrl+c+{k}')
	keyboard.send('ctrl+c') 	# copy selected text
	clips[k] = clipboard.paste()	# into the corresponding clipboard
	print('clips:')
	print(clips)

def paste(k):
	print(f'detected ctrl+b+{k}')
	clipboard.copy(clips[k]) 	# take text from corresponding clipboard
	keyboard.send('ctrl+v') 	# paste it

print('setting up hotkeys')
for k in clip_keys:
	print(f'k={k}')
	keyboard.add_hotkey(f'ctrl+c+{k}', copy, args=[k])

for k in clip_keys:
	keyboard.add_hotkey(f'ctrl+b+{k}', paste, args=[k])

keyboard.wait()
