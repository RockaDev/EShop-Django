
while(true){
    if(document.cookie.indexOf('device=') == 0) {
        setTimeout(function(){
            window.location.href = '/';
        }, 2500);
        break;
    }
}