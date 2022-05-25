
// just a shorter way of getting elements by class name
// too lazy to type that long command each time.
function getByClass(className) {
  return document.getElementsByClassName(className)
}

function getById(Id) {
  return document.getElementById(Id)
}

// get variables for the form and show button
var form = getByClass("comment-form")[0],
    btn  = getByClass("show-hide-comment-form")[0]

// a function which will show/hide comment form
function showHideForm() {
  if (form.style.display === 'none') {
    form.style.display = "flex"
    btn.innerHTML = 'Hide form'
  } else {
    form.style.display = "none";
    btn.innerHTML = 'Comment this post'
  }
}

// get variables for the submit button and comment field
var submitBtn = getByClass('submit-comment')[0],
    comment   = getById('post-comment')
    
// Set a button to be disabled by default
submitBtn.disabled = true

// add an event Listener for the change of the input field
comment.addEventListener('change', () => {
  len = comment.value.length
  if (len < 20) {
    submitBtn.disabled = true
  } else {
    submitBtn.disabled = false
  }
})


// a function which will hide the comment input form on submit
function hideForm() {
  form.style.display = "none"
  btn.innerHTML = 'Comment this post'
}

