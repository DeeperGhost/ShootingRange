var url = '/get_json_data'
//xhr.open('GET', url, true);

function q(id, value, id_user){
//    alert(id+' '+ value);
    var formData  = {
        id: id,
        value: value,
        id_user: id_user
    }
    var json = JSON.stringify(formData);
//    alert(formData.id);
//
    var xhr = new XMLHttpRequest();
    xhr.open('POST', url, true);
    xhr.responseType = 'json';

    xhr.send(json);

    xhr.onload = () => alert(xhr.response.status);
    }