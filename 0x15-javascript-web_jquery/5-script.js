// Adds a <li> element to a list when the user clicks on the tag DIV#add_item

const ulList = $('ul.my_list');
const liDiv = $('div#add_item');
const listElement = $('<li></li>').text('Item');

appendElement = () => ulList.append(listElement);

liDiv.on('click', appendElement);
