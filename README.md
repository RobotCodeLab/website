# Robot Code Lab website

* Install [Jekyll](https://jekyllrb.com/docs/installation/)  (version less than 4.0 required) on your local computer
* On MacOS, you will need to upgrade your Ruby version from the depricated v2.3 that is shipped. Follow the above Jekyll instructions closely.
* Run `$ bundle exec jekyll serve` in the repository root directory
* Your site is now hosted locally at `localhost:4000`, which you can access with your web browser.
* It will be automatically re-built as you save changes to the files it contains.
   Refreshing your web browser reveals these changes.

Note:
* This webpage uses Jekyll plugins like Jekyll Scholar to automatically build your bibliography. 
  If you are using Github pages then you will have to build the site with the `Rakefile` in the root directory of the source branch.

## Customization

* Modify `_config.yml` as appropriate
* Modify YAML database files, located in `_data/*.yml`, as appropriate
* Modify individual pages, located in `_pages/*.md`, as appropriate

### Navbar

The pages listed in the top navbar are located in `_config.yml` file.
The typical options are already included or commented, though additional pages can be created and listed here.

### Creating or editing pages

All pages are located in the `_pages` directory.
Pages generally load information from YAML databases located as `_data/*.yml`.
Creating new pages can be done by using existing pages as a template.

#### Page header information

All pages require header information.
Example header data for the 'Talks' page is below.
```
---
title: "Talks"
layout: gridlay
sitemap: false
permalink: /talks/
---
```
The `layout` variable corresponds to HTML layouts in the `_layouts` directory.
The differences between most layouts is subtle and `gridlay` can generally be used.
The permalink must be unique for each page, and corresponds to the directory that will store the page in the compiled HTML.
Refer to your pages in `_config.yml` via the `title` variable.

#### Markdown

All pages are written in [Markdown](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) as `*.md`.
HTML commands and CSS styles can be directly used in a markdown files.

#### Publication page and database

The publications and talks are now listed via Jekyll Scholar.
The bibliography file `ref.bib` is located in the `cv/` directory.
Modify according to your needs.


## Acknowledgment

Cudos to the [Allen Lab](https://www.allanlab.org/) for creating a beautiful academic research group webpage.
Many parts of this site were adopted or copied from their laboratory webpage.

