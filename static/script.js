
// just a shorter way of getting elements by class name
// too lazy to type that long command each time.
function getByClass(className) {
  return document.getElementsByClassName(className)
}

function getById(Id) {
  return document.getElementById(Id)
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

var submittBtn = getByClass('submit-comment')[0],
    comment    = getById('post-comment')
    

submittBtn.disabled = true

comment.addEventListener( 'change', () => {
  len = comment.value.length
  console.log(len)

  if (len < 20) {
    submittBtn.disabled = true
  } else {
    submittBtn.disabled = false
  }


})





function hideForm() {
  
  console.log(comment)

  form.style.display = "none"
  btn.innerHTML = 'Comment this post'
}

