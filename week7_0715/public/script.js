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

function searchMember(){
    let search_member_result = document.getElementById("search_member_result");
    let username = document.getElementById("user_name").value;
    let url = `/api/member?username=${username}`
    fetch(url,{
        method:"GET"
    })
    .then((data)=>{
        return data.json()
    })
    .then((result)=>{
        search_member_result.innerText = `${result.data.name}(${result.data.username}) is our member!`
    })
    .catch(()=>{
        search_member_result.innerText = `Something went wrong`
    })
}

function updateName(){
    let newName = document.getElementById("new_name").value;
    const updateResult = document.getElementById("update_result");
    let headers = {
        "Content-Type":"application/json"
    };
    let body = {
        "name":newName
    };
    const request = new Request("/api/member",{
        method:"PATCH",
        headers: headers,
        body:JSON.stringify(body)
    }) 

    fetch(request)   
    .then((res)=>{
        return res.json();
    })
    .then((data)=>{
        if (data.ok){
            updateResult.innerText = "Update Successfully!"
        }else{
            updateResult.innerText = "Something Wrong, please try again."
        }
    })
    .catch((e)=>{
        console.log(e)
        updateResult.innerText = "Something Wrong, please try again."
    })

}