function checkAgreement(){
    let agreeBox = document.getElementsByName("agree_box")[0]
    if (!agreeBox.checked){
        alert("Please check the checkbox first")
        return false
    }
    return true
}

function checkPositiveAndRedirect(){
    let numberInput = document.getElementsByName("p_integer")[0]
    if(numberInput.value>0){
        let url = window.location
        let positiveNumber = numberInput.value.toString()
        let newUrl = url + `square/${positiveNumber}`
        window.location.replace(newUrl)
    }
    else{
        alert("Please enter a positive number")
        numberInput.value=0
        //? need return fasle?
        return false
    }
}

function backHome(){
    let url = window.location
    let newUrl = url.toString().split("/square/")[0]
    window.location.replace(newUrl)
}