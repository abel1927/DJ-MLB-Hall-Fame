
console.log('Correct')
var defaultPlayerValue=document.querySelector('#-PLAYER-SHOW-BODY1-').innerHTML;

//document.querySelector('#-BUTTON-NEGRO-').addEventListener('click', negroLeague);

document.querySelector('#-BUTTON-BABE-').addEventListener('click', traerBabe);

document.querySelector('#-BUTTON-PLAYER-').addEventListener('click', traerPlayer);




console.log(defaultPlayerValue)

function showSteroidChance(){

    console.log('Dentro de la funcion de traer steroid chance');

    const xhttp =new XMLHttpRequest();

    xhttp.open('GET','../Data/mlb_players.json',true);

    xhttp.send();
    xhttp.onreadystatechange = function(){
        if(this.readyState==4 && this.status==200){
            let steroidChance= Math.random();
            console.log(steroidChance)
            window.alert(steroidChance*100 +"%" );

            }
    }

}

function yearHall(){
    console.log('Dentro de la funcion de traer negro league');

    const xhttp =new XMLHttpRequest();

    xhttp.open('GET','../Data/hof_players.json',true);

    xhttp.send();
    xhttp.onreadystatechange = function(){

        let datos = JSON.parse(this.responseText); 

            console.log('Carge los datos')
            
            let tempYear=document.querySelector('#-HALL-YEAR-INPUT-');
            
            console.log(tempYear.value)

            year=tempYear.value;

            let result=[]

            
            for (item in datos){
                //console.log('Entre al for')
                console.log(datos[item]["HoF year"])
                if(datos[item]["HoF year"]==year){
                    result.push(datos[item]["Name"]);
                    
                }
                //console.log(datos[item]["Name"]);
                //console.log(datos[item]["Hof year"]);
                
            }
            window.alert(result);  
    }
}

function negroLeague(){
    console.log('Dentro de la funcion de traer negro league');

    const xhttp =new XMLHttpRequest();

    xhttp.open('GET','../Data/mlb_players.json',true);

    xhttp.send();
    xhttp.onreadystatechange = function(){
        if(this.readyState==4 && this.status==200){
            let nList=["George Louis Scales","James William Gilliam","Elston Gene Howard","Allen Hurley McNair","Alphonse Eugene Smith","Newton Henry Allen","Albert Dewey Creacy","Branch Lee Russell","Henry Curtis Thompson","Clinton Cyrus Thomas","John Christopher Beckwith","Richard Benjamin Lundy","Walter Moore","Edgar Wooded Wesley","William Bell","Samuel Jones","Donald Newcombe","Barney Brown","Joseph Black","Clifford Bell","William McKinley Cornelius","Philip Cockrell","Nelson Dean","William Force"];
            window.alert(nList);

            }
    }

}

function showActualChance(playerName){

    console.log('Dentro de la funcion de traer actual chance');

    const xhttp =new XMLHttpRequest();

    xhttp.open('GET','../Data/mlb_players.json',true);

    xhttp.send();
    xhttp.onreadystatechange = function(){
        if(this.readyState==4 && this.status==200){
            let actualChance= Math.random();
            console.log(actualChance)
            window.alert(actualChance*100 +"%" );


            
            }
    }

}

function traerActual(){
    console.log('Dentro de la funcion de traer actual 10 years');

    const xhttp =new XMLHttpRequest();

    xhttp.open('GET','../Data/mlb_players.json',true);

    xhttp.send();
    xhttp.onreadystatechange = function(){
        if(this.readyState==4 && this.status==200){

            let datos = JSON.parse(this.responseText); 

            console.log('Carge los datos')
            
            let playerName=document.querySelector('#-PLAYER-NAME-ACTUAL-');
            
            console.log(playerName.value)

            playerName=playerName.value;
            playerId='';

            for(item in datos){
                //console.log(datos[item]["Name"]);
                if (datos[item]["Name"]==playerName)
                {   
                    playerId=item;
                    console.log(parseInt(datos[item]["Last year"]));
                    if(parseInt(datos[item]["Last year"])<2011)
                    {
                        window.alert("Ya pasaron los 10 años de eleccion de ese jugador.");
                        return
                    }
                    console.log("succes");
                    break;
                    
                    
                }
        
                
            }

            if (playerId!=''){
                showActualChance(playerName);
            }
            
            else{
                    window.alert("No existe ese jugador en nuestra base de datos.");
                }
            
            

            }
    }

}


