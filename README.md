# ToDo List

### **index.html**

- [ ] Add some content to the index page.
- [ ] Apply some css.

### **navbar**

- [ ] Change link 'admin/' to be visible only to the users with **superuser** credentials.

### **blog.html**

- [ ] Untill now the only way to make a blog post is to do it within django admin/ gui. Change it so that say users within staff group can make a blog post.
- [ ] Group some users into a staff group.
- [ ] Apply some css to the blog. Either use display: flex or display: grid... both should work fine.
- [ ] Make a clear separation between blogs. For instance, each blog should be within certain background color, separated from the body bacground.
- [ ] Perhaps for this page create a fixed side menu (as Sara did for our previous project) which will contain all the titles for the posts. A good option would be to add a **overflow-y: auto** (it will create a scroll only when needed) and also **overflow-x: hidden**.

### **detail_view.html:**

- [ ] Whole this page needs a lot of css.
- [ ] So far anibody with an email can make a comment. Change it so that only registered users can comment a post.
- [ ] Make a button and add an eventListener with JS to show the form in which user can make a comment. By default the form should be hidden.
- [ ] Make a custom comment page instead of this django default thing. Similar as we did for the login page.

### **login.html**

- [ ] Apply some css to the login form.
- [ ] Perhaps center the login form to he showed in the center of the screen (horizontally) with some margin-top to give a space between the form and the navbar.

### **registration.html**

- [ ] Apply some css to this page as well.
- [ ] display: grid should work nice with grid template for columns set to 2 columns.

### **user.html**

- [ ] This is the personal page for each user.

- [ ] In this page show each comment that a logged in user has made.
- [ ] Add a functionality to update or delete the comment. To be honest, have no idea how to do it, but will figure it out. Perhaps a good start would be [here](https://www.geeksforgeeks.org/django-crud-create-retrieve-update-delete-function-based-views/).

### **models.py**

- [ ] slug should be equal to some random string of letters with certain length. This is because person can't guess it and thus read the post even it they are not logged in.
- [ ] Write a function which will generate random string of letter.
