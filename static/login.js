var attempt = 3;
function validate(){
    var usuar= document.getElementById("usuar").value;
    var password = document.getElementById("password").value;
    if (usuar == "Alex" && password == "123"){
        alert("Ingreso exitosamente");
        window.location="principal";
        return false;
    }
    else {
        attempt--;
    }
    alert ("Te queda " + attempt+ " intentos más")
    document.getElementById("usuar").disable=true;
    document.getElementById("password").disable=true;
    document.getElementById("sumbit").disable=true;
}