function traerSteroid(){
    console.log('Dentro de la funcion de traer steroid');

    const xhttp =new XMLHttpRequest();

    xhttp.open('GET','../Data/mlb_players.json',true);

    xhttp.send();
    xhttp.onreadystatechange = function(){
        if(this.readyState==4 && this.status==200){

            let datos = JSON.parse(this.responseText); 

            console.log('Carge los datos')
            
            let playerName=document.querySelector('#-PLAYER-NAME-STEROID-');
            
            console.log(playerName.value)

            playerName=playerName.value;
            playerId='';

            for(item in datos){
                //console.log(datos[item]["Name"]);
                if (datos[item]["Name"]==playerName)
                {
                    playerId=item;
                    console.log("succes");
                    break;
                    
                }
            }
            if (playerId!=''){
                console.log("entre al if");

                let playerRes=document.querySelector('#-STEROID-SHOW-BODY1-');
                playerRes.innerHTML='';
            
            if ("G" in datos[playerId]["batter_stats"]){
                let temp_text=`<tr>
            <td>${datos[playerId]["First year"]}</td>
            <td>${datos[playerId]["Last year"]}</td>
            <td>${datos[playerId]["batter_stats"]["G"]["summary"]}</td>
            <td>${datos[playerId]["batter_stats"]["HR"]["summary"]}</td>
            <td>${datos[playerId]["batter_stats"]["BA"]["summary"]}</td>
            <td>${datos[playerId]["batter_stats"]["RBI"]["summary"]}</td>
            <td>${datos[playerId]["batter_stats"]["BB"]["summary"]}</td>
            <td>${datos[playerId]["batter_stats"]["OBP"]["summary"]}</td>
            <td>${datos[playerId]["batter_stats"]["SLG"]["summary"]}</td>
            </tr>`;
                playerRes.innerHTML+=temp_text;
                console.log(  playerRes.innerHTML +"lolol");
            }
            else
            {
                let playerRes=document.querySelector('#-STEROID-SHOW-BODY1-');
                playerRes.innerHTML=defaultPlayerValue;
            } 
        
            
            if ("ERA" in datos[playerId]["pitcher_stats"]){
            temp_text=`<tr>
            <td>${datos[playerId]["First year"]}</td>
            <td>${datos[playerId]["Last year"]}</td>
            <td>${datos[playerId]["pitcher_stats"]["G"]["summary"]}</td>
            <td>${datos[playerId]["pitcher_stats"]["W"]["summary"]}</td>
            <td>${datos[playerId]["pitcher_stats"]["L"]["summary"]}</td>
            <td>${datos[playerId]["pitcher_stats"]["ERA"]["summary"]}</td>
            <td>${datos[playerId]["pitcher_stats"]["IP"]["summary"]}</td>
            <td>${datos[playerId]["pitcher_stats"]["H"]["summary"]}</td>
            <td>${datos[playerId]["pitcher_stats"]["SO"]["summary"]}</td>
            </tr>`;

            let playerResPit=document.querySelector('#-STEROID-SHOW-BODY2-');
            playerResPit.innerHTML=temp_text;
            console.log(  playerRes.innerHTML +"lolol");
            
        }
        else
        {
            let playerRes=document.querySelector('#-PLAYER-SHOW-BODY2-');
            playerRes.innerHTML=defaultPlayerValue;
        } 
            }
            else{
                window.alert("No existe ese jugador en nuestra base de datos de steriodes.");
            }
            

            }
    }

}


