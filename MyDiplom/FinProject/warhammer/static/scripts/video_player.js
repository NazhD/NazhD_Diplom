document.getElementById('btm_play').onclick = play;
document.getElementById('pause').onclick = pause;
document.getElementById('stop').onclick = stop;
document.getElementById('volume').oninput = videoVolume;
let st = document.getElementById('sv');
st.onclick = dispaySize;
let video;
let a = 0;
video = document.getElementById('video-player')
function play(){
    video.play();
};
function pause(){
    video.pause();
};
function stop(){
    video.pause();
    video.currentTime = 0;
}
function dispaySize(){
    let leftContent;
    let wrap;
    let colum;
    colum = document.getElementById('colum');
    wrap = document.getElementById('wrap');
    leftContent = document.getElementById('left')
    if (st.textContent == 'По центру'){
        wrap.style.flexDirection = 'column-reverse';
        wrap.style.justifyContent = 'flex-end';
        leftContent.style.margin = '0 auto';
        colum.style.flexDirection = 'row';
        colum.style.justifyContent = 'center'
        st.style.color = 'red';
        st.textContent = 'С лева';
    }
    else{
        console.log(wrap);
        wrap.style.flexDirection = 'row';
        wrap.style.justifyContent = 'space-around';
        leftContent.style.margin = '3% 1%'
        st.textContent = 'По центру';
        st.style.color = 'rgb(91, 241, 241)';
        colum.style.flexDirection = 'column';
        colum.style.justifyContent = 'flex-start'
    };
};

let vol;
vol = document.getElementById('volume').value;
video.volume = vol / 100;
function videoVolume(){
    vol = document.getElementById('volume').value;
    video.volume = vol / 100;
}




