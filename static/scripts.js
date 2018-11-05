function new_sentence() {
  axios.get('/new_sentence').then(res => {
    document.querySelector('#message').innerHTML = res.data
  })
}
