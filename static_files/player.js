// Initialise
var albumCover = document.getElementById('album-cover');
var mediaButtons = document.getElementById('media-buttons');
mediaButtons.style.display = 'none';

// Add listener for media buttons
albumCover.addEventListener('click', function() {
    mediaButtons.style.display = 'flex';
    setTimeout(function() {
        mediaButtons.classList.add('show'); 
    }, 0);

    setTimeout(function() {
        mediaButtons.classList.remove('show');
        mediaButtons.style.display = 'none';
    }, 3000);
});

// Update track information continuously
async function continuousCheck(){
    let waitTime = 3000;
    while (true) {
        await getResponse()
        .then(async (response) => {
            if (response.status == 200) {
                waitTime = 3000;
                data = await response.json();
                await updateContent(data);
            } else if (response.status == 204) {
                const noTrack = {
                    track_title: "No Track",
                    artist: "No Artist",
                    album_cover: "/static_files/no_track.svg",
                    progress_ms: 0,
                    duration: 100
                }
                updateContent(noTrack)
                waitTime = 6000;
            }
        })
        await new Promise(resolve => setTimeout(resolve, waitTime)); // Delays for 2 seconds
    }
};
async function getResponse() {
    const response = await fetch("/track-info");
    console.log(response);
    return response;
}
continuousCheck();

function updateContent(trackInfo) {
    document.title = trackInfo.track_title + ' • ' + trackInfo.artist;
    document.getElementById('album-cover').src = trackInfo.album_cover;
    background = document.getElementById('background').style.backgroundImage = "url('" + trackInfo.album_cover + "')";
    document.getElementById('artist-name').innerHTML = trackInfo.artist;
    document.getElementById('track-title').innerHTML = trackInfo.track_title;
    progress = document.getElementById('progress-bar');
    const progress_ratio = parseFloat(trackInfo.progress_ms / trackInfo.duration_ms);
    progress.style.transform = "scaleX(" + progress_ratio + ")";
}
