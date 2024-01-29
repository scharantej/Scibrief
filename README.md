## Flask Application Design for a Personal Blog

### HTML Files

- `index.html`:

 - This is the homepage of the blog and provides an overview of the research paper summaries.
 - It includes an introduction to the blog, a list of recent summaries, and links to other pages on the site, such as the About page and Contact page.


- `summary.html`:

 - This template is used to display individual research paper summaries.
 - It includes the title of the paper, authors, abstract, and any additional information you want to share about the research.
 

- `about.html`:

 - This page provides information about the blog owner, their interests, and their background in research.
 - It helps readers connect with the author and understand the purpose of the blog.


- `contact.html`:

 - This page contains contact information for the blog owner.
 - It might include an email address, social media links, or a contact form for readers to reach out with comments, questions, or suggestions.

### Routes

- `/`:

 - This route handles requests to the homepage of the blog.
 - It returns the `index.html` template, displaying the overview of the research paper summaries.


- `/summary/<id>`:

 - This route handles requests to view an individual research paper summary.
 - It fetches the summary from the database using the provided `<id>` and returns the `summary.html` template, displaying the summary details.


- `/about/`:

 - This route handles requests to the About page of the blog.
 - It returns the `about.html` template, providing information about the blog owner.


- `/contact/`:

 - This route handles requests to the Contact page of the blog.
 - It returns the `contact.html` template, displaying the contact information of the blog owner.


- `/add-summary/`:

 - This route handles requests to add a new research paper summary to the blog.
 - It renders a form that allows the user to enter the title, authors, abstract, and any additional information about the research.
 - Upon form submission, it saves the summary to the database and redirects the user to the homepage.


- `/edit-summary/<id>`:

 - This route handles requests to edit an existing research paper summary.
 - It fetches the summary from the database using the provided `<id>`, renders a form pre-populated with the existing summary details, and allows the user to make changes.
 - Upon form submission, it updates the summary in the database and redirects the user to the homepage.


- `/delete-summary/<id>`:

 - This route handles requests to delete a research paper summary from the blog.
 - It fetches the summary from the database using the provided `<id>`, confirms the deletion with the user, and if confirmed, deletes the summary from the database and redirects the user to the homepage.