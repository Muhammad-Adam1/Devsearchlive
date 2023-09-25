// Invoke Functions Call on Document Loaded
document.addEventListener('DOMContentLoaded', function () {
  hljs.highlightAll();
});

// let alertWrapper = document.querySelector('.alert')
// let alertClose = document.querySelector('.alert__close')

// if (alertWrapper){
//   alertClose.addEventListener('click', () =>
//     alertWrapper.style.display = 'none'
//   )
// }

let alertWrappers = document.querySelectorAll('.alert'); // Use querySelectorAll to select all alert elements
let alertCloses = document.querySelectorAll('.alert__close'); // Select all close buttons

// Loop through all alert elements and attach click event listeners
alertCloses.forEach((alertClose, index) => {
  alertClose.addEventListener('click', () => {
    alertWrappers[index].style.display = 'none';
  });
});