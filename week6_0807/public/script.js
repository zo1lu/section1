function checkSigninRequired(){
    let username = document.getElementById("signin_username");
    let password = document.getElementById("signin_password");
    if (username.value=="" |password.value==""){
        alert("Please enter username and password!")
        return false;
    }else{
        return true;
    }
}

function checkSignupRequired(){
    let name = document.getElementById("signup_name");
    let username = document.getElementById("signup_username");
    let password = document.getElementById("signup_password");
    if(name.value==""|username.value==""|password.value==""){
        alert("Please enter name, username, and password!")
        return false;
    }else{
        return true;
    }
}

function deletionCheck(){
    text = "You really want to delete this message?"
    return confirm(text);
}