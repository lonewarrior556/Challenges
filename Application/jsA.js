var contentKeys = "content.landingpages.podcasts|content.landingpages.podcasts.android|content.landingpages.podcasts.android.code|content.landingpages.podcasts.android.offer|content.landingpages.podcasts.android.partner|content.landingpages.podcasts.android.products|content.landingpages.podcasts.brainson|content.landingpages.podcasts.brainson.code|content.landingpages.podcasts.brainson.offer|content.landingpages.podcasts.brainson.partner|content.landingpages.podcasts.brainson.products|content.landingpages.podcasts.flitetest|content.landingpages.podcasts.flitetest.code|content.landingpages.podcasts.flitetest.offer|content.landingpages.podcasts.flitetest.partner|content.landingpages.podcasts.flitetest.products|content.landingpages.podcasts.ijustine|content.landingpages.podcasts.ijustine.code|content.landingpages.podcasts.ijustine.offer|content.landingpages.podcasts.ijustine.partner|content.landingpages.podcasts.ijustine.products|content.landingpages.podcasts.kipkay|content.landingpages.podcasts.kipkay.code|content.landingpages.podcasts.kipkay.offer|content.landingpages.podcasts.kipkay.partner|content.landingpages.podcasts.kipkay.products|content.landingpages.podcasts.techquickie|content.landingpages.podcasts.techquickie.code|content.landingpages.podcasts.techquickie.offer|content.landingpages.podcasts.techquickie.partner".split("|")
var content = {}


var createDirectory = function(){
  addContent(contentKeys[0])
  for (var i = 0; i<contentKeys.length; i++){
    if (!eval(contentKeys[i])){
      eval( contentKeys[i] + "= {}")
    }
  }
  return content
}

var addContent = function(key){
  keyBreak = key.split(".")
  for (var i = 0; i < key.split(".").length; i++){
    if (!eval(keyBreak.slice(0,i+1).join("."))){
      eval(keyBreak.slice(0,i+1).join(".")+"={}")
    }
  }
}

var build = function(obj, str){
  if ( Object.keys(obj).length === 0){
    return "<li>"+ str + "</li>"
  }
  else{
    var path= "<li>" +str+ "<br><ul><br>"
    for (var x in obj){
      path += arguments.callee(obj[x], x)
    }
    path += "<br></ul><br></li>"
  }
  return path
}

exports.allContentKeys = function(){
  content = createDirectory()
  return build(content, "content")
}

exports.addContentKey = function(key){
  addContent(key)
  return build(content, "content")
}
