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

//Заполняет результаты если они есть
    for(let i = 0; i < 10; i++){
        elem = document.getElementById(`li_ex${i+1}`);
        if (data.entries){
            if (data.entries >= i+1){
                elem.textContent = `${i+1} подход - ` + data[`ex${i+1}`];
                elem.style.display = "block";
            }
            else{
                elem.textContent = `${i+1} подход - ` + "None";
                elem.style.display = "none";
            }
        }
        else{
            elem.textContent = `${i+1} подход - ` + "None";
            elem.style.display = "none";
        }
    }

    elem = document.getElementById("li_tens_count");
    elem.textContent = "количество 10 - " + data.tens_count;
};
/*=========================================================================*/
/*EDIT_RESULT*/
function openEditDialog(data){
//открывает модальное окно
        (function() {
//        Закрывает модальное окно при нажатии на бек граунд
            editDialog.addEventListener('click', (event) => {
                if (event.target === editDialog) {
                    editDialog.close('cancelled');
                }
              });

          })();
    let dialog = document.getElementById('editDialog');

    changeEditDialog(data);

    dialog.showModal();
}
function changeEditDialog(data){
  elem = document.getElementById("editDialogH3");
  elem.textContent = "Внесение результатов участника"

  for(let i = 1; i < 11; i++){
    if (data.entries >= i){
      document.getElementById(`ex${i}`).value = data[`ex${i}`];
      document.getElementById(`ex${i}`).hidden=false; 
      document.getElementById(`label_ex${i}`).hidden=false; 
    }
    else{
      // document.getElementById(`ex${i}`).style.display = "none";
      document.getElementById(`ex${i}`).hidden=true; 
      document.getElementById(`label_ex${i}`).hidden=true; 
      // document.getElementById(`label_ex${i}`).style.display = "none";
    }
  }
  // document.getElementById("ex1").value = data.ex1;
  // document.getElementById("ex2").value = data.ex2;
  // document.getElementById("ex3").value = data.ex3;
  // document.getElementById("ex4").value = data.ex4;
  // document.getElementById("ex5").value = data.ex5;
  // document.getElementById("ex6").value = data.ex6;
  // document.getElementById("ex7").value = data.ex7;
  // document.getElementById("ex8").value = data.ex8;
  // document.getElementById("ex9").value = data.ex9;
  // document.getElementById("label_ex9").style.display = "none";
  // document.getElementById("ex9").style.display = "none";
  // document.getElementById("ex10").value = data.ex10;

  document.getElementById("tens").value = data.tens_count;
  // elem.document.getElementById("ex1");
  // elem.value = data.ex1;

  // elem.document.getElementById("ex2");
  // elem.value = data.ex2;
  // alert(data.ex10)
}

var url_edit = '/edit_result/'
var edit_result = function(id_user){
getJSON(url+id_user,
function(err, data) {
  if (err !== null) {
    alert('Something went wrong: ' + err);
  } else {
//    alert(data.name_player);

    var formData = {
        id_user: 1,
        id_event: 11,
        value: 111,
        test :12
    }

    openEditDialog(data)

    var json = JSON.stringify(formData);
    var xhr = new XMLHttpRequest();
    xhr.open('POST', url_edit+id_user, true);
    xhr.responseType = 'json';
    xhr.send(json);
    xhr.onload = () => alert(xhr.response.status);

  }
});
};
