let url_google = 'https://www.google.tw'
let url_taipei_city = 'https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json'

fetch(url_google)
    .then(res=>console.log(res))

fetch(url_taipei_city)
    .then(res=>{
        let data = res.json()
        console.log(data)
        return data
    })
    .then(data=>{
        let result = data.result.results
        console.log(result)
    })
    .catch(e=>console.log(e))
