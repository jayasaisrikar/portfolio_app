# Portfolio Website

This is a personal portfolio website showcasing projects, skills, and contact information. The website features a modern design with interactive elements and animations to enhance user experience.

## Features

- **VANTA Background**: A dynamic globe animation using VANTA.js.
- **Custom Cursor**: A visually appealing cursor with hover and click animations.
- **Responsive Design**: Mobile-friendly layout with a responsive navbar.
- **Smooth Scrolling**: Enhanced user experience with smooth scrolling behavior.
- **Animated Sections**: Sections reveal with animations using AOS (Animate On Scroll).
- **Interactive Project Cards**: 3D hover effects on project cards.
- **Dynamic Scroll Progress**: A progress bar indicating the scroll position.

## Technologies Used

- **HTML5 & CSS3**: For structuring and styling the website.
- **JavaScript**: For interactivity and animations.
- **VANTA.js**: For the animated background.
- **AOS (Animate On Scroll)**: For scroll animations.
- **Font Awesome**: For icons.

## Setup and Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/portfolio-website.git
   ```

2. Navigate to the project directory:
   ```bash
   cd portfolio-website
   ```

3. Open `index.html` in your browser to view the website.

## File Structure

- **index.html**: The main HTML file.
- **static/css/style.css**: Custom styles for the website.
- **static/js/main.js**: JavaScript for interactivity and animations.

## Code Highlights

- **Custom Cursor Implementation**:
  ```javascript:static/js/main.js
  // Custom cursor
    const cursor = document.createElement('div');
    const cursorDot = document.createElement('div');
    cursor.className = 'custom-cursor';
    cursorDot.className = 'custom-cursor-dot';
    document.body.appendChild(cursor);
    document.body.appendChild(cursorDot);

    document.addEventListener('mousemove', (e) => {
        requestAnimationFrame(() => {
            cursor.style.left = e.clientX + 'px';
            cursor.style.top = e.clientY + 'px';
            cursorDot.style.left = e.clientX + 'px';
            cursorDot.style.top = e.clientY + 'px';
        });
    });

    // Add click animation
    document.addEventListener('mousedown', () => {
        cursor.classList.add('clicking');
    });

    document.addEventListener('mouseup', () => {
        cursor.classList.remove('clicking');
    });
  ```

- **Responsive Navbar**:
  ```css:static/css/style.css
  .navbar {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    padding: 1.5rem 3rem;
    background: rgba(10, 25, 47, 0.85);
    backdrop-filter: blur(10px);
    z-index: 1000;
    transition: all 0.3s ease;
}




## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

For any inquiries, please contact [Jaya Sai Srikar](mailto:bjayasaisrikar@gmail.com).
