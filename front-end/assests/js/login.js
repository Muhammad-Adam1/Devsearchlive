let form = document.getElementById('login-form');

form.addEventListener('submit', (e) => {
    e.preventDefault()
    // let formData = new FormData(form)
    let formData = {
        'username' : form.username.value,
        'password' : form.password.value
    }
    fetch('http://localhost:8000/api/users/token/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData)
        
    })
    .then(response => response.json())
    .then(data => {
        console.log('DATA :', data.access)
        if(data.access){
            localStorage.setItem('token', data.access)
            window.location = 'file:///C:/Users/Ahmed/Desktop/Social%20media%20web/front-end/project-list.html'
        }
        else{
            alert('username or passeord did not work')
        }
    })
})