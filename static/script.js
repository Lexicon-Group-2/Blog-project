
// just a shorter way of getting elements by class name
// too lazy to type that long command each time.
function getByClass(className) {
  return document.getElementsByClassName(className)
}


var form = getByClass("comment-form")[0],
    btn  = getByClass("show-hide-comment-form")[0]


function showHideForm() {
  if (form.style.display === 'none') {
    form.style.display = "flex"
    btn.innerHTML = 'Hide form'
  } else {
    form.style.display = "none";
    btn.innerHTML = 'Comment this post'
  }
}


function hideForm() {
  form.style.display = "none"
  btn.innerHTML = 'Comment this post'
}

