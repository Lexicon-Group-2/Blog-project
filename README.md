# ToDo List

### **index.html**

- [ ] Add some content to the index page.
- [ ] Apply some css.

### **navbar**

- [x] Change link 'admin/' to be visible only to the users with **superuser** credentials.

### **blog.html**

- [ ] Untill now the only way to make a blog post is to do it within django admin/ gui. Change it so that say users within staff group can make a blog post.
- [x] Group some users into a staff group.
- [x] Apply some css to the blog. Either use display: flex or display: grid... both should work fine.
- [x] Make a clear separation between blogs. For instance, each blog should be within certain background color, separated from the body bacground.
- [ ] Perhaps for this page create a fixed side menu (as Sara did for our previous project) which will contain all the titles for the posts. A good option would be to add a **overflow-y: auto** (it will create a scroll only when needed) and also **overflow-x: hidden**.

### **post_detail.html:**

- [ ] Whole this page needs a lot of css.
- [x] Add css to the comments. Each comment should have their own field (div with some background). Nicelly visualise username and date_added fields with comment field bellow. Perhaps check some of the bootstrap comment boxes.
- [x] So far anybody with an email can make a comment. Change it so that only registered users can comment a post.
- [x] Make a button and add an eventListener with JS to show the form in which user can make a comment. By default the form should be hidden.
- [x] Make a custom comment form instead of this django default thing. Similar as we did for the login page.

### **login.html**

- [x] Apply some css to the login form.
- [x] Perhaps position the login form in the center of the screen (horizontally) with some margin-top to give a space between the form and the navbar. Another option is to use display: flex with additional options justify-content and align, to align center everything inside a div container.

### **registration.html**

- [x] Apply some css to this page as well.
- [x] display: grid should work nice with grid template for columns set to 2 columns.

### **user.html**

- [x] This is the personal page for each user.

- [x] In this page show each post and comment that a logged-in user has made.
- [ ] Add a functionality to update or delete the comment. To be honest, have no idea how to do it, but will figure it out. Perhaps a good start would be [here](https://www.geeksforgeeks.org/django-crud-create-retrieve-update-delete-function-based-views/).

### **models.py**

- [ ] slug should be equal to some random string of letters with certain length. This is because person can't guess it and thus read the post even it they are not logged in.
- [ ] Write a function which will generate random string of letter.
