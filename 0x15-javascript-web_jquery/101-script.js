// Adds, removes and clears LI elements from a list when the user clicks,
// depending on the button clicked

const addLi = () => $('ul.my_list').append($('<li></li>').text('Item'));
const removeLi = () => $('ul.my_list li:last').remove();
const clearUl = () => $('ul.my_list').empty();

$('document').ready(() => {
  $('div#add_item').click(addLi);
  $('div#remove_item').click(removeLi);
  $('div#clear_list').click(clearUl);
});
