function new_sentence() {
  axios.get('/app.py').then(res => {
    document.querySelector('#message').innerHTML = res.data;
    document.querySelector('.container').style.display = 'flex';
  }).catch(error => {
    console.log(error.message);
  })
}
