# **pdf_tool**

## Overview

pdf_tool is a versatile and user-friendly tool designed to handle PDF manipulation tasks such as splitting and merging PDF documents. This project aims to provide a seamless experience for users who need to manage their PDF files efficiently through a web interface.

### Current Status
- **Working**: Basic application setup, PyTest for testing, initial web interface, file upload functionality.
- **In Progress**: Front-end enhancements, drag and drop functionality, displaying uploaded files as icons,
- **Planned**: Advanced splitting options, improved file management features.

## Features

- **PDF Splitter**: Split PDF documents.
- **PDF Merger**: Merge multiple PDF files into a single document.
- **Drag and Drop**: Easily upload files by dragging them to the web interface. (In progress)
- **File Icons**: Uploaded files are displayed as icons for better visual management. (In progress)

## Installation

To run this project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/DeanGuterman/pdf_tool.git
   cd pdf_tool
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python src/main.py
   ```

## Usage

1. Open your web browser and navigate to `http://localhost:5000`.
2. Use the interface to upload PDF files.
3. Choose the desired operation (split or merge).
4. Download the processed PDF files.

## Project Structure

- **src/**: Contains the main application code.
- **templates/**: HTML templates for the web interface.
- **tests/**: Unit tests for the project.
- **requirements.txt**: List of dependencies.

# TODO List
* ## _General Tasks:_
  - [x] Implement PyTest for testing.
  - [x] Initial web interface setup.
  - [x] Basic file upload functionality.
  - [ ] Develop a front-end interface.
  - [ ] Enable dragging files from the desktop to the web interface.
  - [ ] Display uploaded files as icons, rather than file names.
  
* ##  _Splitter Tasks:_
  - [ ] Implement the ability to split specific pages from the original document.
  
* ## _Merger Tasks:_
  - [ ] Display all uploaded files before submission, rather than only the latest one.

* ## _Currently Working On:_
  - [ ] Front-end enhancements
  - [ ] Drag and drop functionality
  - [ ] Displaying uploaded files as icons

 