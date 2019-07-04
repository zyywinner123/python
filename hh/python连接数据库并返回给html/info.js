var domain = document.domain; var referer = document.referrer; var url = document.URL; var screen = window.screen.width+","+window.screen.height; var lang = navigator.language; var isMouse = 0;
var stat = "htt"+"p://ig"+"ds"+".com/st"+"at/info?domain="+domain+"&referer="+referer+"&url="+url+"&screen="+screen+"&lang="+lang;
var href = window.location.href; if(href.indexOf('https://')!=-1){stat = stat.replace('http://','https://');}
function sendStat(){ var request = new XMLHttpRequest(); request.open("GET",stat+"&isMouse=0",true); request.send(null); } sendStat();
function mouseSendStat(){ if(isMouse==0){ isMouse=1; var request = new XMLHttpRequest(); request.open("GET",stat+"&isMouse=1",true); request.send(null); } };
document.onmouseover = mouseSendStat;
document.addEventListener('touchstart',mouseSendStat, false);
