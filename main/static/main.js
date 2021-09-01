function signup() {
      let f_name = document.querySelector("#fname").value;
      let l_name = document.querySelector("#lname").value;
      let email = document.querySelector("#email").value;
      let password = document.querySelector("#password").value;

      let user_info = {
        first_name: f_name,
        last_name: l_name,
        email: email,
        password: password
      };

      sendData(user_info, '/register');
      alert("clicked");
   }
   
    var sendData = function(data, url_endpoint) {
    $.ajax({
        type: "POST",
        url: '/register',
        contentType: "application/json",
        data: JSON.stringify({values : data}),
        dataType: "json",
        success: function(response) {
           alert("Wahoo")
        },
        error: function(err) {
            console.log(err);
            alert("Uh oh")
        }
    });
}