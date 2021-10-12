var objXMLHT = new XMLHttpRequest();

objXMLHT.addEventListener("load", completo);

objXMLHT.open('GET', 'http://127.0.0.1:5000/listadoMensajes/');

objXMLHT.send();

function completo(evt)
{
    console.log('consuluta completa');
    console.log(this.response);

    var data = JSON.parse(this.response);

    console.log(data)

    var info="<ul>";

    for(var i=0; i < data.length; i++)
    {
        var mensaje = data[i];

        console.log(mensaje.asunto);
        info += "<li>";
        info += "<p>" +  mensaje.asunto + "</p>"; 
        info += "<p>" + mensaje.mensaje + "</p>";
        info += "<p>" + mensaje.usuario + "</p>";
        info += "</li>";

    }

    info += "</ul>";

    document.getElementById("respuesta").innerHTML = info;

}