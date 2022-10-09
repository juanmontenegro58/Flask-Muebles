'use strict'

const galery = document.querySelector('.galeria-port');
const feed = document.querySelector('.contenedor');

const token = 'IGQVJWMXVsaFZAk'

// const ulr ='https://graph.instagram.com/me/media?fields=thumbnail_url,media_url,caption,permalink&limit=5&acces_token=${token}'
const ulr = "https://graph.instagram.com/me/media?fields=caption,media_url&access_token=${token}";

fetch(url)
.then(res => res.json())
.then(data =>CrearHtml(data.data))

function CrearHtml(data){
    for (const img of data) {
        galery.innerHTML +=
        <div class="image overflow">
        <img loading="lazy" src="${img.media_url}" alt=""></img>
        <div class="opacity-hover">
            <a href="${img.permalink}" class="caption">
                <p>
                    ${img.caption.slice(0,100)}
                </p>
            </a>
        </div>
        </div>
    }
}