function traerPlayer(){
    console.log('Dentro de la funcion de traer player');

    const xhttp =new XMLHttpRequest();

    xhttp.open('GET','../Data/mlb_players.json',true);

    xhttp.send();
    xhttp.onreadystatechange = function(){
        if(this.readyState==4 && this.status==200){

            let datos = JSON.parse(this.responseText); 

            console.log('Carge los datos')
            
            let playerName=document.querySelector('#-PLAYER-NAME-STATIC-');
            
            console.log(playerName.value)

            playerName=playerName.value;
            playerId='';

            for(item in datos){
                //console.log(datos[item]["Name"]);
                if (datos[item]["Name"]==playerName)
                {
                    playerId=item;
                    console.log("succes");
                    break;
                    
                }
            }
            if (playerId!=''){
                console.log("entre al if");

                let playerRes=document.querySelector('#-PLAYER-SHOW-BODY1-');
                playerRes.innerHTML='';
            
            if ("G" in datos[playerId]["batter_stats"]){
                let temp_text=`<tr>
            <td>${datos[playerId]["First year"]}</td>
            <td>${datos[playerId]["Last year"]}</td>
            <td>${datos[playerId]["batter_stats"]["G"]["summary"]}</td>
            <td>${datos[playerId]["batter_stats"]["HR"]["summary"]}</td>
            <td>${datos[playerId]["batter_stats"]["BA"]["summary"]}</td>
            <td>${datos[playerId]["batter_stats"]["RBI"]["summary"]}</td>
            <td>${datos[playerId]["batter_stats"]["BB"]["summary"]}</td>
            <td>${datos[playerId]["batter_stats"]["OBP"]["summary"]}</td>
            <td>${datos[playerId]["batter_stats"]["SLG"]["summary"]}</td>
            </tr>`;
                playerRes.innerHTML+=temp_text;
                console.log(  playerRes.innerHTML +"lolol");
            }
            else
            {
                let playerRes=document.querySelector('#-PLAYER-SHOW-BODY1-');
                playerRes.innerHTML=defaultPlayerValue;
            } 
        
            
            if ("ERA" in datos[playerId]["pitcher_stats"]){
            temp_text=`<tr>
            <td>${datos[playerId]["First year"]}</td>
            <td>${datos[playerId]["Last year"]}</td>
            <td>${datos[playerId]["pitcher_stats"]["G"]["summary"]}</td>
            <td>${datos[playerId]["pitcher_stats"]["W"]["summary"]}</td>
            <td>${datos[playerId]["pitcher_stats"]["L"]["summary"]}</td>
            <td>${datos[playerId]["pitcher_stats"]["ERA"]["summary"]}</td>
            <td>${datos[playerId]["pitcher_stats"]["IP"]["summary"]}</td>
            <td>${datos[playerId]["pitcher_stats"]["H"]["summary"]}</td>
            <td>${datos[playerId]["pitcher_stats"]["SO"]["summary"]}</td>
            </tr>`;

            let playerResPit=document.querySelector('#-PLAYER-SHOW-BODY2-');
            playerResPit.innerHTML=temp_text;
            console.log(  playerRes.innerHTML +"lolol");
            
        }
        else
        {
            let playerRes=document.querySelector('#-PLAYER-SHOW-BODY2-');
            playerRes.innerHTML=defaultPlayerValue;
        } 
            }
            else{
                window.alert("No existe ese jugador en nuestra base de datos.");
            }
            

            }
    }

}

function traerBabe(){
    console.log('Dentro de la funcion de Babe');

    const xhttp =new XMLHttpRequest();

    xhttp.open('GET','../Data/mlb_players.json',true);

    xhttp.send();

    xhttp.onreadystatechange = function(){
        if(this.readyState==4 && this.status==200){

            let datos = JSON.parse(this.responseText); 

            console.log('Carge los datos')
            

            let babeRes=document.querySelector('#-BABE-SHOW-BODY1-');
                babeRes.innerHTML='';

            let temp_text=`<tr>
            <td>${datos["Babe_Ruth_17764"]["First year"]}</td>
            <td>${datos["Babe_Ruth_17764"]["Last year"]}</td>
            <td>${datos["Babe_Ruth_17764"]["batter_stats"]["G"]["summary"]}</td>
            <td>${datos["Babe_Ruth_17764"]["batter_stats"]["HR"]["summary"]}</td>
            <td>${datos["Babe_Ruth_17764"]["batter_stats"]["BA"]["summary"]}</td>
            <td>${datos["Babe_Ruth_17764"]["batter_stats"]["RBI"]["summary"]}</td>
            <td>${datos["Babe_Ruth_17764"]["batter_stats"]["BB"]["summary"]}</td>
            <td>${datos["Babe_Ruth_17764"]["batter_stats"]["OBP"]["summary"]}</td>
            <td>${datos["Babe_Ruth_17764"]["batter_stats"]["SLG"]["summary"]}</td>
            </tr>`;
                babeRes.innerHTML+=temp_text;
                console.log(  datos["Babe_Ruth_17764"]["First year"]);
                console.log(  datos["Babe_Ruth_17764"]["Last year"]);
                console.log(  babeRes.innerHTML +"lolol");

            temp_text=`<tr>
            <td>${datos["Babe_Ruth_17764"]["First year"]}</td>
            <td>${datos["Babe_Ruth_17764"]["Last year"]}</td>
            <td>${datos["Babe_Ruth_17764"]["pitcher_stats"]["G"]["summary"]}</td>
            <td>${datos["Babe_Ruth_17764"]["pitcher_stats"]["W"]["summary"]}</td>
            <td>${datos["Babe_Ruth_17764"]["pitcher_stats"]["L"]["summary"]}</td>
            <td>${datos["Babe_Ruth_17764"]["pitcher_stats"]["ERA"]["summary"]}</td>
            <td>${datos["Babe_Ruth_17764"]["pitcher_stats"]["IP"]["summary"]}</td>
            <td>${datos["Babe_Ruth_17764"]["pitcher_stats"]["H"]["summary"]}</td>
            <td>${datos["Babe_Ruth_17764"]["pitcher_stats"]["SO"]["summary"]}</td>
            </tr>`;

            let babeResPit=document.querySelector('#-BABE-SHOW-BODY2-');
            babeResPit.innerHTML=temp_text;

            }
    }
}

