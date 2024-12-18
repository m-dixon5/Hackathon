# Testing

This is the TESTING file for the [StageScore](https://) website.

Return back to the [README.md](README.md) file.

## Testing Contents  
  
- [Testing](#testing)
  - [Testing Contents](#testing-contents)
  - [Validation](#validation)
    - [HTML Validation](#html-validation)
    - [JavaScript Validation](#javascript-validation)
    - [Python Validation](#python-validation)
    - [CSS Validation](#css-validation)
    - [Lighthouse Scores](#lighthouse-scores)
    - [Wave Accessibility Evaluation](#wave-accessibility-evaluation)
  - [Manual Testing](#manual-testing)
    - [Browser Compatibility](#browser-compatibility)
    - [Testing User Stories](#testing-user-stories)
    - [Dev Tools/Real World Device Testing](#dev-toolsreal-world-device-testing)
  - [Bugs](#bugs)

## Validation

### HTML Validation

For our HTML files we have used [HTML W3C Validator](https://validator.w3.org) to validate all of our HTML files.

I have had to follow a different approach for validating my HTML for this project as the majority of my pages are developed using Jinja syntax such as '{% extends "base.html" %}' and '{{ form|crispy }}' and most require user authentication. The HTML validator will throw errors if we use the website's URL, so we have had to follow the below approach for every page:

- Via the deployed Heroku app link, I have navigated to each individual page.
- Right clicking on the screen/CTRL+U/⌘+U on Mac, allows a menu to appear, giving me the option to 'View page source'.
- The complete HTML code for the deployed page will appear, allowing you to select the entire code using CTRL+A/⌘+A on Mac.
- Paste the copied code into the [validate by input](https://validator.w3.org/#validate_by_input) option.
- Check for errors and warnings, fix any issues, revalidate by following the above steps and record the results.

![html validation]()

All HTML pages were validated and received a 'xxxxxxxxx' result, as shown above.

| HTML Source Code/Page | Errors | Warnings |
| ---- | ------ | -------- | 
| Home | 0 | 0 |
| Sign In | 0 | 0 |
| Sign Up | 0 | 0 |
| Review | 0 | 0 |
| Add Review | 0 | 0 |
| Review_detail | 0 | 0 |
| Edit Review | 0 | 0 |
| Delete Review | 0 | 0 |
| Delete Comment | 0 | 0 |


| Error 403 | 0 | 0 |
| Error 404 | 0 | 0 |
| Error 500 | 0  | 0 |
  
<hr>  

### JavaScript Validation

[JSHint](https://jshint.com/) was used to validate the small amount of JavaScript code added to the project. 

<hr>

### Python Validation

[CI Python Linter](https://pep8ci.herokuapp.com/#) was used to validate the Python files that were created or edited by myself. No issues presented and line lengths were double checked. I have included some screenshots with the results below.

| Feature | admin.py | forms.py | models.py | urls.py | views.py |
|---------|----------|----------|-----------|---------|----------|
| Review | [no errors](documentation/testing/review_admin.png) | [no errors](documentation/testing/review_forms.png) | [no errors](documentation/testing/review_models.png) | [no errors](documentation/testing/review_urls.png) | [no errors](documentation/testing/review_views.png) |
| Profile  | [no errors](documentation/testing/profile_admin.png) | [no errors](documentation/testing/profile_forms.png) | [no errors](documentation/testing/profile_models.png) | [no errors](documentation/testing/profile_urls.png) | [no errors](documentation/testing/profile_views.png) |
| Stage Score main app | na | na | na | [no errors](documentation/testing/stagescore_urls.png) | na |
| Home | na | na | na | [no errors](documentation/testing/home_urls.png) | [no errors](documentation/testing/home_views.png) |
| User | [no errors](/documentation/images/user-app-admin.py.png) | [no errors](/documentation/images/user-app-forms.py.png) | [no errors](/documentation/images/user-app-models.py.png) | [no errors](/documentation/images/user-app-urls.py.png) | [no errors](/documentation/images/) |


<hr>

### CSS Validation 

[W3C CSS Validator](https://jigsaw.w3.org/css-validator/) was used to validate my CSS file.

![css validation](documentation/testing/css_valid.png)

<hr> 

## Bugs

| **Bugs**                    | **Location**                              | **Cause**                                                                               | **Solution / Fix**                                                                                                                                              | **Status** |
|-----------------------------|------------------------------------------|---------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|------------|
| Relation does not exist error | Blog app database tables (blog_category and blog_review) | Corrupted database state or missing tables due to failed migrations.                 | Deleted the blog app entirely. Created a new app named `music_blog`, redefined models, ran `makemigrations` and `migrate` to rebuild the database tables.      | Fixed      |
| InvalidCursorName error      | Admin page for `blog/review/add/`         | Missing database table caused by incomplete or failed migrations.                     | Removed the broken blog app. Updated references across the project to point to the new `music_blog` app. Reapplied migrations and fixed database schema.       | Fixed      |
| Model sync issues            | Profile view `/profile/`                 | Missing or inconsistent `blog_review` table due to migration failures.                | Created clean migrations for the `music_blog` app. Ensured all related views, URLs, and templates referenced the new app. Applied migrations to sync the schema. | Unfixed    |
| Pagination Error             | Blog page, next button                   | One or more posts were missing slug values or had invalid data (e.g., missing author or category). | Ensure the slug is auto-populated in the model, and filter out posts with invalid or missing fields in the view.                                              | Fixed      |
| Missing Slug Field           | Blog posts                               | Posts created before the slug field was auto-populated lacked valid slugs.            | Update the `Review` model to auto-generate slugs using the `slugify` method if a slug is missing.                                                             | Fixed      |
| Author Deletion Error        | Blog posts                               | A post was linked to an author who was deleted, causing a `NoneType` issue in queries and views. | Change the `author` field to `on_delete=models.SET_NULL` and add `null=True` and `blank=True` options to the field.                                            | Fixed      |
| Orphaned Posts               | Blog database                            | Existing data in the database had posts without slugs, authors, or categories.        | Clean up the database by deleting or fixing posts with missing slugs, authors, or categories using Django shell.                                              | Fixed      |
| Broken Template Links        | Blog template (HTML)                     | Links to details page failed due to missing slug or category in the URL patterns.      | Validate posts in the template and show only valid posts with slug and category to prevent broken links.                                                      | Fixed      |
| Data Integrity Validation Missing | Blog model and admin                   | There were no validations in place to prevent saving invalid posts without slugs or authors. | Add validation in the `clean` method of the `Review` model to enforce data integrity during save operations.                                                   | Fixed      |
