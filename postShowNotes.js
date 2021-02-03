let input_data = args.shortcutParameter;
let story_text = input_data.note_text;
let story_url = input_data.url;
let note_api_url = "https://reqbin.com/echo/post/json"

let request = new Request(note_api_url);
request.method = "POST";
request.addParameterToMultipart("url", story_url);
request.addParameterToMultipart("note text", story_text);

let response = await request.loadJSON();
let post_status = response.success;
console.log(post_status);
return post_status;
Script.complete();