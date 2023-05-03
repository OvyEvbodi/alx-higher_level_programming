// Updates the text color of the <header> element to red (#FF0000)
// when the user clicks on the tag DIV#red_header

const header = $('header');
const redDiv = $('div#red_header');

changeColor = () => header.css('color', '#FF0000');
redDiv.on('click', changeColor);
