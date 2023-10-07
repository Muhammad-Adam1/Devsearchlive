
// get the search form
    let searchForm = document.getElementById('searchForm')
    let pageLinks = document.getElementsByClassName('page-link')

    if(searchForm){
        for(let i = 0; pageLinks.length > i; i++){
            pageLinks[i].addEventListener('click', function(e) {
                e.preventDefault()
                
                // get the page number from the data attribute
                let page = this.dataset.page

                // set the hidden input value to the page number
                // we are doing thsi so that our search_query works combinely with the pagination 
                searchForm.innerHTML += `<input value=${page} name="page" hidden/>`

                // submit the form
                searchForm.submit()

            })
        }
    }

    // get the project tags and send them in backend to del them 
    let tags = document.getElementsByClassName('project-tag');
    for(let i = 0; tags.length > i; i++){
        tags[i].addEventListener('click', (e) => {
            let tagId = e.target.dataset.tag;
            let projectId = e.target.dataset.project;
            console.log("TAG ID : ", tagId);
            console.log("Project ID : ", projectId);
            
            fetch(`http://localhost:8000/api/remove-tag/`, {
                method: 'DELETE',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({'project':projectId, 'tag':tagId})
            })
            .then(response => response.json())
            .then(data => {
                e.target.remove();
            })
            /*.catch((error) => {
                console.error('Error:', error);
            }); */
        });  
    }