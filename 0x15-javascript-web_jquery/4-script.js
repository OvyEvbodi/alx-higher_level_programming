// Toggles the class of the <header> element between red and green
// when the user clicks on the tag DIV#toggle_header

const header = $('header');
const redDiv = $('div#toggle_header');

toggleElementClass = () => {
    header.toggleClass('red');
    header.toggleClass('green');
};

redDiv.on('click', toggleElementClass);
