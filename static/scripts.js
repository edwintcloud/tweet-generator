function new_sentence() {
  axios.get('/new_sentence').then(res => {
    document.querySelector('.sentence').innerHTML = res.data
  })
}
