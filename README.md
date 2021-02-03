Hello! This is the first time I've ever tried to do anything with Shortcuts. The problem statement, as I understood it, was this:

## Problem
> Run the contents of a browser bookmarklet from an RSS reader without manually propagating data from the app to Safari.

## Solution
The pieces I've assembled that I _think_ achieve this require these iOS apps:

- Pythonista
- Scriptable
- Shortcuts

Here is [the link to the Shortcut I've created](https://www.icloud.com/shortcuts/81ebf03d2de44d73aff56d51ea5650b0). This workflow starts in Pythonista; I couldn't find a way that Newsly or Feedly exposed their article metadata through Shortcuts, but that would be simpler.

### Workflow
In a nutshell, here's the flow:

1. Install the apps.
2. Create a new Python file in Pythonista and move the content of `postShowNotes.py` to that file.
3. Create a new JavaScript file in Scriptable and move the content of `postShowNotes.js` to that file. I've named mine "Post Show Notes".
3. In Pythonista, go to `Settings / Share Extension / Shortcuts` and add the script you created in the step above.
4. Tap the link above to the Shortcut and add to Shortcuts.
5. Open Newsly and find a story worth sharing.
6. Open the Share Sheet and choose `Run Pythonista Script`. Choose the Python script you created above.

With any luck I haven't skipped any steps or settings and everything is flawless. If not, feel free to file an issue.

## Customize
The JavaScript script just hits a dummy API endpoint. So long as you pay attention to the `args` statements that ingest data passed to the Scriptable kernel from Shortcuts, you should be able to do anything a bookmarklet can do. There is a limit to the system resources given to Shortcuts actions, but I don't anticipate that'll be an issue.

Also the JavaScript is garbage because I don't know from JavaScript.
