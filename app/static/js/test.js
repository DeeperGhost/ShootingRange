//var url1 = 'http://192.168.0.100:9999/test'
//var url1 = '/test'
var url1 = '/show_result/111'
var getJSON = function(url, callback) {
    var xhr = new XMLHttpRequest();
    xhr.open('GET', url, true);
    xhr.responseType = 'json';
    xhr.onload = function() {
      var status = xhr.status;
      if (status === 200) {
        callback(null, xhr.response);
      } else {
        callback(status, xhr.response);
      }
    };
    xhr.send();
};

var t = function(){
getJSON(url1,
function(err, data) {
  if (err !== null) {
    alert('Something went wrong: ' + err);
  } else {
//    alert('Your query count: ' + data.username);
//        document.write('<p>'+data.username+'<\p>')
//        document.getElementById('testID').textContent = data.username;
        alert(data.id)
  }
});
};