$(document).ready(function () {
    $("#form").submit(function (event) {
        event.preventDefault()
        var username = $("#username").val()
        var password = $("#password").val()

        let auth = btoa(username + ":" + password);


        fetch("https://api.github.com/user", {
            headers: {
                'Authorization': 'Basic ' + auth
            }
        })
            .then(function (data) {
            return data.json()
            })
            .then(function (data) {
                $("#username").val("")
                $("#password").val("")
                if (data.message == "Bad credentials") {
                    alert("wrong credentials")
                }
                else {
                    var result = `<img class="img-thumbnail ml-4" width="100" height="100" src="${data.avatar_url}"/><br><h1>${data.login}</h1><br><a target="_blank" href="${data.html_url}"><button class="btn btn-success">See Profile</button></a>`
                    $("#result").html(result)
                }
                console.log(data)
        })
    })
})