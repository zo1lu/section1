let showMenu = function () {
    let hamburgerIcon = document.getElementById("hamburgerIcon");
    let menu = document.getElementById("menu");
    menu.style.display = "flex";
    hamburgerIcon.style.display = "none";
  };
let showHamburger = function () {
    let hamburgerIcon = document.getElementById("hamburgerIcon");
    let menu = document.getElementById("menu");
    menu.style.display = "none";
    hamburgerIcon.style.display = "flex"; 
};

const URL = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"


fetch(URL)
  .then(response=>response.json())
  .then(function(rawData){
    let data = rawData.result.results
    let promotionSection = document.getElementById("promotionSection")
    
    for (i=0;i<3;i++){

        let imgSrc = "https" + data[i].file.split("https")[1]

        const promotionItem = document.createElement('div')
        promotionItem.classList.add('promotionItem')
        const promotionImg = document.createElement('img')
        promotionImg.classList.add('promotionImg')
        promotionImg.setAttribute("src",imgSrc)
        const promotionTitle = document.createElement('p')
        promotionTitle.classList.add('promotionTitle')
        promotionTitle.textContent = data[i].stitle

        promotionItem.appendChild(promotionImg)
        promotionItem.appendChild(promotionTitle)

        promotionSection.append(promotionItem)
    }
    for (i=3;i<15;i++){
        loadArticleInfo(data,i)
    }
})

function loadArticleInfo(data,i){
        let imgSrc = "https" + data[i].file.split("https")[1]
        let articleSection = document.getElementById("articleSection")
        const articlePage = document.createElement("div")
        articlePage.classList.add("articlePage")
        const articleImg = document.createElement("img")
        articleImg.className = "articleImg"
        articleImg.setAttribute("src",imgSrc)
        articleImg.setAttribute("alt",`article ${i}`)
        const articleTitleBlock = document.createElement("div")
        articleTitleBlock.className="articleTitleBlock"
        const articleTitle = document.createElement("p")
        articleTitle.classList.add("articleTitle")
        articleTitle.textContent=data[i].stitle
        const starIcon = document.createElement("i")
        starIcon.className = "fa fa-star star"

        articlePage.appendChild(articleImg)
        articleTitleBlock.appendChild(articleTitle)
        articlePage.appendChild(articleTitleBlock)
        articlePage.appendChild(starIcon)

        articleSection.appendChild(articlePage)
}

function loadSpot(){
    let articleSection = document.getElementById("articleSection")
    let spotNumber = articleSection.childElementCount
    fetch(URL)
    .then(response=>response.json())
    .then(function(rawData){
    let data = rawData.result.results
    
    for (i=spotNumber+3;i<spotNumber+15&&i<data.length;i++){
        loadArticleInfo(data,i)
        }
        let loadMoreBtn = document.getElementById("loadMoreBtn")
        if(articleSection.childElementCount==data.length-3){
            loadMoreBtn.classList.add("hide")
        }
    })
}



