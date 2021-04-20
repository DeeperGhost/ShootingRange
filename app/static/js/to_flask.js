function reg_role_event(id, value, id_user){
/*регестрация роли в соревновании*/
var url = '/reg_role_user_event'
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

function add_role_event(id_event, id_user, value){
/*добавление роли пользователя в соревновании*/
    var url = "/add_role_event"
    var formData = {
        id_user: id_user,
        id_event: id_event,
        value: value
    }
//    alert(formData.value + formData.id_event + formData.id_user)
    var json = JSON.stringify(formData);
    var xhr = new XMLHttpRequest();
    xhr.open('POST', url, true);
    xhr.responseType = 'json';
    xhr.send(json);
    xhr.onload = () => alert(xhr.response.status);
}