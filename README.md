# clippys
simple clipboard manager for efficiency freaks

No GUI, no frills, no nonsense

Just ctrl+<+0, ctrl+<+9, ctrl+<+8 to copy to clipboard 0, 9, or 8

ctrl+>+0, ctrl+>+9, ctrl+>+8 to paste from clipboard 0, 9, or 8

Note: you don't need shift to do ctrl+> or ctrl+< (at least on my machine). I suppose technically they're ctrl+, and ctrl+. but '<' and '>' are visually appealing symbols for copy and paste. In fact, the code specifies '<' and '>', not ',' and '.'... but in my tests I haven't needed to use shift. Let me know if on your machine you do need shift. In any case it's easy to change the hotkeys in the code, or you can use a tool like AutoHotkey. 

## Security Warning

### Understand the risks of copying passwords or other sensitve info. This applies to the standard clipboard as well, but with clippys the risk is greater. Close clippys and the terminal it was running on before letting anyone use your computer. Although really you probably shouldn't be letting people use your computer, and definitely lock it with a strong password while you're away...

## Known limitations, plans for updates

Currently just 3 clipboards. In future update, you'll be able to add as many as you want (and possibly name them). Until then, if you want to add more it's easy to do so in the code (literally just add more clip_keys)

Using 0, 9, 8 instead of 1, 2, 3 because they are easier to reach after hitting ctrl (left ctrl at least... who uses right ctrl?)

If you don't like the hotkeys, it's easy to change them in the code, or just use a tool like AutoHotkey. 

It is probably not possible at the moment to use include 'alt' in the hotkeys. I thought at first this might be a limitation of the keyboard library or something to do with Windows blocking it, but I noticed that keyboard was correctly detecting alt presses, just not copying or pasting text. That's because to copy, I send an artificial ctrl+c press, but if you were pressing alt, the computer essentially receives ctrl+alt+c, which does nothing! Try it, ctrl+c copies, ctrl+alt+c does nothing... so basically that's why you can't use alt in your hotkey. 

Only tested on Windows, but the libraries used are cross platform (supposedly)
