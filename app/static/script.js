const fetchData = async () => {
    const access_token = 'IGQVJWTHg3anRtOG5rMVZAfbGYzM25yeUw1YXdaby1qbDRnZAERibDlCcUhPMDVRdTAxa3FGWTZAyR01ORnBLLVZAEQ1I3aTBNaEUtWUhxY01Ed3l4bU5qRHVhd0dZAdmI3MzN3NkdZAQ0JR';
    const fields = 'id,caption,media_type,media_url,permalink'
    const url = `https://graph.instagram.com/me/media?access_token=${access_token}&fields=${fields}`

    const response = await fetch(url)
    const data = await response.json()
    let content = ''
    for(let item of data.data) {
        const mediaType = item.media_type
        if(mediaType === 'IMAGE'){
            content += `<div class="column">
                <a href="${item.permalink}" target="_blank">
                <img src="${item.media_url}" class="dimensiones_ig image" alt="...">
                </a>
            </div>`
        }
    }
    content += ''
    const galeria_port = document.getElementById('galeria_port')
    galeria_port.innerHTML = content
}
fetchData()