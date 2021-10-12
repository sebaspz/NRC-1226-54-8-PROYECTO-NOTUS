//var userNameInput = document.formularioRegistro.username;
//window.status="Hola mundo";
function validar()
{
    var userNameInput = document.formularioRegistro.username;
    var passWordInput = document.formularioRegistro.userPassword;
    var correoInput = document.formularioRegistro.correo;

    var formato_email = /^\w+([\.-]?\w+)@\w+([\.-]?\w+)(\.\w{2,3})+$/;

    var swErrores=false;

    console.log(userNameInput.value + "-"+passWordInput.value+"-"+correoInput.value);



    if(userNameInput.value.length < 8)
    {
        //alert("El nombre de usuario debe tener mínimo 8 caracteres.");
        document.getElementById("errorUsername").innerHTML="El nombre de usuario debe tener mínimo 8 caracteres.";
        userNameInput.focus();
        //document.getElementById("botonEnviar").disabled=true;
        swErrores=true;
    }

    if(passWordInput.value.length < 4)
    {
        //alert("La clave debe tener mínimo 8 caracteres.");
        document.getElementById("errorPassword").innerHTML="La clave debe tener mínimo 4 caracteres.";
        passWordInput.focus();
        swErrores=true;
    }

    if(!correoInput.value.match(formato_email))
    {
        //alert("Por favor escriba un correo válido.");
        document.getElementById("errorMail").innerHTML="Por favor escriba un correo válido.";
        correoInput.focus();
        swErrores=true;
    }


    if( swErrores==true)
    {
        return false;
    }
    else{
        return true;
    }
}


function verClave()
{
    console.log('Mostrar clave');

    var passWordInput = document.formularioRegistro.userPassword;
    passWordInput.type="text";
}

function ocultarClave()
{
    console.log('Ocultar clave');
    var passWordInput = document.formularioRegistro.userPassword;
    passWordInput.type="password";

    
}

function ocultarVerClave()
{
    var passWordInput = document.formularioRegistro.userPassword;
    var tipo = passWordInput.type;

    console.log(tipo);

    if(tipo=="text")
    {
        passWordInput.type="password";
    }

    if(tipo == "password")
    {
        passWordInput.type="text";
    }
}


 