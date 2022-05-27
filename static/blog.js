var form = document.getElementsByClassName("comment-form")[0],
    btn  = document.getElementsByClassName("show-hide-comment-form")[0]

function showHideForm() {
  if (form.style.display === 'none') {
    form.style.display = "flex"
    btn.innerHTML = 'Hide form'
  } else {
    form.style.display = "none";
    btn.innerHTML = 'Write a post?'
  }
}

var submitBtn = document.getElementsByClassName('submit-comment')[0],
    comment   = document.getElementById('post-comment')

function hideForm() {
  form.style.display = "none"
  btn.innerHTML = 'Write a post?'
}

