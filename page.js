
const u1x=document.getElementById("u1x");
const journee=document.getElementById("journee");



var joueurs = document.getElementsByClassName('joueur');

function setCheckboxes(){
    
    for(j of joueurs){
        var qui==j.id;
        var etat=data=getUserState(u1X,journee,qui)
        var cbpr=document.getElementById(qui+"pr").value;
        var cbab=document.getElementById(qui+"ab").value;
        if(etat=="pr"){
            cbpr.checked=true;
            cbpr.checked=false;
        }
        else if(etat=="ab"){
            cbpr.checked=false;
            cbpr.checked=true;
        }
        else{
        
            cbpr.checked=false;
            cbpr.checked=false;
        }
    }   
}

function onChangeBox(idb){
    var qui = idb[:-2];
    var etatc1 = document.getElementById(qui+"pr").checked;
    var etatc2 = document.getElementById(qui+"ab").checked;
    var etat="??";
    if(etatc1 && !etatc2) etat="pr";
    else if(!etatc1 && etatc2) etat="ab";
    var msg="houdsdeb"+u1x+"\t"+journee+"\t"+qui+etat;
    
    var res = httpGet("https://olki.loria.fr/python4nlp.php?"+msg);
    console.log("message : "+msg);
}


setCheckboxes();


