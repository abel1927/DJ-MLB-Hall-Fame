
console.log('Correct')



//var jsonData= require('../Data/mlb_players.json'); 


document.querySelector('#-BUTTON-BABE-').addEventListener('click', traerBabe)

function traerBabe(){
    console.log('Dentro de la funcion de Babe');

    const xhttp =new XMLHttpRequest();

    xhttp.open('GET','../Data/mlb_players.json',true);

    xhttp.send();

    xhttp.onreadystatechange = function(){
        if(this.readyState==4 && this.status==200){

            //console.log(this.responseText);  


            let datos = JSON.parse(this.responseText); 
            //console.log(datos);

            console.log('Carge los datos')
            let babeRes=document.querySelector('#-BABE-SHOW-');
                babeRes.innerHTML='';
            
            //let i =0;
            //for(let item in datos){
            //console.log(item);
            //console.log(datos);    

            let temp_text=`<tr>
            <td>${datos["Babe_Ruth_17764"]["First year"]}</td>
            <td>${datos["Babe_Ruth_17764"]["Last year"]}</td>
            </tr>`;
                babeRes.innerHTML+=temp_text;
                console.log(  datos["Babe_Ruth_17764"]["First year"]);
                console.log(  datos["Babe_Ruth_17764"]["Last year"]);
                console.log(  babeRes.innerHTML +"lolol");

            
                //document.getElementById("-BABE-SHOW-").innerHTML=`
                //<tr>
                //<td>${datos["Babe_Ruth_17764"]["First year"]}</td>
                //<td>${datos["Babe_Ruth_17764"]["Last year"]}</td>
                //</tr`
            //break;
            
            
            
            
        //} 
            
            ////babeRes.innerHTML='';
//
//
            //
            //<tr>
            //<td>${datos["Babe_Ruth_17764"]["First year"]}</td>
            //<td>${datos["Babe_Ruth_17764"]["First year"]}</td>
            //</tr>
            //`
            //console.log(datos["Babe_Ruth_17764"]) 
            }
    }
}

//function csv_To_Array(str, delimiter = ",") {
//  const header_cols = str.slice(0, str.indexOf("\n")).split(delimiter);
//  const row_data = str.slice(str.indexOf("\n") + 1).split("\n");
//  const arr = row_data.map(function (row) {
//    const values = row.split(delimiter);
//    const el = header_cols.reduce(function (object, header, index) {
//      object[header] = values[index];
//      return object;
//    }, {});
//    return el;
//  });
//
//  // return the array
//  return arr;
//}
