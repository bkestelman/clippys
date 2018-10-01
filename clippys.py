'''
Use:
User must first copy text normally (ctrl+c) to put it in standard clipboard.
Then use one of the copy_hotkeys to copy from the standard clipboard to one of the managed clipboards.
Then use one of the paste_hotkeys to paste from a managed clipboard to the standard clipboard.
Then paste normally (ctrl+v)
'''
import keyboard
import win32.win32clipboard as clipboard

clip_keys = ['0', '9', '8']
clips = {}

copy_hotkeys = {k: f'ctrl+alt+c+{k}' for k in clip_keys}
paste_hotkeys = {k: f'ctrl+alt+v+{k}' for k in clip_keys}

def copyTo(k):
	print(f'detected {copy_hotkeys[k]}')
	clipboard.OpenClipboard()
	clips[k] = clipboard.GetClipboardData()
	clipboard.CloseClipboard()
	print('clips:')
	print(clips)

def pasteFrom(k):
	print(f'detected {paste_hotkeys[k]}')
	clipboard.OpenClipboard()
	clipboard.EmptyClipboard() 
	print(f'putting {clips[k]} in clipboard')
	clipboard.SetClipboardText(clips[k])
	clipboard.CloseClipboard()

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

