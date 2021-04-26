function open_dialog(data){
//открывает модальное окно
        (function() {
//        Закрывает модальное окно при нажатии на бек граунд
            favDialog.addEventListener('click', (event) => {
                if (event.target === favDialog) {
                    favDialog.close('cancelled');
                }
              });

          })();

    let dialog = document.getElementById('favDialog');

    change_data_dialog(data);

    dialog.showModal();
}

function close_dialog(){
//закрытие модального окна при нажатии на кнопку закрыть
    let dialog = document.getElementById('favDialog');
    dialog.close();
}

var url = '/show_result/'
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

var show_result = function(id_user){
getJSON(url+id_user,
function(err, data) {
  if (err !== null) {
    alert('Something went wrong: ' + err);
  } else {
//    alert('Your query count: ' + data.username);
//        document.write('<p>'+data.username+'<\p>')
//        document.getElementById('testID').textContent = data.username;
//        alert(data.name_player)
        open_dialog(data)
  }
});
};


function change_data_dialog(data){
        var elem = document.getElementById("li_name");
        elem.textContent = "имя - " + data.name_player;

        elem = document.getElementById("li_age");
        elem.textContent = "возраст - " + data.age_player;

        elem = document.getElementById("li_sex");
        elem.textContent = "пол - " + data.sex_player;

        elem = document.getElementById("li_city");
        elem.textContent = "город - " + data.city_player;

        elem = document.getElementById("li_organization");
        elem.textContent = "клуб - " + data.organization_player;

         elem = document.getElementById("li_rank");
         elem.textContent = "разряд - " + data.rank_name;

         elem = document.getElementById("li_event");
         elem.textContent = "соревнование - " + data.event_name;

         elem = document.getElementById("li_excercise");
         elem.textContent = "упражнение - " + data.section_player;

         elem = document.getElementById("li_result");
         elem.textContent = "результат - " + data.result_player;

         elem = document.getElementById("li_reached_rank");
         elem.textContent = "выполненый разряд - " + data.reached_rank;

         for(let i = 0; i < data.entries; i++){
             elem = document.getElementById("li_ex1");
             elem.textContent = `${i+1} подход - ` + data.ex1;
         }

          elem = document.getElementById("li_tens_count");
          elem.textContent = "количество 10 - " + data.tens_count;
};
