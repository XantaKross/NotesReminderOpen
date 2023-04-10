let boolean = -1; // default value.

function getCookie(name) {
  const value = `; ${document.cookie}`;
  const parts = value.split(`; ${name}=`);
  if (parts.length >= 2) return parts.pop().split(';').shift();
}

const csrf_token = getCookie('csrftoken');


function showTable(container) {
    $.ajax({
        type: 'POST',
        url:  '/Homepage/',
        data: {"csrfmiddlewaretoken": csrf_token,
               "input": container,
               "remove_or_add": boolean},

        success: function(data) {


            let Table = document.getElementById("TableBody");
            let tr = "";
            let Queries = data["Data"];

            Table.innerHTML = '';

            for(let row=0; row < Queries.length; row++) {
                tr += "<tr>";
                for(let clm=0; clm < Queries[row].length; clm++) {
                    tr += "<td>" + Queries[row][clm] + "</td>";
                }
                tr+='</tr>';
            }
            Table.innerHTML += tr;

            boolean = -1; // reset to default value.
       }

    });

}



function logOut() {
    $.ajax({
        type: 'GET',
        url: '/Logout/',

        success: function() {
            window.setTimeout(function () {location.href = "/Login/";}, 100);
            console.log("Logout Success.");
        }

    });

}

window.onload = showTable('');