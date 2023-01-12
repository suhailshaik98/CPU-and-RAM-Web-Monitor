import bottle
import json
import App
@bottle.route("/")
def serve_html():
  return bottle.static_file("index.html",root="")
@bottle.route("/front_end.js")
def serve_front_end_js():
  return bottle.static_file("front_end.js",root="")
@bottle.route("/ajax.js")
def serve_AJAX():
  return bottle.static_file("ajax.js",root="")
@bottle.post('/donut')
def serve_donut():
  jsonBlob = bottle.request.body.read().decode()
  print("This is json Blob "+jsonBlob,type(jsonBlob))
  content = json.loads(jsonBlob)
  print(content)
  start_year=content["hour_start"]
  end_year=content["hour_end"]
  dict={"hour_start":start_year,"hour_end":end_year}
  data=App.data_by_subject(dict)
  print(data)
  return json.dumps(data)
@bottle.post('/donut2')
def serve_donut2():
  jsonBlob = bottle.request.body.read().decode()
  print("This is json Blob for cpu "+jsonBlob,type(jsonBlob))
  content = json.loads(jsonBlob)
  print(content)
  start_year=content["hour_start"]
  end_year=content["hour_end"]
  dict={"hour_start":start_year,"hour_end":end_year}
  data=App.cpuramgraph(dict)
  print(data)
  return json.dumps(data)
  