// Когда html документ готов (прорисован)

// $(document).ready(function () {
//   // берем в переменную элемент разметки с id jq-notification для оповещений от ajax
//   // var successMessage = $("#jq-notification");

//   // Ловим собыитие клика по кнопке добавить в избранное
//   $(document).on("click", "#favorite", function (event) {
//     // Блокируем его базовое действие
//     event.preventDefault();

//     var pk = $(this).attr("value");
//     var url = $(this).attr("href");
//     var csrftoken = getCookie("csrftoken");
//     console.log(pk);

//     $.ajax({
//       headers: { "X-CSRFToken": csrftoken },
//       type: "POST",
//       url: url,
//       data: {
//         id: pk,
//       },
//       contentType: "application/json",
//       dataType: "json",
//       success: function (response) {
//         $("#favorites-selection").html(response["form"]);
//         console.log($("#favorites-selection").html(response["form"]));
//       },
//       error: function (rs, e) {
//         console.log(rs, e);
//       },
//     });
//   });
// });
// function getCookie(name) {
//   let cookieValue = null;
//   if (document.cookie && document.cookie !== "") {
//     const cookies = document.cookie.split(";");
//     for (let i = 0; i < cookies.length; i++) {
//       const cookie = jQuery.trim(cookies[i]);
//       if (cookie.startsWith(name + "=")) {
//         cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
//         break; // Выходим, как только найдём нужное cookie
//       }
//     }
//   }
//   return cookieValue;
// }
