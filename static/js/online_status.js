const online_status=new WebSocket(
    'ws://'
    + window.location.host
    + '/ws/'
    +'online/'
)

online_status.onopen=function(e){
    console.log('CONNECTED TO ONLINE CONSUMER')

}

online_status.onclose=function(e){
    console.log('DISCONNECTED FROM ONLINE CONSUMER')
}