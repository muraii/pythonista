import appex, webbrowser
import urllib.parse
import clipboard
import json
import shortcuts

# Get the data.
urls = appex.get_urls()
text = appex.get_text()

# Create the output object.
note_body = {
	'url': urls[0],
	'note_text': text
}

note_body_json = json.dumps(note_body)

# Paste to clipboard
clipboard.set(note_body_json)

# Create POST.
run_url_base = 'shortcuts://x-callback-url/run-shortcut?name='
shortcut_name = urllib.parse.quote('PostShowNotes')
shortcut_input = 'clipboard'
shortcut_input = 'text&text=drep'
run_url = f'{run_url_base}{shortcut_name}&input={shortcut_input}'

# POST data
webbrowser.open(run_url))
