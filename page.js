
const u1x=document.getElementById("u1x");
const journee=document.getElementById("journee");



var joueurs = document.getElementsByClassName('joueur');

function setCheckboxes(){
    
    for(j of joueurs){
        var qui==j.id;
        var etat=data=getUserState(u1X,journee,qui)
        var cbpr=document.getElementById(qui+"pr");
        var cbab=document.getElementById(qui+"ab");
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





