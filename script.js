window.addEventListener('load',() => {

})

const fetchData = async () => {
    const access_token = "IGQVJXaDdlODF1cUJXVF9nakJ0cGx3aDB3WVV5OTJOLVZAMUmlpcnRBcW1NZA0YtM1FyLVN1NzZAHd21fSGJqSzhkUnAwcVpSd1d4ZA3dqYUI2LVpjQ2pYZAThHSHprWlFoUVRwMWZABNEVR";
    const fields = 'id,caption,media_type,media_url,permalink'
    const url = `https://graph.instagram.com/me/media?access_token=${access_token}&fields=${fields}`

    const response = await fetch(url)
    const data = await response.jason()
    let content = '<div class"portafolio">'
    for(let item of data.data) {
        const mediaType = item.media_type
        if(mediaType === 'IMAGE'){
            content += `<div class="col-md-6"
                <a href="${item.permalink}">
                <img src="${item.media_url}" class="img-fluid alt="...">
                </a>
            </div>`
        }
    }
    content += '</div>'
    const contenedor_ig = document.getElementById('contenedor_ig')
    contenedor_ig.innerHTML = content
}
fetchData()