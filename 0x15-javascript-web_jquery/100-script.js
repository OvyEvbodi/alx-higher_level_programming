// Updates the text color of the <header> element to red (#FF0000)

changeColor = () => {
  const header = document.querySelector('header');
  header.style.color = '#FF0000'
};
document.addEventListener('DOMContentLoaded', changeColor);
