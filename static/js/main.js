
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
