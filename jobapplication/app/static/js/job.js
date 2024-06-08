function addrowdata(){
    console.log("++++++++++++")
   
    let numb = document.getElementById("education").children.length;
    if (numb<4){
        let edutable=document.getElementsByClassName("eduaction")[0];
        let eduadd=document.getElementsByClassName("edu")[0];
        let column=eduadd.cloneNode(true);
        edutable.appendChild(column);
    }
}
function removerow(){
    let edutable=document.getElementsByClassName("eduaction")[0];
    let eduremove=document.getElementsByClassName("edu").length;
    if(eduremove>1){
        edutable.removeChild(edutable.lastElementChild)
    }
}

function addrowdatawork(){
    let workdatatable=document.getElementsByClassName("worktable")[0];
    let workadd=document.getElementsByClassName("work")[0];
    let column=workadd.cloneNode(true);
    workdatatable.appendChild(column);
}
function removerowwork(){
    let workdatatable=document.getElementsByClassName("worktable")[0];
    let workremove=document.getElementsByClassName("work").length;
    if(workremove>1){
        workdatatable.removeChild(workdatatable.lastElementChild)
    }
}


function addrowdatareference(){
    let referencedatatable=document.getElementsByClassName("referencetable")[0];
    let referenceadd=document.getElementsByClassName("reference")[0];
    let column=referenceadd.cloneNode(true);
    referencedatatable.appendChild(column);
}
function removerowreference(){
    let referencedatatable=document.getElementsByClassName("referencetable")[0];
    let referenceremove=document.getElementsByClassName("reference").length;
    if(referenceremove>1){
        referencedatatable.removeChild(referencedatatable.lastElementChild)
    }
}

count=0
function next(){
    count++
    console.log(count,"++")
    
    switch (count) {

        case 1:

            document.getElementById('basicdetatilsdiv').setAttribute("style","display:none")
            document.getElementById('edudetailsdiv').removeAttribute("style","display")
            document.getElementById('pre').disabled=false
            break;

        case 2:

    
        
            console.log("else part")
            document.getElementById('edudetailsdiv').setAttribute("style","display:none")
            document.getElementById('workdwtailsdiv').removeAttribute("style","display")
            break;
        


        case 3:
     
    
        document.getElementById('workdwtailsdiv').setAttribute("style","display:none")
        document.getElementById('langdetailsdiv').removeAttribute("style","display")
        break;

        case 4:
        
    
        document.getElementById('langdetailsdiv').setAttribute("style","display:none")
        document.getElementById('techdetailsdiv').removeAttribute("style","display")
        break;

        case 5:
        document.getElementById('techdetailsdiv').setAttribute("style","display:none")
        document.getElementById('referencediv').removeAttribute("style","display")
        break;

        case 6:
        document.getElementById('referencediv').setAttribute("style","display:none")
        document.getElementById('preferencediv').removeAttribute("style","display")
        document.getElementById('nex').disabled=true
        document.getElementById('submit').hidden=false

        break;
    }
        
        
}
function previous(){
   
    count--
    console.log(count,"--")
    switch (count) {

        case 0:
            document.getElementById('edudetailsdiv').setAttribute("style","display:none")
            document.getElementById('basicdetatilsdiv').removeAttribute("style","display")
            document.getElementById('pre').disabled=true

            break;

        case 1:
        document.getElementById('workdwtailsdiv').setAttribute("style","display:none")
        document.getElementById('edudetailsdiv').removeAttribute("style","display")
        break;

        case 2:
        document.getElementById('langdetailsdiv').setAttribute("style","display:none")
        document.getElementById('workdwtailsdiv').removeAttribute("style","display")
        break;

        case 3:
        document.getElementById('techdetailsdiv').setAttribute("style","display:none")
        document.getElementById('langdetailsdiv').removeAttribute("style","display")
        break;

        case 4:
        document.getElementById('referencediv').setAttribute("style","display:none")
        document.getElementById('techdetailsdiv').removeAttribute("style","display")
        document.getElementById('sub').hidden

        break;

        case 5:
        document.getElementById('preferencediv').setAttribute("style","display:none")
        document.getElementById('referencediv').removeAttribute("style","display")
        document.getElementById('nex').disabled=false
        document.getElementById('submit').hidden=true


        break;
        }}
        
