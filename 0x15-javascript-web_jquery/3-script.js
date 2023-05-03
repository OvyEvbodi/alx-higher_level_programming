// dds the class red to the <header> element
// when the user clicks on the tag DIV#red_header

const header = $('header');
const redDiv = $('div#red_header');

const changeColor = () => header.addClass('red');
redDiv.on('click', changeColor);
