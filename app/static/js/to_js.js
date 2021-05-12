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
var edit_result = function(id_user){
getJSON(url+id_user,
function(err, data) {
  if (err !== null) {
    alert('Something went wrong: ' + err);
  } else {
//    alert(data.name_player); 
    openEditDialog(data);
  }
});
};

function openEditDialog(data){
  //открывает модальное окно
          (function() {
  //        Закрывает модальное окно при нажатии на бек граунд
              editDialog.addEventListener('click', (event) => {
                  if (event.target === editDialog) {
                      editDialog.close('cancelled');
                  }
                  // вызов обработчика отправки формы
                  if(event.target === submitResForm) {
                    onSubmitRes(data["id_user"]);
                  }
                });
  
            })();
      let dialog = document.getElementById('editDialog'); 
      changeEditDialog(data);
      dialog.showModal();
}

function changeEditDialog(data){
  // Заполняет форму начальными данными из бд
    elem = document.getElementById("editDialogH3");
    elem.textContent = "Внесение результатов участника"
  
    for(let i = 1; i < 11; i++){
      if (data.entries >= i){
        document.getElementById(`ex${i}`).value = data[`ex${i}`];
        document.getElementById(`ex${i}`).hidden=false; 
        document.getElementById(`label_ex${i}`).hidden=false; 
      }
      else{
        document.getElementById(`ex${i}`).value = 0;
        document.getElementById(`ex${i}`).hidden=true; 
        document.getElementById(`label_ex${i}`).hidden=true; 
        // document.getElementById(`ex${i}`).remove(); 
        // document.getElementById(`label_ex${i}`).remove(); 
      }
    }
    document.getElementById("tens").value = data.tens_count;
  }

function onSubmitRes(idUser) {
  // отправка формы результатов на сервер
//   document.getElementById("resForm").submit();
  let form = document.forms.resForm;
  if (!form.checkValidity())
  {
    alert("PROBLEM IN FORM");
    return false
  }
  else{
    let elem = form.elements;
    let formData ={
      idUser: idUser,
      ex1: Number(elem.ex1.value),
      ex2: Number(elem.ex2.value),
      ex3: Number(elem.ex3.value),
      ex4: Number(elem.ex4.value),
      ex5: Number(elem.ex5.value),
      ex6: Number(elem.ex6.value),
      ex7: Number(elem.ex7.value),
      ex8: Number(elem.ex8.value),
      ex9: Number(elem.ex9.value),
      ex10: Number(elem.ex10.value),
      tens: Number(elem.tens.value)
    }

    var url_edit = '/edit_result/'
    var json = JSON.stringify(formData);
    var xhr = new XMLHttpRequest();
    xhr.open('POST', url_edit+idUser, true);
    xhr.responseType = 'json';
    xhr.send(json);
    xhr.onload = () => alert(xhr.response.status);
  }
}
