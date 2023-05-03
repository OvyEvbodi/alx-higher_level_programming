// Updates the text of the <header> element to New Header!!!
// when the user clicks on DIV#update_header

const header = $('header');
const updateDiv = $('div#update_header');

const changeColor = () => header.text('New Header!!!');
updateDiv.on('click', changeColor);

